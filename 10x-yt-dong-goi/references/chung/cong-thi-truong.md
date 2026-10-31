# Cổng thị trường–ngôn ngữ (bước 0 của mọi phân tích)

Trước khi skill nào trong bộ chạy phân tích, nghiên cứu hay sinh nội dung, thị trường, ngôn ngữ và định dạng của kênh phải được chốt và ghi trong `kenh.md`. Lý do: đã từng có lần nghiên cứu chạy trên dữ liệu mặc định của thị trường toàn cầu tiếng Anh rồi xuất tiêu đề tiếng Việt. Bằng chứng cầu của thị trường này bị gắn vào đề xuất nội dung cho thị trường khác, và người dùng tin vào số liệu sai ngữ cảnh.

## 1. Ba điều phải chốt

| Điều | Giá trị hợp lệ | Ghi ở |
|---|---|---|
| Thị trường mục tiêu | `VN`, hoặc một thị trường khác người dùng nêu tên | `kenh.md` dòng `thi-truong` |
| Ngôn ngữ video và tiêu đề | `vi`, `en`, … | `kenh.md` dòng `ngon-ngu` |
| Định dạng | `dai` (video dài), `short`, `ca-hai` (nói rõ cái nào trước) | `kenh.md` dòng `dinh-dang` |

## 2. Cách chạy cổng

1. Đọc `kenh.md`. Cả ba dòng đã có giá trị rõ ràng ⇒ cổng mở, đọc lại cho người dùng nghe một câu để chắc («kênh nhắm người xem Việt Nam, nội dung tiếng Việt, video dài»), rồi chạy tiếp.
2. Thiếu bất kỳ dòng nào ⇒ **hỏi, không đoán.** Hỏi từng điều một, câu hỏi ngắn: «Bạn nhắm người xem ở nước nào?»; «Video và tiêu đề viết bằng tiếng gì?»; «Làm video dài, Short hay cả hai?».
3. **Thị trường và ngôn ngữ không được suy luận từ ngữ cảnh.** Người dùng viết tiếng Việt không có nghĩa là kênh nhắm người xem Việt Nam (có người dạy tiếng Anh cho người nước ngoài, có người làm kênh song ngữ). Chỉ chuyên môn và sở thích mới được suy luận (nêu giả định để người dùng chỉnh); thị trường và ngôn ngữ thì luôn hỏi.
4. Ghi ba giá trị vào `kenh.md`, đổi dòng `thi-truong` trong `TIEN-DO` thành `xong`.

## 3. Cổng chặn lệch thị trường–ngôn ngữ

Chạy lại cổng này TRƯỚC khi xuất bất kỳ kết quả nào có dùng dữ liệu cầu hoặc dữ liệu đối thủ.

| Kiểm | Lệch khi | Làm gì |
|---|---|---|
| Dữ liệu cầu (cụm tìm kiếm, số người dùng đọc từ ô tìm kiếm) | Lấy từ thị trường hoặc ngôn ngữ khác `kenh.md` | **Dừng, không xuất.** Hỏi lại người dùng lấy đúng thị trường, hoặc ghi rõ «số này của thị trường X, không dùng làm bằng chứng cầu cho kênh này» |
| Kênh đối thủ | Khán giả chính ở thị trường khác | Vẫn mổ được cho học cách làm, nhưng không dùng số của họ làm bằng chứng cầu; gắn `[SUY LUẬN]` |
| Tiêu đề, thumbnail, kịch bản đề xuất | Ngôn ngữ khác `ngon-ngu` | Viết lại đúng ngôn ngữ, hoặc dừng và hỏi |
| Định dạng đề xuất | Khác `dinh-dang` (ví dụ ra kịch bản video dài cho kênh chỉ làm Short) | Hỏi lại có mở rộng định dạng không |

Khi cổng chặn: nói thẳng lệch ở đâu bằng một câu («số này lấy từ ô tìm kiếm tiếng Anh, còn kênh bạn nhắm người xem Việt Nam»), chỉ cách sửa, không xuất bản nháp «tạm».

## 4. Khi đổi thị trường hoặc ngôn ngữ giữa chừng

Người dùng đổi `thi-truong` hoặc `ngon-ngu` sau khi đã có `ngach.md`, `video-thang.md`, `de-tai.md`: nói rõ các tệp đó dựa trên thị trường cũ và liệt kê tệp nào cần làm lại. Không tự sửa số trong các tệp đó. Ghi thay đổi vào `kenh.md` kèm ngày.

## 5. Nguồn gốc

Ý «chốt thị trường–ngôn ngữ trước mọi research, và chặn khi bằng chứng lệch thị trường» lấy từ khối Confirm Gate của skill `10x-youtube-niche-idea-vn` (tài sản nội bộ của 10X, header MIT), viết lại cho cả bộ. Xem `NGUON.md`.
