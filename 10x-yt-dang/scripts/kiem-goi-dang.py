#!/usr/bin/env python3
"""kiem-goi-dang.py — kiểm tệp gói đăng `ho-so-kenh/goi/<ma>-dang.md` của skill 10x-yt-dang.

Chạy tại máy, chỉ dùng thư viện chuẩn của Python 3, không gọi mạng, không ghi tệp.

Cách dùng:
    python3 kiem-goi-dang.py <tệp gói đăng> [--ban-chep-loi <tệp>] [--cum "<cụm>"]...

Đọc theo khuôn cố định của SKILL.md («Khuôn đầu ra»):
  - khối mô tả = khối ``` đầu tiên sau mục «## 1.»
  - dòng `thẻ: a, b, c`
  - dòng `- tieu-de:`, `- muc-tieu-nguon-view:`, `- ban-quay:`
  - chương = dòng «mm:ss Tên» trong khối mô tả; hashtag = chữ #… trong khối mô tả

Mỗi kiểm in một dòng `KIEM <tên>: XANH` hoặc `KIEM <tên>: DO <lý do>`.
Thoát mã 0 khi mọi kiểm xanh, mã 1 khi có kiểm đỏ, mã 2 khi không đọc được tệp hoặc khuôn sai.

Giới hạn ký tự (tiêu đề ≤ 100, mô tả ≤ 5000, thẻ ≤ 500) là giới hạn hiện hành của YouTube Studio;
ngưỡng 6–12 thẻ, 3–5 hashtag, ±15 giây, 3 lần nhắc cụm là [ĐỀ XUẤT] của bộ (03 §3.9, 04 §5.10).
"""
import argparse
import re
import sys
import unicodedata

MAX_TIEU_DE = 100
MAX_MO_TA = 5000
MAX_THE_KY_TU = 500
THE_MIN, THE_MAX = 6, 12
HASHTAG_MIN, HASHTAG_MAX = 3, 5
LECH_GIAY = 15
CHUONG_MIN_SO = 3
CHUONG_MIN_GIAY = 10
CUM_MAX_LAN = 3

RE_MOC = r"(?:\d{1,2}:)?\d{1,2}:\d{2}"
RE_CHUONG = re.compile(r"^\s*(" + RE_MOC + r")\s+(\S.*)$")
RE_MOC_BAN_CHEP = re.compile(r"\[(" + RE_MOC + r")\]")


def nfc(s):
    return unicodedata.normalize("NFC", s)


def ra_giay(moc):
    phan = [int(p) for p in moc.split(":")]
    giay = 0
    for p in phan:
        giay = giay * 60 + p
    return giay


def doc_truong(text, ten):
    m = re.search(r"^-\s*" + re.escape(ten) + r":\s*(.*)$", text, re.M)
    return m.group(1).strip() if m else None


def tach_khoi_mo_ta(text):
    m = re.search(r"^##\s*1\..*?$", text, re.M)
    if not m:
        return None
    sau = text[m.end():]
    f = re.search(r"^```[^\n]*\n(.*?)^```", sau, re.M | re.S)
    return f.group(1).rstrip("\n") if f else None


def tach_the(text):
    m = re.search(r"^\s*th[ẻe]:\s*(.+)$", nfc(text), re.M | re.I)
    if not m:
        return None
    return [t.strip() for t in m.group(1).split(",") if t.strip()]


def moc_ban_chep_loi(text):
    return sorted({ra_giay(m) for m in RE_MOC_BAN_CHEP.findall(text)})


def kiem(tep, ban_chep_loi, van_ban_bcl, cum_list):
    text = nfc(open(tep, encoding="utf-8").read())
    ket_qua = []

    def ghi(ten, ok, ly_do=""):
        ket_qua.append((ten, ok, ly_do))

    mo_ta = tach_khoi_mo_ta(text)
    the = tach_the(text)
    if mo_ta is None or the is None:
        print("KHUON-SAI: không tìm thấy khối mô tả (mục «## 1.» có khối ```) hoặc dòng «thẻ:»")
        return None

    # T1 giới hạn
    tieu_de = doc_truong(text, "tieu-de") or ""
    tieu_de = re.sub(r"\s*\(nguồn:.*\)\s*$", "", tieu_de)
    ghi("tieu-de<=100", len(tieu_de) <= MAX_TIEU_DE, f"{len(tieu_de)} ký tự")
    ghi("mo-ta<=5000", len(mo_ta) <= MAX_MO_TA, f"{len(mo_ta)} ký tự")
    tong_the = len(", ".join(the))
    ghi("the<=500-ky-tu", tong_the <= MAX_THE_KY_TU, f"{tong_the} ký tự")
    ghi("so-the-6-12", THE_MIN <= len(the) <= THE_MAX, f"{len(the)} thẻ")
    hashtag = re.findall(r"(?<!\S)#[^\s#]+", mo_ta)
    ghi("hashtag-3-5", HASHTAG_MIN <= len(hashtag) <= HASHTAG_MAX, f"{len(hashtag)} hashtag")

    # T2 + T6 chương
    chuong = []
    for dong in mo_ta.split("\n"):
        m = RE_CHUONG.match(dong)
        if m:
            chuong.append((ra_giay(m.group(1)), m.group(1), m.group(2).strip()))
    ban_quay = (doc_truong(text, "ban-quay") or "").lower()
    khong_ban_quay = ban_quay.startswith("khong-co") or ban_quay.startswith("không")
    if khong_ban_quay:
        ghi("khong-ban-quay-khong-chuong", len(chuong) == 0, f"{len(chuong)} mốc chương dù không có bản quay")
    if chuong:
        moc = [c[0] for c in chuong]
        ghi("chuong-tu-3-moc", len(chuong) >= CHUONG_MIN_SO, f"{len(chuong)} mốc")
        ghi("chuong-dau-00:00", moc[0] == 0, f"mốc đầu {chuong[0][1]}")
        tang = all(b - a >= CHUONG_MIN_GIAY for a, b in zip(moc, moc[1:]))
        ghi("chuong-cach-10s", tang, "có hai mốc cách nhau dưới 10 giây hoặc không tăng dần")
        if ban_chep_loi is not None:
            if not ban_chep_loi:
                ghi("chuong-khop-ban-chep-loi", False, "bản chép lời không có mốc [mm:ss] nào")
            else:
                dai = max(ban_chep_loi)
                loi = []
                for g, ten_moc, _ in chuong:
                    gan = min(abs(g - b) for b in ban_chep_loi)
                    if g > dai:
                        loi.append(f"{ten_moc} vượt độ dài bản chép lời")
                    elif gan > LECH_GIAY:
                        loi.append(f"{ten_moc} cách dòng gần nhất {gan}s")
                ghi("chuong-khop-ban-chep-loi", not loi, "; ".join(loi))

    # T3 hai câu đầu + T4 nhắc cụm
    dau = re.split(r"(?<=[.!?…])\s+", mo_ta.strip(), maxsplit=2)[:2]
    hai_cau = nfc(" ".join(dau)).lower()
    cum_list = [nfc(c).lower() for c in cum_list]
    if cum_list:
        ghi("hai-cau-dau-co-cum", any(c in hai_cau for c in cum_list), "hai câu đầu không chứa cụm nào")
        toan = nfc(mo_ta).lower()
        qua = [f"«{c}» {toan.count(c)} lần" for c in cum_list if toan.count(c) > CUM_MAX_LAN]
        ghi("cum<=3-lan", not qua, "; ".join(qua))

    # T4 thẻ là năm: chỉ hợp lệ khi chữ năm có trong bản quay
    for t in the:
        for n in re.findall(r"(?<!\d)(?:19|20)\d{2}(?!\d)", t):
            if ban_chep_loi is None:
                ghi("the-nam-co-trong-ban-quay", False, f"thẻ «{t}» có năm {n}: cần --ban-chep-loi để kiểm")
            else:
                ghi("the-nam-co-trong-ban-quay", n in van_ban_bcl, f"năm {n} trong thẻ «{t}» không có trong bản chép lời")

    # T5 đăng riêng tư trước
    thap = text.lower()
    ghi("dang-rieng-tu-truoc", "đăng riêng tư/không công khai trước" in thap, "thiếu dòng đăng riêng tư/không công khai trước")
    ghi("tu-bam-cong-khai", "tự bấm công khai" in thap, "thiếu câu người dùng tự bấm công khai")
    return ket_qua


def main(argv=None):
    p = argparse.ArgumentParser(description="Kiểm gói đăng của 10x-yt-dang")
    p.add_argument("tep")
    p.add_argument("--ban-chep-loi", help="tệp bản chép lời có mốc [mm:ss]")
    p.add_argument("--cum", action="append", default=[], help="cụm tìm kiếm thật (lặp được)")
    a = p.parse_args(argv)
    try:
        ban = None
        van_ban_bcl = ""
        if a.ban_chep_loi:
            van_ban_bcl = nfc(open(a.ban_chep_loi, encoding="utf-8").read())
            ban = moc_ban_chep_loi(van_ban_bcl)
        kq = kiem(a.tep, ban, van_ban_bcl, a.cum)
    except OSError as e:
        print(f"KHUON-SAI: không đọc được tệp: {e}")
        return 2
    if kq is None:
        return 2
    do = 0
    for ten, ok, ly_do in kq:
        if ok:
            print(f"KIEM {ten}: XANH")
        else:
            do += 1
            print(f"KIEM {ten}: DO {ly_do}")
    return 1 if do else 0


if __name__ == "__main__":
    sys.exit(main())
