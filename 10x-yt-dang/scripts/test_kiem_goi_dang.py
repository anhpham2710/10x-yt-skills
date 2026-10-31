#!/usr/bin/env python3
"""Test cho kiem-goi-dang.py. Chạy: python3 skills/10x-yt-dang/scripts/test_kiem_goi_dang.py
Mỗi kiểm được ép chạy qua cả nhánh XANH lẫn nhánh ĐỎ (một bản tốt, rồi các bản hỏng đúng một chỗ)."""
import importlib.util
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("kiem", os.path.join(HERE, "kiem-goi-dang.py"))
kiem = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kiem)

BAN_CHEP_LOI = """# Bản chép lời
[00:00] Hôm nay mình nói về cách cài đặt kênh
[00:20] Phần thứ nhất là ảnh đại diện
[01:05] Phần thứ hai là mô tả kênh
[02:10] Phần cuối là lịch đăng
[02:40] Cảm ơn các bạn
"""

GOI = """# Gói đăng: Cài đặt kênh YouTube · lượt 2026-10-25

- ma: 01-cai-dat-kenh
- tieu-de: Cài đặt kênh YouTube đúng cách (nguồn: người dùng đưa)
- muc-tieu-nguon-view: tim-kiem
- cum-tim-kiem: cài đặt kênh youtube
- ban-quay: co-moc-thoi-gian
- ghi-chu: giả thuyết

## 1. Mô tả (dán nguyên khối vào ô «Mô tả»)

```
Video này hướng dẫn cài đặt kênh youtube cho người mới. Xem xong bạn có kênh sẵn sàng đăng video đầu tiên.

Câu hỏi hay gặp: ảnh đại diện nên chọn thế nào? Chọn ảnh rõ mặt, nền đơn giản.

00:00 Mở đầu
00:20 Ảnh đại diện
01:05 Mô tả kênh
02:10 Lịch đăng

#kenhyoutube #caidat #chuyengia
```

## 2. Thẻ

thẻ: cài đặt kênh youtube, cai dat kenh youtube, ảnh đại diện kênh, mô tả kênh, lịch đăng video, kênh cho chuyên gia

## 5. Đăng thế nào

- Nên đăng riêng tư/không công khai trước, rồi bạn tự bấm công khai.
"""


def chay(noi_dung, ban_chep=True, cum=("cài đặt kênh youtube",), thay=None):
    if thay:
        for a, b in thay:
            assert a in noi_dung, a
            noi_dung = noi_dung.replace(a, b)
    with tempfile.TemporaryDirectory() as d:
        tep = os.path.join(d, "g.md")
        open(tep, "w", encoding="utf-8").write(noi_dung)
        bcl = None
        if ban_chep:
            bcl = os.path.join(d, "bcl.md")
            open(bcl, "w", encoding="utf-8").write(BAN_CHEP_LOI)
        ban = kiem.moc_ban_chep_loi(BAN_CHEP_LOI) if ban_chep else None
        kq = kiem.kiem(tep, ban, BAN_CHEP_LOI if ban_chep else "", list(cum))
    return {t: (ok, ly) for t, ok, ly in kq}


class TestKiem(unittest.TestCase):
    def test_ban_tot_xanh_het(self):
        kq = chay(GOI)
        do = {t: v for t, v in kq.items() if not v[0]}
        self.assertEqual(do, {})
        self.assertIn("chuong-khop-ban-chep-loi", kq)  # nhánh có việc thật sự chạy
        self.assertIn("hai-cau-dau-co-cum", kq)

    def test_mo_ta_qua_dai_do(self):
        kq = chay(GOI, thay=[("Chọn ảnh rõ mặt, nền đơn giản.", "Chọn ảnh rõ mặt. " + "x" * 5000)])
        self.assertFalse(kq["mo-ta<=5000"][0])

    def test_qua_it_the_do(self):
        kq = chay(GOI, thay=[("thẻ: cài đặt kênh youtube, cai dat kenh youtube, ảnh đại diện kênh, mô tả kênh, lịch đăng video, kênh cho chuyên gia",
                              "thẻ: a, b, c")])
        self.assertFalse(kq["so-the-6-12"][0])

    def test_the_dai_qua_500_do(self):
        the = ", ".join(["thẻ" + "y" * 60 + str(i) for i in range(10)])
        kq = chay(GOI, thay=[("thẻ: cài đặt kênh youtube, cai dat kenh youtube, ảnh đại diện kênh, mô tả kênh, lịch đăng video, kênh cho chuyên gia", "thẻ: " + the)])
        self.assertFalse(kq["the<=500-ky-tu"][0])

    def test_hashtag_qua_nhieu_do(self):
        kq = chay(GOI, thay=[("#kenhyoutube #caidat #chuyengia", "#a #b #c #d #e #f")])
        self.assertFalse(kq["hashtag-3-5"][0])

    def test_moc_chuong_vuot_ban_chep_loi_do(self):
        kq = chay(GOI, thay=[("02:10 Lịch đăng", "09:10 Lịch đăng")])
        self.assertFalse(kq["chuong-khop-ban-chep-loi"][0])

    def test_moc_khong_khop_dong_nao_do(self):
        # 01:40 cách dòng 01:05 là 35s và cách 02:10 là 30s: lệch quá 15s
        kq = chay(GOI, thay=[("01:05 Mô tả kênh", "01:40 Mô tả kênh")])
        self.assertFalse(kq["chuong-khop-ban-chep-loi"][0])

    def test_chuong_dau_khong_phai_0_do(self):
        kq = chay(GOI, thay=[("00:00 Mở đầu", "00:05 Mở đầu")])
        self.assertFalse(kq["chuong-dau-00:00"][0])

    def test_hai_moc_sat_nhau_do(self):
        kq = chay(GOI, thay=[("00:20 Ảnh đại diện", "00:05 Ảnh đại diện")])
        self.assertFalse(kq["chuong-cach-10s"][0])

    def test_khong_ban_quay_ma_co_chuong_do(self):
        kq = chay(GOI, ban_chep=False, thay=[("ban-quay: co-moc-thoi-gian", "ban-quay: khong-co")])
        self.assertFalse(kq["khong-ban-quay-khong-chuong"][0])

    def test_khong_ban_quay_khong_chuong_xanh(self):
        bo = "00:00 Mở đầu\n00:20 Ảnh đại diện\n01:05 Mô tả kênh\n02:10 Lịch đăng\n\n"
        kq = chay(GOI, ban_chep=False, thay=[("ban-quay: co-moc-thoi-gian", "ban-quay: khong-co"), (bo, "")])
        self.assertTrue(kq["khong-ban-quay-khong-chuong"][0])

    def test_hai_cau_dau_thieu_cum_do(self):
        kq = chay(GOI, thay=[("Video này hướng dẫn cài đặt kênh youtube cho người mới.", "Video này dành cho người mới.")])
        self.assertFalse(kq["hai-cau-dau-co-cum"][0])

    def test_nhoi_cum_do(self):
        nhoi = "Cài đặt kênh youtube. " * 4
        kq = chay(GOI, thay=[("Chọn ảnh rõ mặt, nền đơn giản.", nhoi)])
        self.assertFalse(kq["cum<=3-lan"][0])

    def test_the_nam_khong_co_trong_ban_quay_do(self):
        kq = chay(GOI, thay=[("lịch đăng video,", "lịch đăng video 2027,")])
        self.assertFalse(kq["the-nam-co-trong-ban-quay"][0])

    def test_the_nam_co_trong_ban_quay_xanh(self):
        ban = BAN_CHEP_LOI + "[02:50] cập nhật 2027\n"
        with tempfile.TemporaryDirectory() as d:
            tep = os.path.join(d, "g.md")
            open(tep, "w", encoding="utf-8").write(GOI.replace("lịch đăng video,", "update 2027,"))
            kq = {t: ok for t, ok, _ in kiem.kiem(tep, kiem.moc_ban_chep_loi(ban), ban, [])}
        self.assertTrue(kq["the-nam-co-trong-ban-quay"])

    def test_thieu_dang_rieng_tu_do(self):
        kq = chay(GOI, thay=[("Nên đăng riêng tư/không công khai trước, rồi bạn tự bấm công khai.", "Đăng luôn.")])
        self.assertFalse(kq["dang-rieng-tu-truoc"][0])
        self.assertFalse(kq["tu-bam-cong-khai"][0])

    def test_tieu_de_qua_100_do(self):
        kq = chay(GOI, thay=[("Cài đặt kênh YouTube đúng cách", "Cài đặt " + "kênh " * 30)])
        self.assertFalse(kq["tieu-de<=100"][0])

    def test_khuon_sai_tra_none(self):
        with tempfile.TemporaryDirectory() as d:
            tep = os.path.join(d, "g.md")
            open(tep, "w", encoding="utf-8").write("không có khối nào\n")
            self.assertIsNone(kiem.kiem(tep, None, "", []))

    def test_main_ma_thoat(self):
        with tempfile.TemporaryDirectory() as d:
            tep = os.path.join(d, "g.md")
            bcl = os.path.join(d, "b.md")
            open(tep, "w", encoding="utf-8").write(GOI)
            open(bcl, "w", encoding="utf-8").write(BAN_CHEP_LOI)
            self.assertEqual(kiem.main([tep, "--ban-chep-loi", bcl, "--cum", "cài đặt kênh youtube"]), 0)
            open(tep, "w", encoding="utf-8").write(GOI.replace("#kenhyoutube #caidat #chuyengia", "#a #b #c #d #e #f"))
            self.assertEqual(kiem.main([tep]), 1)
            self.assertEqual(kiem.main([os.path.join(d, "khong-co.md")]), 2)


if __name__ == "__main__":
    unittest.main()
