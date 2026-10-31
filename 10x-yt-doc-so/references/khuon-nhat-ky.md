# Khuôn `ho-so-kenh/nhat-ky-thu.md`

Đây là khuôn đầu ra của `10x-yt-doc-so`. Giữ **đúng tên mục và các nhãn mở đầu dòng** (`Bệnh:`, `Biến đổi:`, `Giả thuyết:`, `Đo lại:`…) vì lần đọc số sau, skill `10x-yt-de-tai` và người soát đọc theo đó. Hợp đồng dữ liệu (`references/chung/ho-so-kenh.md`) chỉ khoá tên tệp và chủ tệp; phần thân dưới đây do skill này định nghĩa.

Quy ước dòng nhãn, mỗi nhãn **nằm riêng một dòng** và xuất hiện **đúng một lần** trong một lần đọc số:

| Dòng | Ý nghĩa | Chỉ có khi |
|---|---|---|
| `Bệnh:` | Một trong `gói`, `mở đầu`, `thân`, `phân phối`, `không thấy bệnh rõ so với mức thường của kênh` | Đủ số để kết luận (Chế độ đủ số) |
| `Chưa kết luận:` | Lý do chưa kết luận và cần thêm gì | Thiếu số cho một phần chẩn đoán |
| `Nghi thêm:` | Bệnh phụ nghi ngờ, không phải biến của vòng này | Cây quyết định dòng 2 |
| `Biến đổi:` | **Đúng một** thứ sẽ đổi | Đã qua cổng đủ mẫu; có giả thuyết thử hoặc giữ nguyên để thu thập dữ liệu |
| `Giả thuyết:` | Câu dạng «Nếu đổi X thì Y tăng/giảm, đo bằng Z.» | Cùng lúc với `Biến đổi:` |
| `Đo lại:` | Ngày, mốc, video đo | Cùng lúc với `Biến đổi:` |
| `Kết quả:` | `chưa đo` khi mở vòng, được điền khi đo lại | Luôn có |
| `Cờ:` | Cờ của kênh (tuỳ chọn) | Chỉ khi chạy phần cờ |

Chế độ «chỉ ghi số» (dưới 5 video) **không có** dòng `Bệnh:`, `Biến đổi:`, `Giả thuyết:`, `Đo lại:` và không dùng chữ «chẩn đoán».

Khi đã qua cổng đủ mẫu nhưng `Chưa kết luận:`, theo hai nhánh Bước 6 trong SKILL.md. Nhánh thu thập dữ liệu không mở vòng thử; giả thuyết/ngày chưa có phải ghi chưa lập/chưa chốt, không tự điền.

## 1. Đầu tệp (tạo ở lần đọc số đầu tiên)

````markdown
# Nhật ký thử

Mỗi mục là một lần đọc số. Mỗi vòng chỉ đổi MỘT biến. Mọi thứ dưới đây là giả thuyết cho tới khi đo lại.

Vòng đang mở: <mã video + ngày đo lại> | không có
````

Dòng «Vòng đang mở» ở đầu tệp là nơi `doc-so` và `de-tai` nhìn nhanh. Cập nhật mỗi khi mở hoặc đóng vòng. Mục mới thêm **ngay dưới** dòng này (mới nhất trên cùng); không sửa mục cũ, trừ ô `Kết quả:` của đúng mục đang được đo lại.

## 2. Khuôn một lần đọc số (chế độ đủ số)

````markdown
## <ma> · <tiêu đề video> · đọc ngày <YYYY-MM-DD> · mốc <48 giờ | 7 ngày | 30 ngày>

> Đăng ngày <YYYY-MM-DD>, tuổi <n> ngày lúc đọc. Độ tin: <thấp | trung bình | cao> (theo mốc).

### 1. Mức thường của kênh
- So với: <k> video khác đủ điều kiện (đăng từ 7 ngày trở lên), tính bằng tinh-median.py, ngày quét <YYYY-MM-DD> `[SỐ LIỆU]`
- Video bị bỏ khỏi phép so: <tiêu đề + lý do (dưới 7 ngày, thiếu số, là Short)> | không có

| Chỉ số | Video này | Median kênh (n) | Bội số | Đọc |
|---|---|---|---|---|
| Lượt hiển thị | <số> | <số> (<n>) | <×> | <thấp rõ / trong mức thường / cao rõ / chưa đo> |
| Lượt xem | | | | |
| Giữ chân 30 giây | | | | |
| % thời lượng xem TB | | | | |

### 2. CTR theo từng nguồn view

| Nguồn | % lượt hiển thị của video | CTR video | CTR median kênh (n) | Bội số | Đọc |
|---|---|---|---|---|---|
| Đề xuất | | | | | |
| Tìm kiếm | | | | | |
| Duyệt / Trang chủ | | | | | |
| Bên ngoài | | | | | |
| Khác | | | | | |

CTR tổng (chỉ để tham khảo, không dùng một mình làm căn cứ): <số>.
Cơ cấu nguồn lượt xem: <nguồn: %, …> so với cơ cấu thường của kênh <…> | chưa đủ video để so.
Mục tiêu nguồn view của video: <nguyên lời người dùng `[TRÍCH]`> | chưa đặt mục tiêu nguồn view.

### 3. Đường giữ chân (chỉ khi có)
<bảng ở references/duong-giu-chan.md, mục 4> | chưa có đường giữ chân.

### 4. Kết luận
Bệnh: <gói | mở đầu | thân | phân phối | không thấy bệnh rõ so với mức thường của kênh>
Bằng chứng: <một dòng trỏ đúng con số ở bảng 1 hoặc 2, kèm bội số và median>
Nghi thêm: <mở đầu | thân> | (bỏ dòng này nếu không có)

### 5. Một biến
Biến đổi: <đúng MỘT thứ: tiêu đề | thumbnail | 30 giây đầu | …, nói cụ thể đổi từ gì sang gì> (áp cho <video này | video kế tiếp>)
Giả thuyết: Nếu đổi <X> thì <Y> tăng/giảm, đo bằng <Z>.
Cặp ví dụ: được = «<…>» · không được = «<…>»
Đo lại: <YYYY-MM-DD> · mốc <48 giờ | 7 ngày | 30 ngày> · trên <video nào>
Việc để vòng sau: <các việc khác phát hiện được, không làm bây giờ> | không có

### 6. Kết quả (điền khi đo lại)
Kết quả: chưa đo
````

Hướng dẫn điền:

- «Đọc» dùng đúng ba nhãn: `thấp rõ` (bội số dưới 0,8), `trong mức thường` (0,8 đến 1,2), `cao rõ` (trên 1,2). Hai ngưỡng này là `[ĐỀ XUẤT]` (xem `cach-tinh.md`, mục 3.3). Không có median để so thì ghi «chưa đủ video để so», không ghi nhãn.
- Ô chưa đo ghi «chưa đo», không ghi 0.
- Mọi con số trong mục 1 và 2 mang nhãn `[SỐ LIỆU]` kèm nguồn và ngày ở dòng đầu mục. Phần diễn giải mang `[SUY LUẬN]`.
- Dòng `Bằng chứng:` phải chép một con số có trong bảng ở trên, không phải con số mới.
- Sau dòng `Biến đổi:` không được còn thứ hai. Ý khác để dưới «Việc để vòng sau:».

## 3. Khuôn chế độ «chỉ ghi số» (dưới 5 video)

````markdown
## <ma> · <tiêu đề video> · ghi ngày <YYYY-MM-DD> · mốc <48 giờ | 7 ngày | 30 ngày>

Mới có <n> video đã đăng, chưa đủ 5 để so với mức thường của kênh. Mục này chỉ ghi số, chưa kết luận gì.

| Chỉ số | Video này |
|---|---|
| Lượt hiển thị | <số> |
| Lượt xem | <số> |
| CTR từng nguồn | <Đề xuất: …; Tìm kiếm: …; …> |
| Giữ chân 30 giây | <số> |
| % thời lượng xem TB | <số> |

Chưa kết luận: cần thêm <5 − n> video đã đăng. Khi đủ, đọc số lại từ đầu.
Quay lại: khi đăng thêm video kế tiếp, đọc số lại.
````

Trong chế độ này **không** viết dòng `Bệnh:`, không dùng chữ «chẩn đoán», không viết dòng `Biến đổi:`, không đề nghị sửa gì. Ghi số cũng có ích: số ghi hôm nay là mốc so cho video sau. Dòng `Quay lại:` chỉ là lời nhắc, không phải lời hẹn đo một biến, nên không gắn mốc 48 giờ, 7 ngày, 30 ngày và không dùng nhãn `Đo lại:`.

## 4. Khuôn đóng vòng (chế độ đo lại)

Khi đến ngày đo lại, **không thêm mục mới thay cho mục cũ**. Điền vào ô `Kết quả:` của mục đang mở:

````markdown
Kết quả: đo ngày <YYYY-MM-DD>, mốc <…>, trên <video>
- Trước: <số đo của đúng chỉ số Z ở lần đọc trước, kèm nguồn view nếu là CTR> `[SỐ LIỆU]`
- Sau: <số đo mới của đúng chỉ số Z> `[SỐ LIỆU]`
- Bội số so với median kênh: <trước ×> → <sau ×>
- Số video đã dùng biến này: <k> trên <3 cần cho kết luận `[ĐỀ XUẤT]`>
- Đọc: <giữ biến này | bỏ biến này | thử lại | chưa đủ video để kết luận> `[SUY LUẬN]`
- Vì sao: <một câu trỏ vào hai số trên>
````

Rồi đổi dòng «Vòng đang mở» ở đầu tệp thành `không có` và mới được mở vòng kế tiếp.

## 5. Ví dụ đã điền `[GIẢ LẬP]`

Số dưới đây bịa ra để minh hoạ khuôn. Không dùng làm số tham chiếu cho bất kỳ kênh nào.

````markdown
## 05-ba-loi-khi-nhan-bao-gia · Ba lỗi khiến khách bỏ báo giá của bạn · đọc ngày 2026-11-10 · mốc 7 ngày

> Đăng ngày 2026-11-02, tuổi 8 ngày lúc đọc. Độ tin: trung bình.

### 1. Mức thường của kênh
- So với: 7 video khác đủ điều kiện, tính bằng tinh-median.py, ngày quét 2026-11-10 `[SỐ LIỆU]`
- Video bị bỏ khỏi phép so: không có

| Chỉ số | Video này | Median kênh (n) | Bội số | Đọc |
|---|---|---|---|---|
| Lượt hiển thị | 9.400 | 10.100 (7) | 0,93 | trong mức thường |
| Lượt xem | 310 | 560 (7) | 0,55 | thấp rõ |
| Giữ chân 30 giây | 68% | 66% (7) | 1,03 | trong mức thường |

### 2. CTR theo từng nguồn view

| Nguồn | % lượt hiển thị của video | CTR video | CTR median kênh (n) | Bội số | Đọc |
|---|---|---|---|---|---|
| Đề xuất | 62% | 2,9% | 4,6% (7) | 0,63 | thấp rõ |
| Tìm kiếm | 24% | 4,8% | 5,0% (6) | 0,96 | trong mức thường |
| Duyệt / Trang chủ | 9% | 3,0% | chưa đủ video để so | | ít lượt hiển thị, chỉ ghi số |
| Bên ngoài | 5% | 6,1% | chưa đủ video để so | | ít lượt hiển thị, chỉ ghi số |

### 4. Kết luận
Bệnh: gói
Bằng chứng: CTR nguồn Đề xuất 2,9% so với median kênh 4,6% (n = 7), bội số 0,63, thấp rõ; giữ chân 30 giây 68% so với median 66%, bội số 1,03.

### 5. Một biến
Biến đổi: thumbnail, từ ảnh toàn cảnh bàn làm việc sang ảnh một người cầm tờ báo giá, một dòng chữ (áp cho video này)
Giả thuyết: Nếu đổi thumbnail sang ảnh một người cầm tờ báo giá thì CTR nguồn Đề xuất tăng, đo bằng CTR nguồn Đề xuất sau 7 ngày kể từ ngày đổi so với 2,9% hôm nay.
Cặp ví dụ: được = «CTR nguồn Đề xuất tăng so với 2,9%» · không được = «thumbnail thu hút hơn»
Đo lại: 2026-11-17 · mốc 7 ngày · trên video 05-ba-loi-khi-nhan-bao-gia
Việc để vòng sau: không có

### 6. Kết quả (điền khi đo lại)
Kết quả: chưa đo
````
