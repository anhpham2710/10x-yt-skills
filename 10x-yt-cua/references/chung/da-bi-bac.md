# Đã bị bác: con số và luật đã kiểm rồi loại

Tệp này liệt kê những con số, quy tắc đã được xem xét khi thiết kế bộ skill và **bị loại**, kèm lý do. Mục đích: để người viết skill về sau (và model khi chạy skill) không chép lại chúng từ trí nhớ hoặc từ một tài liệu khác. Gặp một khẳng định giống mục nào dưới đây thì coi là `[CẦN NGUỒN]` (xem `nhan-nguon.md`) trừ khi người dùng đưa nguồn kiểm được.

Quy tắc chung: **một con số về hành vi thuật toán YouTube, lượt tìm, thị phần, hoặc ngưỡng chỉ số không kèm nguồn kiểm được (đường dẫn, ngày, phép đo) thì không được dùng làm cơ sở quyết định.**

## 1. Con số và khẳng định đã loại

| Điều bị bác | Vì sao loại | Dùng thay bằng |
|---|---|---|
| «Mỗi video cần 15–20 thẻ (tag)», kể cả tên thương hiệu và từ khoá đơn lẻ | Thẻ là tín hiệu phụ; nhồi thẻ không có cơ sở. Chính tài liệu khuyên điều này cũng tự ghi thẻ là tín hiệu phụ nên tự mâu thuẫn | Số thẻ ít, dùng để phân biệt cách viết/chính tả của từ khoá chính. `[ĐỀ XUẤT] 6–12` thẻ, coi là mục phụ, chốt ở skill đăng video |
| «CTR 6%+ là tốt» (hoặc bất kỳ ngưỡng CTR cứng nào) | Ba tài liệu nội bộ cũ đưa ba ngưỡng CTR/AVD khác nhau cho cùng một việc; CTR tốt phụ thuộc loại video, nguồn lượt xem và tuổi kênh | So CTR của video với **median CTR của chính kênh** (khi đủ video), không so ngưỡng tuyệt đối |
| «Tìm kiếm chỉ chiếm sáu phần trăm lượt xem» | Một câu trong gói lệnh cũ, không ghi nguồn. Tỉ lệ nguồn lượt xem khác nhau theo kênh | Người dùng xem báo cáo nguồn lượt xem **của chính kênh** trong YouTube Studio |
| «Lượt tìm trên YouTube = 3–8 lần lượt tìm trên Google» | Nguồn ghi là «nghiên cứu từ khoá của kênh bạn, tháng 3/2026», không phải phép đo kiểm được | Gõ vào ô tìm kiếm YouTube, đọc gợi ý, quan sát lượt xem của các video đầu trang kết quả; ghi `[SỐ LIỆU]` kèm ngày |
| Điểm từ khoá 0–100 của công cụ bên thứ ba đọc thành «số lượt tìm» | Đó là điểm tương đối, không phải số lượt tìm | Chỉ dùng để so hai cụm với nhau, ghi rõ «điểm, không phải lượt tìm» |
| «Gợi ý (Suggested) mang lại gấp 3 lần…», «video quá 2 năm mất khoảng 40% hiển thị tìm kiếm», «Shorts đạt đỉnh sau 28–30 ngày», «ngắt mạch giảm rớt 40%», «đăng 2–3 lần mỗi tuần tăng người đăng ký nhanh gấp 4», «hook quá 60 giây mất 35% người xem» | Cả nhóm trình bày như số liệu chính thức nhưng không dẫn nguồn kiểm được | Bỏ hẳn. Muốn biết thì đọc từ số liệu của kênh (YouTube Studio) và đo lại bằng nhật ký thử |
| Điểm hook chấm bằng biểu thức chính quy rồi hiện thành «mạnh / dùng được / yếu» (ngưỡng 72/55) | Tự thừa nhận không đo được CTR nhưng dễ bị người dùng tin như số đo; ngưỡng không nguồn; biểu thức cắt hỏng dấu tiếng Việt | Chấm hook bằng câu hỏi có đáp án rõ (hook có trả đúng lời hứa của tiêu đề trong ~20 giây đầu không), không cho điểm số |
| Số liệu quy mô của một nền tảng («75 triệu+ người dùng…») chép từ bản nháp | Không nguồn, không ngày | Không dùng số quy mô nền tảng làm cơ sở. Nếu cần, người dùng đưa nguồn |
| Bảng RPM/AdSense theo ngách | Lệch hướng sản phẩm: kênh của chuyên gia kiếm tiền từ khách hàng của mình, không phải từ AdSense; số cũng không có nguồn | Câu hỏi «người xem này có phải khách của tôi không» ở skill chốt ngách |
| «Ngưỡng 3× median là outlier» hay «5×/2×/1,5×» coi như quy luật | Đây là ngưỡng do mỗi công cụ tự chọn, không phải sự thật về YouTube | Ghi là `[ĐỀ XUẤT]`, nêu ngưỡng đã dùng và lý do trong `video-thang.md`, cho người dùng chỉnh |
| Tính median nhẩm trong đầu model | Model tính nhẩm median từ vài chục số dễ sai và sai im lặng | `tinh-median.py` |
| Median của dưới 4 video | Không đủ để gọi là median | `tinh-median.py` từ chối; skill nói «kênh này chưa đủ video để so» |
| So lượt xem tuyệt đối giữa kênh lớn và kênh nhỏ | 100.000 lượt xem ở kênh 2 triệu người đăng ký và ở kênh 2.000 người đăng ký là hai chuyện khác nhau | Bội số so với median của **chính kênh đó** |
| Video đăng chưa đủ 7 ngày đưa vào so sánh | Lượt xem còn đang leo | Loại khỏi median và bội số (`tinh-median.py` làm sẵn) |

## 2. Cách thêm một mục mới

Khi một skill phát hiện con số hay luật sai (hoặc không kiểm được) mà bản trước đã dùng:

1. Thêm một dòng vào bảng trên: điều bị bác, vì sao, dùng thay bằng gì.
2. Sửa chỗ đã chép nó ở skill (grep tên con số trong thư mục `skills/10x-yt-*`).
3. Chạy `dong-bo.sh` để bản chép trong các skill con khớp với bản gốc (xem `README.md`).

## 3. Nguồn gốc

Danh sách được tổng hợp trong quá trình mổ xẻ 57 skill YouTube của giai đoạn 1 (tài liệu thiết kế nội bộ của 10X). Các khẳng định bị bác được nêu để đối chiếu; không có câu chữ nào chép lại từ tài liệu nguồn. Xem `NGUON.md`.
