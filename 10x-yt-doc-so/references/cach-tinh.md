# Cách tính: median của chính kênh, bằng script

Mọi phép so trong `10x-yt-doc-so` là **số của video ÷ median của chính kênh**. Median tính bằng `references/chung/tinh-median.py`, không tính nhẩm (xem `references/chung/nhan-nguon.md`, luật 7). Script chạy tại máy, chỉ dùng Python chuẩn, không gọi mạng.

Script từ chối từng nhóm (kênh, hoặc nguồn khi dùng cột `kenh` làm tên nguồn) có dưới 4 video đủ điều kiện (đăng từ 7 ngày trở lên); chỉ khi không nhóm nào đủ thì thoát với mã 2. Nhóm bị từ chối in dòng «TỪ CHỐI» riêng trong kết quả. Khi đó ghi «chưa đủ video để so» cho nhóm đó. Không nới ngưỡng, không tính tay thay.

## 1. Đọc `so-video.csv`: tên cột nào cũng nhận, ý nghĩa mới quan trọng

Hợp đồng (`references/chung/ho-so-kenh.md`, mục 3.3) khoá các cột `tieu_de, ngay_dang, luot_xem, ma, ti_le_nhap_chuot, thoi_gian_xem_tb, ngay_do` và cho `doc-so` thêm cột ở cuối. Người dùng có thể xuất từ YouTube Studio với tên khác, nên đọc theo ý nghĩa:

| Ý nghĩa | Tên chuẩn | Tên khác nhận được | Ghi chú |
|---|---|---|---|
| Mã video | `ma` | `video_id` | Khoá nối với `de-tai.md`, `goi/`, `kich-ban/` |
| Ngày đăng | `ngay_dang` | | `YYYY-MM-DD` hoặc `DD/MM/YYYY` |
| Lượt xem | `luot_xem` | | Tại `ngay_do` |
| Lượt hiển thị | `hien_thi` | `impressions` | Cột thêm ở cuối |
| CTR (tỉ lệ nhấp) | `ti_le_nhap_chuot` | `ctr` | Đơn vị %, ví dụ `4,27` |
| Thời gian xem TB | `thoi_gian_xem_tb` | | Giây |
| % thời lượng xem TB | `phan_tram_xem_tb` | | Cột thêm ở cuối |
| Giữ chân 30 giây đầu | `giu_chan_30s` | | Cột thêm ở cuối, đơn vị % |
| Nguồn view | `nguon` | | Xem mục 2 |
| Ngày đo | `ngay_do` | | |

**Ô trống nghĩa là chưa đo, không phải 0.** Dòng nào thiếu cột cần cho phép tính nào thì bỏ khỏi phép tính đó và đếm lại số video còn lại. Báo cho người dùng biết đã bỏ dòng nào.

## 2. Tệp có cột `nguon` (mỗi video nhiều dòng, mỗi nguồn một dòng)

Nếu `so-video.csv` có cột `nguon`:

- Dòng có `nguon` **trống hoặc ghi `tong`** là dòng tổng của video. Chỉ các dòng này vào phép tính median lượt xem, hiển thị và giữ chân.
- Dòng có `nguon` điền (`de-xuat`, `tim-kiem`, `duyet`, `ben-ngoai`, `khac`…) là dòng theo nguồn. Chỉ các dòng này vào bảng CTR theo nguồn.
- **Không đưa nguyên tệp vào `tinh-median.py`**: script sẽ đếm một video nhiều lần và median sai im lặng.

Nếu tệp không có cột `nguon`, xin người dùng dán bảng nguồn của video cần đọc (YouTube Studio, mở video, Analytics, Reach, «Traffic source types»; chép cột nguồn, lượt hiển thị, CTR, lượt xem). Với các video để so, cũng cần bảng nguồn của chúng; thiếu thì nhóm nguồn đó ghi «chưa đủ video để so».

## 2.1 Một video chỉ góp một quan sát vào mỗi phép so

Cùng `ma` có nhiều `ngay_do` không phải nhiều video. Trước khi tính, nhóm theo mã video và nguồn, chọn một lần đo có cùng mốc tuổi (48 giờ/7 ngày/30 ngày) với video đích. Không cộng các snapshot tích luỹ; không trộn số 48 giờ của video đích với số cả đời của video cũ. Có nhiều dòng cùng mã/nguồn/mốc thì chọn ngày đo mới nhất trong mốc đó và báo quy tắc đã chọn. Hai dòng cùng ngày nhưng khác số thì hỏi lại, không tự chọn.
Thiếu `ma`, `ngay_do` hoặc không xác định được cửa sổ đo thì ghi chưa đủ dữ liệu so tương đương; có thể trình bày số thô nhưng không gán bệnh từ bội số. Điều kiện đủ mẫu đếm số mã khác nhau sau bước này.

## 3. Ba phép tính, đều qua tệp tạm trong `ho-so-kenh/tam/`

Tạo thư mục `ho-so-kenh/tam/` nếu chưa có. Các tệp tạm giữ lại làm bằng chứng phép tính; đừng xoá.

**Video đích không vào median.** Mức thường là median của các video **khác** video đang đọc. Bội số của video đích = số của nó ÷ median, viết rõ phép chia.

### 3.1 Lượt xem, lượt hiển thị

Tệp `ho-so-kenh/tam/luot-xem.csv` với cột `tieu_de,ngay_dang,luot_xem` (các video khác video đích, dòng tổng):

```bash
python3 references/chung/tinh-median.py ho-so-kenh/tam/luot-xem.csv --ngay-quet <YYYY-MM-DD> --json
```

Cùng cách cho lượt hiển thị: tệp `hien-thi.csv`, cột `luot_xem` điền số hiển thị.

### 3.2 CTR và giữ chân: nhân 100 thành số nguyên

Script đọc cột `luot_xem` là số nguyên và **bỏ dấu chấm, dấu phẩy** (coi là dấu ngăn nghìn). Đưa thẳng `4,27` vào sẽ thành 427 mà không báo lỗi. Vì vậy nhân phần trăm với 100 rồi làm tròn: CTR 4,27% thành `427`. Đọc median xong thì chia lại cho 100.

Tệp `ho-so-kenh/tam/ctr-theo-nguon.csv`, cột `kenh,tieu_de,ngay_dang,luot_xem` với `kenh` là **tên nguồn**; script tự tính median riêng từng nguồn:

```csv
kenh,tieu_de,ngay_dang,luot_xem
de-xuat,Tiêu đề video A,2026-08-01,512
de-xuat,Tiêu đề video B,2026-08-15,447
tim-kiem,Tiêu đề video A,2026-08-01,689
```

Chạy lệnh như mục 3.1. Kết quả vẫn gọi số là «lượt xem»; đó là CTR nhân 100, đọc lại bằng cách chia 100. Mỗi nguồn trong kết quả có `trang_thai` riêng: `ĐÃ TÍNH` hoặc `TỪ CHỐI`. Nguồn bị từ chối ghi «chưa đủ video để so».

Giữ chân 30 giây và % thời lượng xem TB: cùng cách, tệp `giu-chan.csv`, `kenh` đặt là `giu-chan-30s` hoặc `phan-tram-xem`.

### 3.3 Bội số và nhãn đọc

Bội số = số của video ÷ median (làm tròn hai chữ số). Nhãn đọc, mức `[ĐỀ XUẤT]`:

| Bội số | Nhãn |
|---|---|
| dưới 0,8 | thấp rõ |
| từ 0,8 đến 1,2 | trong mức thường |
| trên 1,2 | cao rõ |

Lý lẽ: một video lệch dưới 20% so với median của chính kênh là dao động thường gặp khi mẫu nhỏ, chưa đủ để gọi là lệch. Con số 20% là của người thiết kế bộ, chưa kiểm trên kênh thật; chỉnh được sau khi chạy thử. Khi in ra, luôn in cả **bội số và median**, để người dùng tự đánh giá lại nếu họ thấy mức này quá chặt hoặc quá lỏng.

## 4. Không có Python

Nếu máy không chạy được `python3`: sắp các số theo thứ tự, in cả danh sách ra để người dùng kiểm, lấy giá trị giữa (số chẵn thì trung bình hai giá trị giữa), và ghi rõ «tính tay, chưa qua script». Phép tính tay vẫn phải theo đủ luật: bỏ video dưới 7 ngày, dưới 4 video thì không tính.
