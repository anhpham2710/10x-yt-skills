#!/usr/bin/env python3
"""tinh-median.py — tính median lượt xem của TỪNG KÊNH và bội số của từng video.

Chạy tại máy, chỉ dùng thư viện chuẩn của Python 3, không gọi mạng, không ghi tệp.

Đầu vào: tệp CSV có dòng tiêu đề, các cột đọc theo TÊN (thứ tự tuỳ ý, cột thừa bị bỏ qua):
    tieu_de, ngay_dang, luot_xem            (bắt buộc)
    kenh                                    (tuỳ chọn; thiếu thì coi cả tệp là một kênh)
`ngay_dang` nhận YYYY-MM-DD hoặc DD/MM/YYYY. `luot_xem` nhận 12345, 12.345, 12,345.

Luật tính (viết lại độc lập từ ý "median của chính kênh" của Jake, MIT — xem NGUON.md):
  1. Bội số = lượt xem của video ÷ median lượt xem của CHÍNH kênh đó.
  2. Video đăng chưa đủ 7 ngày tính tới ngày quét bị loại khỏi median và khỏi bội số
     (số xem còn đang leo, không so được).
  3. Kênh có ít hơn 4 video đủ điều kiện thì TỪ CHỐI tính bội số: median của dưới 4 video
     không phải median. Script không tự nới ngưỡng này.
  4. Ô lượt xem trống hoặc không đọc được là "thiếu số", KHÔNG phải 0. Dòng đó bị bỏ và báo.

Mã thoát: 0 = có ít nhất một kênh được tính · 2 = không kênh nào đủ điều kiện (từ chối)
          · 1 = lỗi đầu vào (tệp không có, thiếu cột bắt buộc, tệp rỗng).

Cách chạy:
    python3 tinh-median.py so-video.csv
    python3 tinh-median.py so-video.csv --ngay-quet 2026-10-24 --cua-so-thang 6 --json
"""

import argparse
import csv
import json
import statistics
import sys
from datetime import date, datetime, timedelta

MIN_VIDEO = 4          # luật "< 4 video thì không phải median"
MIN_TUOI_NGAY = 7      # video đăng chưa đủ 7 ngày bị loại
KENH_MAC_DINH = "(tệp không ghi kênh)"
COT_BAT_BUOC = ("tieu_de", "ngay_dang", "luot_xem")


def doc_ngay(chuoi):
    chuoi = (chuoi or "").strip()
    for dang in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(chuoi, dang).date()
        except ValueError:
            continue
    return None


def doc_luot_xem(chuoi):
    """Trả về số nguyên, hoặc None nếu trống/không đọc được (None KHÔNG phải 0)."""
    s = (chuoi or "").strip().replace(" ", "")
    if not s:
        return None
    s = s.replace(".", "").replace(",", "")
    return int(s) if s.isdigit() else None


def doc_tep(duong_dan):
    """Đọc CSV, trả về (danh sách dòng hợp lệ, danh sách cảnh báo dòng hỏng)."""
    with open(duong_dan, newline="", encoding="utf-8-sig") as f:
        doc = csv.DictReader(f)
        if not doc.fieldnames:
            raise ValueError("tệp rỗng, không có dòng tiêu đề")
        cot = [c.strip() for c in doc.fieldnames]
        thieu = [c for c in COT_BAT_BUOC if c not in cot]
        if thieu:
            raise ValueError("thiếu cột bắt buộc: " + ", ".join(thieu))
        dong_ok, canh_bao = [], []
        for so_dong, hang in enumerate(doc, start=2):
            hang = {(k or "").strip(): v for k, v in hang.items()}
            ngay = doc_ngay(hang.get("ngay_dang"))
            luot = doc_luot_xem(hang.get("luot_xem"))
            tieu_de = (hang.get("tieu_de") or "").strip()
            if ngay is None or luot is None:
                ly_do = "ngày đăng không đọc được" if ngay is None else "thiếu số lượt xem"
                canh_bao.append(f"dòng {so_dong} ({tieu_de[:40] or 'không tiêu đề'}): {ly_do} — bỏ, không coi là 0")
                continue
            kenh = (hang.get("kenh") or "").strip() or KENH_MAC_DINH
            dong_ok.append({"kenh": kenh, "tieu_de": tieu_de, "ngay_dang": ngay, "luot_xem": luot})
        return dong_ok, canh_bao


def tru_thang(ngay, so_thang):
    """Lùi so_thang tháng (xấp xỉ 30,44 ngày/tháng — đủ cho cửa sổ lọc, không dùng để tính khác)."""
    return ngay - timedelta(days=round(so_thang * 30.44))


def tinh(dong, ngay_quet, cua_so_thang=None):
    """Gom theo kênh và tính. Trả về danh sách kết quả, mỗi kênh một phần tử."""
    theo_kenh = {}
    for d in dong:
        theo_kenh.setdefault(d["kenh"], []).append(d)

    ket_qua = []
    for kenh, ds in theo_kenh.items():
        cua_so = ds
        ngoai_cua_so = 0
        if cua_so_thang:
            tu = tru_thang(ngay_quet, cua_so_thang)
            cua_so = [d for d in ds if d["ngay_dang"] >= tu]
            ngoai_cua_so = len(ds) - len(cua_so)
        du_dk = [d for d in cua_so if (ngay_quet - d["ngay_dang"]).days >= MIN_TUOI_NGAY]
        qua_moi = len(cua_so) - len(du_dk)

        kq = {
            "kenh": kenh,
            "so_video_doc_duoc": len(ds),
            "ngoai_cua_so": ngoai_cua_so,
            "loai_vi_duoi_7_ngay": qua_moi,
            "so_video_du_dieu_kien": len(du_dk),
            "median": None,
            "trang_thai": None,
            "video": [],
        }
        if len(du_dk) < MIN_VIDEO:
            kq["trang_thai"] = (
                f"TỪ CHỐI: chỉ có {len(du_dk)} video đủ điều kiện (cần ≥ {MIN_VIDEO}); "
                "median của dưới 4 video không phải median, không tính bội số cho kênh này"
            )
        else:
            med = statistics.median(d["luot_xem"] for d in du_dk)
            if med <= 0:
                kq["trang_thai"] = "TỪ CHỐI: median bằng 0, không chia được"
            else:
                kq["median"] = med
                kq["trang_thai"] = "ĐÃ TÍNH"
                for d in sorted(du_dk, key=lambda x: -x["luot_xem"]):
                    kq["video"].append({
                        "tieu_de": d["tieu_de"],
                        "ngay_dang": d["ngay_dang"].isoformat(),
                        "luot_xem": d["luot_xem"],
                        "boi_so": round(d["luot_xem"] / med, 2),
                    })
        ket_qua.append(kq)
    return ket_qua


def in_bang(ket_qua, canh_bao, ngay_quet):
    dong = [f"[SỐ LIỆU] ngày quét {ngay_quet.isoformat()} · tính tại máy bằng tinh-median.py", ""]
    for kq in ket_qua:
        dong.append(f"Kênh: {kq['kenh']}")
        dong.append(
            f"  đọc được {kq['so_video_doc_duoc']} video · ngoài cửa sổ {kq['ngoai_cua_so']} · "
            f"loại vì đăng chưa đủ 7 ngày {kq['loai_vi_duoi_7_ngay']} · đủ điều kiện {kq['so_video_du_dieu_kien']}"
        )
        dong.append(f"  {kq['trang_thai']}")
        if kq["median"] is not None:
            dong.append(f"  median lượt xem của kênh: {kq['median']:,.0f}".replace(",", "."))
            dong.append("  bội số | lượt xem | ngày đăng  | tiêu đề")
            for v in kq["video"]:
                dong.append(
                    f"  {v['boi_so']:>5.2f}× | {v['luot_xem']:>8} | {v['ngay_dang']} | {v['tieu_de']}"
                )
        dong.append("")
    if canh_bao:
        dong.append("Dòng bị bỏ:")
        dong.extend("  - " + c for c in canh_bao)
    return "\n".join(dong).rstrip() + "\n"


def main(argv=None):
    p = argparse.ArgumentParser(description="Median lượt xem theo kênh + bội số từng video (không mạng).")
    p.add_argument("tep_csv", help="CSV: tieu_de,ngay_dang,luot_xem[,kenh]")
    p.add_argument("--ngay-quet", help="YYYY-MM-DD; mặc định là hôm nay. Ghi ngày này vào video-thang.md")
    p.add_argument("--cua-so-thang", type=float, help="chỉ tính video đăng trong N tháng gần nhất")
    p.add_argument("--json", action="store_true", help="in JSON thay cho bảng chữ")
    args = p.parse_args(argv)

    if args.ngay_quet:
        ngay_quet = doc_ngay(args.ngay_quet)
        if ngay_quet is None:
            print("Lỗi: --ngay-quet phải là YYYY-MM-DD", file=sys.stderr)
            return 1
    else:
        ngay_quet = date.today()

    try:
        dong, canh_bao = doc_tep(args.tep_csv)
    except (OSError, ValueError) as loi:
        print(f"Lỗi đầu vào: {loi}", file=sys.stderr)
        return 1
    if not dong:
        print("Lỗi đầu vào: không có dòng nào đọc được (kiểm cột ngay_dang và luot_xem)", file=sys.stderr)
        for c in canh_bao:
            print("  - " + c, file=sys.stderr)
        return 1

    ket_qua = tinh(dong, ngay_quet, args.cua_so_thang)
    if args.json:
        print(json.dumps({"ngay_quet": ngay_quet.isoformat(), "kenh": ket_qua, "dong_bi_bo": canh_bao},
                         ensure_ascii=False, indent=2))
    else:
        print(in_bang(ket_qua, canh_bao, ngay_quet), end="")
    return 0 if any(kq["median"] is not None for kq in ket_qua) else 2


if __name__ == "__main__":
    sys.exit(main())
