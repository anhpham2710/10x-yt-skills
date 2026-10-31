#!/usr/bin/env python3
"""loc-loai.py — lọc bảng video theo cột `loai` (dai | short) và in CSV đã lọc ra đầu ra chuẩn.

Chạy tại máy, chỉ dùng thư viện chuẩn của Python 3, không gọi mạng, KHÔNG ghi tệp.
Dùng với ống, để không tạo tệp tạm nào ngoài ho-so-kenh/:

    python3 scripts/loc-loai.py <tệp.csv> --loai dai | python3 references/chung/tinh-median.py /dev/stdin --ngay-quet <YYYY-MM-DD> --cua-so-thang 6

Giữ nguyên mọi cột và thứ tự dòng; chỉ bỏ dòng có `loai` khác giá trị đã chọn. Số dòng giữ/bỏ in ra stderr.
Không có cột `loai`: in nguyên tệp và báo ở stderr (coi cả tệp là một định dạng). Ô `loai` trống tính là `dai`.
Mã thoát: 0 = xong · 1 = lỗi đầu vào (không có tệp, tệp rỗng, `--loai` lạ).
"""
import argparse
import csv
import sys

LOAI_HOP_LE = ("dai", "short")


def main():
    ap = argparse.ArgumentParser(description="Lọc bảng video theo cột loai, in CSV ra đầu ra chuẩn")
    ap.add_argument("tep", help="CSV có dòng tiêu đề")
    ap.add_argument("--loai", required=True, choices=LOAI_HOP_LE, help="định dạng cần giữ: dai | short")
    a = ap.parse_args()
    try:
        with open(a.tep, newline="", encoding="utf-8-sig") as f:
            doc = csv.DictReader(f)
            if not doc.fieldnames:
                print("tệp rỗng, không có dòng tiêu đề", file=sys.stderr)
                return 1
            cot = [c.strip() for c in doc.fieldnames]
            ra = csv.writer(sys.stdout, lineterminator="\n")
            ra.writerow(cot)
            giu = bo = 0
            co_loai = "loai" in cot
            for hang in doc:
                hang = {(k or "").strip(): v for k, v in hang.items()}
                lo = (hang.get("loai") or "").strip().lower() or "dai"
                if co_loai and lo != a.loai:
                    bo += 1
                    continue
                giu += 1
                ra.writerow([hang.get(c, "") for c in cot])
    except OSError as e:
        print("không đọc được tệp: %s" % e, file=sys.stderr)
        return 1
    if not co_loai:
        print("không có cột loai: in nguyên %d dòng" % giu, file=sys.stderr)
    else:
        print("loai=%s: giữ %d dòng, bỏ %d dòng" % (a.loai, giu, bo), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
