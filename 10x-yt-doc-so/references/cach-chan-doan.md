# Cách chẩn đoán: bốn bệnh, mỗi bệnh trỏ đúng một con số

Phần này dùng ở Bước 3 đến Bước 5 của `SKILL.md`. Mọi phép so là **với mức thường của chính kênh** (bội số ÷ median, xem `cach-tinh.md`). Không có ngưỡng CTR hay AVD tuyệt đối nào trong tệp này, và không được thêm vào: ngưỡng cứng đã bị loại (xem `references/chung/da-bi-bac.md`).

## 1. Nền: hai nửa của một lượt xem

Một lượt xem đi qua hai cửa liên tiếp:

1. **Trước khi bấm:** người xem thấy tiêu đề và thumbnail trong một danh sách và quyết định bấm hay không. Số đo: lượt hiển thị và CTR. Cửa này do **gói** (tiêu đề + thumbnail) quyết định, cộng với việc YouTube có đưa video ra danh sách đó hay không.
2. **Sau khi bấm:** người xem ở lại hay thoát. Số đo: giữ chân, thời gian xem, % thời lượng xem. Cửa này do **nội dung** quyết định: mở đầu rồi đến thân.

Hệ quả cho việc chẩn đoán: CTR cao mà giữ chân thấp nghĩa là gói kéo người vào nhưng nội dung không giữ được, và đẩy thêm gói không cứu được video này. CTR thấp mà giữ chân bình thường nghĩa là nội dung ổn nhưng ít người được thuyết phục bấm vào. Hai tình huống này cần hai cách sửa khác nhau, nên phải tách trước khi chọn biến.

Đây là cách đọc để chọn việc sửa. Nó không phải mô tả cách YouTube chấm video, và skill không được khẳng định điều gì về thuật toán (xem `references/chung/da-bi-bac.md`).

## 2. CTR phải đọc theo TỪNG nguồn view

CTR của danh sách đề xuất, của kết quả tìm kiếm và của trang chủ là ba chuyện khác nhau: người xem đang ở trong tâm thế khác, và cùng một video có thể tốt ở nguồn này và kém ở nguồn kia. Một CTR tổng trộn các nguồn lại sẽ thay đổi chỉ vì cơ cấu nguồn đổi, không vì gói đổi.

Quy tắc:

- Luôn in bảng CTR **theo từng nguồn** (Đề xuất, Tìm kiếm, Duyệt/Trang chủ, Bên ngoài, Khác). CTR tổng chỉ in kèm, không dùng một mình làm căn cứ chẩn đoán gói.
- Chỉ **đọc** (gắn nhãn thấp rõ, trong mức thường, cao rõ) những nguồn chiếm từ `[ĐỀ XUẤT] 20%` tổng lượt hiển thị của video trở lên. Lý lẽ: nguồn nhỏ có ít lượt hiển thị nên CTR dao động mạnh; con số 20% chưa kiểm. Nguồn nhỏ hơn thì in số, nhãn «ít lượt hiển thị, chỉ ghi số».
- Median CTR của từng nguồn tính từ **chính các video khác của kênh** ở nguồn đó. Nguồn nào chưa có đủ 4 video để so thì ghi «chưa đủ video để so nguồn này».
- Không có nguồn lớn nào so được ⇒ không kết luận bệnh gói. Ghi «Chưa kết luận:» và nói cần thêm gì (bảng nguồn của vài video khác).

Ngoài CTR, in thêm **cơ cấu nguồn lượt xem** (mỗi nguồn chiếm bao nhiêu phần trăm lượt xem của video, so với cơ cấu thường của kênh nếu đủ dữ liệu). Nếu người dùng đã đặt mục tiêu nguồn view cho video (ví dụ muốn video này sống nhờ tìm kiếm), đối chiếu cơ cấu thực với mục tiêu đó và nói thẳng nó lệch hay khớp. Chưa có mục tiêu thì ghi «chưa đặt mục tiêu nguồn view» và đừng tự đặt hộ.

## 3. Cây quyết định

Đi từ trên xuống, gặp dòng đầu tiên khớp thì dừng. «Nguồn lớn» là nguồn đủ điều kiện đọc ở mục 2. «Giữ chân» là giữ chân 30 giây đầu nếu có, nếu không thì % thời lượng xem trung bình; so với median của cùng chỉ số ở các video khác của kênh. Video dài hơn nhiều hoặc ngắn hơn nhiều so với phần lớn các video còn lại thì nói rõ đây là hạn chế của phép so.

| # | CTR ở nguồn lớn | Giữ chân | Hiển thị | Bệnh | Dòng ghi |
|---|---|---|---|---|---|
| 1 | thấp rõ | trong mức thường hoặc cao rõ | bất kỳ | **gói** | `Bệnh: gói` |
| 2 | thấp rõ | thấp rõ | bất kỳ | **gói** (chính), nghi thêm nội dung | `Bệnh: gói` và `Nghi thêm: mở đầu` hoặc `Nghi thêm: thân` |
| 3 | trong mức thường hoặc cao rõ | thấp rõ, mất người **tập trung ở 30 giây đầu** | bất kỳ | **mở đầu** | `Bệnh: mở đầu` |
| 4 | trong mức thường hoặc cao rõ | thấp rõ, mất người **rải ở giữa hoặc dần dần** | bất kỳ | **thân** | `Bệnh: thân` |
| 5 | trong mức thường hoặc cao rõ | trong mức thường hoặc cao rõ | thấp rõ | **phân phối** | `Bệnh: phân phối` |
| 6 | trong mức thường hoặc cao rõ | trong mức thường hoặc cao rõ | trong mức thường hoặc cao rõ | không thấy bệnh rõ | `Bệnh: không thấy bệnh rõ so với mức thường của kênh` |

Ghi chú từng dòng:

- **Dòng 1** là ca «tiêu đề hoặc thumbnail đang cản». Biến đổi nên là tiêu đề hoặc thumbnail, không đụng kịch bản.
- **Dòng 2**: gói hứa lệch kéo nhầm người vào thì giữ chân cũng thấp theo. Sửa gói trước, đo lại, rồi mới tính chuyện nội dung. Đây là `[SUY LUẬN]`, ghi nhãn.
- **Dòng 3 và 4** cần đường giữ chân (xem `duong-giu-chan.md`) để phân biệt. Có mỗi giữ chân 30 giây hoặc % xem trung bình mà không có đường: ghi `Bệnh: mở đầu` chỉ khi giữ chân 30 giây thấp rõ; không có số giữ chân 30 giây thì ghi `Chưa kết luận:` và xin đường giữ chân. Đừng đoán giữa mở đầu và thân.
- **Dòng 5**: video ít được đưa ra cho người xem dù người thấy thì bấm. Việc sửa nằm ở chỗ video được tìm thấy ở đâu (từ khoá ở tiêu đề và mô tả, mục tiêu nguồn view, đưa link ở nơi người dùng có khán giả), không phải ở gói. Hiển thị còn tăng theo thời gian, nên nếu video dưới 28 ngày thì ghi thêm «độ tin thấp, đo lại ở mốc 30 ngày». Con số 28 ngày là `[ĐỀ XUẤT]`, chưa kiểm.
- **Dòng 6**: được phép. Khi đó MỘT biến vẫn phải chọn, hoặc ghi «giữ nguyên» (xem `SKILL.md`, Bước 6).
- Giữ chân thấp mà **không có** CTR theo nguồn: không rơi vào dòng nào. Ghi `Chưa kết luận:`, nói thiếu bảng nguồn.

Mỗi dòng bệnh phải kèm **một dòng bằng chứng trỏ đúng con số**, ví dụ: «CTR nguồn Đề xuất 3,10% so với median kênh 4,60% (n = 7), bội số 0,67, thấp rõ». Bệnh không trỏ được con số nào thì không được ghi.

## 4. Bản đồ bốn góc của kênh (tuỳ chọn, khi kênh có từ 8 video)

Đặt các video khác của kênh lên hai trục, cả hai theo bội số so với median của chính kênh: **lượt xem** và **giữ chân**. Bốn góc, đặt tên theo việc cần làm:

| Lượt xem | Giữ chân | Tên góc | Ý nghĩa cho vòng sau |
|---|---|---|---|
| cao rõ | cao rõ | Chạy tốt cả hai | Học khuôn của nó; đừng sửa |
| cao rõ | thấp rõ | Nhiều người vào, ở không lâu | Gói đang làm tốt hơn nội dung |
| thấp rõ | cao rõ | Ít người vào, ở lâu | Nội dung tốt hơn gói hoặc phân phối |
| thấp rõ | thấp rõ | Cả hai thấp | Xem lại đề tài, không chỉ gói |

Dùng bản đồ để đặt video đang đọc vào hàng xóm của nó, không để chấm điểm. Video nằm ngoài bốn góc (trong mức thường ở một trục) thì ghi «ở giữa». Không đủ 8 video thì bỏ bước này.

## 5. Mốc đọc: 48 giờ, 7 ngày, 30 ngày `[ĐỀ XUẤT]`

Chọn mốc theo tuổi video lúc đọc số (từ ngày đăng đến ngày đọc): dưới 7 ngày là mốc 48 giờ, từ 7 đến dưới 30 ngày là mốc 7 ngày, từ 30 ngày trở lên là mốc 30 ngày. Lý lẽ cho ba mốc: ba lần nhìn đủ để thấy tín hiệu đầu, tín hiệu ổn định và kết quả dài hạn, và khớp bộ ba mốc của các skill đọc số cũ của 10X. Cả ba mốc chưa kiểm trên kênh chuyên gia.

| Mốc | Đọc gì | Độ tin |
|---|---|---|
| 48 giờ | CTR theo nguồn, hiển thị, giữ chân 30 giây | Thấp. Số còn leo; chỉ chẩn đoán gói và mở đầu, đo lại ở 7 ngày |
| 7 ngày | Thêm cơ cấu nguồn lượt xem, % thời lượng xem, đường giữ chân | Trung bình. Mốc chính để chọn biến |
| 30 ngày | Thêm nguồn tìm kiếm, tăng đăng ký từ video, video có sống tiếp không | Cao hơn. Mốc để kết luận phân phối và đóng vòng |

Ngày đo lại của vòng mới đặt ở **mốc kế tiếp** của video bị đổi (hoặc của video kế tiếp nếu biến đổi chỉ áp được cho video sau, ví dụ sửa 30 giây đầu của kịch bản).

## 6. Năm cờ của kênh (tuỳ chọn, chỉ khi người dùng hỏi sức khoẻ cả kênh hoặc cuối tháng)

Cờ là câu hỏi «có lệch so với chính kênh không», không phải điểm. Mỗi cờ có tên, con số kích hoạt so với lịch sử của chính kênh, và việc kế tiếp phải **cụ thể**, không được là «cải thiện CTR».

| Cờ | Kích hoạt khi | Việc kế tiếp (ví dụ về độ cụ thể) |
|---|---|---|
| Cờ gói | Median CTR 3 video gần nhất thấp rõ so với median CTR các video trước đó của kênh | «Thử 2 kiểu thumbnail khác nhau cho 2 video kế tiếp», không phải «làm thumbnail đẹp hơn» |
| Cờ nội dung | Median giữ chân 3 video gần nhất thấp rõ so với các video trước | «Cắt phần giới thiệu bản thân khỏi 30 giây đầu của video kế» |
| Cờ khán giả | Số người huỷ đăng ký lớn hơn số người đăng ký mới trong kỳ đang xét | «Đọc 20 bình luận mới nhất của video mất người, ghi lại điều họ kỳ vọng» |
| Cờ một nguồn | Một nguồn chiếm `[ĐỀ XUẤT] 80%` lượt xem của kênh trở lên. Lý lẽ: con số này lấy từ skill đọc số cũ của 10X, chưa kiểm | «Chọn một đề tài hợp nguồn còn lại, ghi mục tiêu nguồn view trước khi đăng» |
| Cờ nhịp | Khoảng cách từ video mới nhất đến hôm nay lớn hơn 2 lần khoảng cách median giữa các lần đăng của chính kênh (con số 2 lần là `[ĐỀ XUẤT]`) | «Chốt ngày quay cho đề tài treo đầu tiên» |

Cờ nằm ở phần riêng của đầu ra, dòng bắt đầu bằng `Cờ:`. **Cờ không phải là biến đổi.** Không gộp cờ vào dòng `Biến đổi:`; việc cờ chỉ ra là việc để vòng sau.
