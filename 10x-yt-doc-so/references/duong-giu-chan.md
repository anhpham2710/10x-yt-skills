# Chế độ đường cong: nối từng điểm tụt với đoạn kịch bản

Dùng khi người dùng đưa **đường giữ chân** của một video (tỉ lệ người còn xem theo thời gian) và muốn biết người xem rời đi ở đâu và vì sao. Đây là phần đào sâu của bệnh «mở đầu» và «thân» ở `cach-chan-doan.md`.

## 1. Đầu vào

| Cần | Nguồn | Thiếu thì |
|---|---|---|
| Các điểm của đường: giây và phần trăm còn xem, ví dụ `0:00 = 100%, 0:15 = 82%, 0:30 = 71%` | Người dùng gõ các điểm đọc từ YouTube Studio (video, Analytics, Engagement, «Audience retention»), hoặc gửi ảnh chụp đường | Dừng chế độ này, nói cần gì. Không vẽ đường từ trí nhớ hay từ giữ chân trung bình |
| Thời lượng video | Người dùng | Hỏi một câu |
| Lời nói của video **có mốc thời gian** | Người dùng dán bản chép lời (`references/chung/lay-chu.md`, bước 1 và 2) hoặc kịch bản ghi theo giây | Không nối được điểm tụt với câu cụ thể. Vẫn đọc được đường, nhưng ghi «chưa nối với lời nói» và xin dán bản chép lời |

Nếu người dùng đưa **ảnh** đường giữ chân: đọc các điểm từ ảnh, in lại bảng điểm đã đọc và ghi «đọc từ ảnh, xấp xỉ». Hỏi người dùng xác nhận các điểm tụt chính trước khi dựa vào chúng. Không bịa điểm mà ảnh không thấy rõ.

Bản chép lời hay sai tên riêng và thuật ngữ (xem `lay-chu.md`, mục 3). Khi trích một câu làm bằng chứng thì nói rõ để người dùng soát lại những chữ đó.

## 2. Thế nào là «điểm tụt»: so với chính đường cong, không so ngưỡng tuyệt đối

Không có «tụt hơn bao nhiêu phần trăm thì xấu». Đường giữ chân nào cũng đi xuống, và độ dốc phụ thuộc loại video, độ dài và nguồn người xem. Cách đọc:

1. Chia video thành các đoạn bằng nhau, mỗi đoạn `[ĐỀ XUẤT] 30 giây`. Lý lẽ: đủ ngắn để nối với vài câu nói, đủ dài để không đọc nhiễu của từng giây.
2. Tính **mức giảm trung bình mỗi đoạn** của chính video này (điểm đầu trừ điểm cuối, chia số đoạn).
3. Một đoạn là **điểm tụt** khi mức giảm của nó lớn hơn `[ĐỀ XUẤT] 2 lần` mức giảm trung bình mỗi đoạn của chính video. Lý lẽ: đoạn nào mất người nhanh gấp đôi nhịp thường của video là đoạn đáng xem lại; con số 2 chưa kiểm.
4. Một đoạn là **điểm giữ** khi đường đi ngang hoặc nhích lên (người xem tua lại hoặc xem lại).

Nếu `so-video.csv` có giữ chân 30 giây của các video khác (cột `giu_chan_30s`) thì so thêm: giữ chân 30 giây của video này so với median của kênh (bội số, `cach-tinh.md` mục 3.2). Đây là phép so giữa các video, bổ sung cho phép so trong một video.

## 3. Ba kiểu vấn đề

| Kiểu | Dấu hiệu trên đường | Hướng nghĩ về nguyên nhân (là giả thuyết, cần nối với lời nói) |
|---|---|---|
| **Rò ở mở đầu** | Đoạn 0–30 giây là điểm tụt, hoặc mức giảm của nó lớn hơn `[ĐỀ XUẤT] 2 lần` mức giảm trung bình các đoạn còn lại | Lời mở không trả lời điều tiêu đề và thumbnail hứa; mở bằng giới thiệu bản thân hay lời chào dài; hứa xong lại trì hoãn |
| **Vách ở giữa** | Một đoạn riêng lẻ ở giữa hoặc cuối là điểm tụt, các đoạn xung quanh bình thường | Đoạn đó lạc đề, quá dài, đổi nhịp, hoặc báo hiệu «sắp hết ý chính» |
| **Dốc đều** | Không có điểm tụt riêng, nhưng cả đường dốc hơn mức thường của kênh | Nhịp chậm cả bài, thiếu lý do để xem tiếp, thiếu thay đổi cảnh hoặc ví dụ |

Nếu mở đầu **khoẻ** (đoạn 0–30 giây không phải điểm tụt) mà cả đường dốc đều thì cân nhắc lỗi nằm ở gói: người xem vào với kỳ vọng khác với thứ video đưa ra. Ghi là `[SUY LUẬN]`, kèm câu hỏi kiểm: nội dung video có khớp với điều tiêu đề hứa không (xem lại `goi/<ma>.md` nếu có).

Đoạn cuối: người xem rời đi ở những giây cuối là bình thường và không tự nó là bệnh. Chỉ gọi là vấn đề khi cuối video đi ngay sau phần giá trị chính và đoạn đó lại kéo dài (lời cảm ơn, nhắc đăng ký dài).

## 4. Nối điểm tụt với lời nói

Với mỗi điểm tụt (tối đa `[ĐỀ XUẤT] 3` điểm quan trọng nhất, để người dùng làm được; lý lẽ: một lần sửa một biến, không cần liệt kê tất cả):

1. Tìm trong bản chép lời các câu rơi vào **đoạn tụt** (và 10 giây ngay trước đoạn đó, vì người xem quyết định rời đi sau khi nghe, không phải trong lúc).
2. Trích **nguyên văn** hai đến ba câu, đặt trong dấu ngoặc kép, nhãn `[TRÍCH]`, kèm mốc giây.
3. Nêu **giả thuyết nguyên nhân** gắn nhãn `[SUY LUẬN]`, nói tại sao câu đó có thể làm người xem rời đi. Đừng khẳng định.
4. Nêu **một cách sửa nhỏ** để thử ở video kế (cắt, đảo thứ tự, thay mở đầu). Chỉ một trong các cách này sẽ trở thành «Biến đổi:» của vòng này; số còn lại ghi là việc để vòng sau.

Bảng đầu ra:

| Đoạn (giây) | Còn xem | Mức giảm so với trung bình | Kiểu | Câu trong đoạn `[TRÍCH]` | Giả thuyết `[SUY LUẬN]` |
|---|---|---|---|---|---|

Thiếu mốc thời gian trong bản chép lời thì cột `[TRÍCH]` ghi «chưa nối: bản chép lời không có mốc giây». Không đoán câu nào nằm ở giây nào bằng cách chia đều chữ theo thời lượng.

## 5. Một cặp ví dụ cho giả thuyết kiểm được

Mỗi đề xuất sửa kèm cặp ví dụ để biết thế nào là «được» và «không được», để sau này đo lại không cãi nhau:

| Được (kiểm được) | Không được (quá mờ) |
|---|---|
| «Cắt 20 giây giới thiệu bản thân khỏi mở đầu, vào thẳng câu trả lời; giữ chân 30 giây của video kế sẽ cao hơn median kênh» | «Mở đầu hay hơn» |
| «Đổi thumbnail sang ảnh một người, một chữ; CTR nguồn Đề xuất của video này sẽ tăng so với trước khi đổi» | «Thumbnail bắt mắt hơn» |
