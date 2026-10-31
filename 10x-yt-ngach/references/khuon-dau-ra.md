# Khuôn đầu ra của 10x-yt-ngach

Đọc khi vào bước 8 (ghi tệp) hoặc khi phải dừng. Luật và thứ tự bước nằm ở `SKILL.md`.

### `ho-so-kenh/ngach.md`

````markdown
# Ngách của kênh <tên kênh>

thi-truong: <chép từ kenh.md> · ngon-ngu: <chép từ kenh.md>
Mục tiêu kênh: <xây thương hiệu cá nhân | bán sản phẩm hay dịch vụ | nuôi cộng đồng | chia sẻ quá trình học hay làm | chữ của người dùng> · Nền: <chuyện thật / nghề / sản phẩm, chữ của người dùng; trống nếu chưa có>
Mọi thứ trong tệp này là giả thuyết cho tới khi video đăng và có số đo.

## Ứng viên
| # | Ứng viên | Truy về lời người dùng | Trạng thái |
|---|---|---|---|
| ƯV-A | <ngách bằng chữ người xem gõ> | «<câu nguyên văn của họ>» | được chọn |
| ƯV-B | … | «…» | để dành |
| ƯV-C | … | «…» | để dành |

Ngách chốt: ƯV-A · <tên ngách> · <câu định vị một dòng: ai · giúp việc gì · khác chỗ nào>

## Bảng cầu
Ngày tra: <ngày đọc theo từng nguồn>
Nguồn: số YouTube gốc do người dùng tự đọc hoặc máy đọc trên Chrome khi họ đồng ý. Skill không ước, không tính lại trong bảng này; phép chia duy nhất của skill nằm ở mục «Video lệch» bên dưới.

| Cụm tìm kiếm | Của | Ngày đọc | Gợi ý hiện khi gõ | Từng kết quả đầu: loại · kênh · người đăng ký · lượt xem · đăng | Nguồn | Ảnh bằng chứng |
|---|---|---|---|---|---|---|
| <cụm> | ƯV-A | <ngày> | <gợi ý chép nguyên, hoặc «không có gợi ý», hoặc «chưa đọc»> | `[SỐ LIỆU]` <kênh> · <số> · <số> · <thời điểm> ; <kết quả kế, giữ cả danh sách phát / Short / quảng cáo> … | <số do máy đọc trên Chrome của bạn, ngày YYYY-MM-DD hoặc người dùng tự đọc, ngày YYYY-MM-DD> | <đường dẫn ảnh goi-y và ket-qua; ảnh không lưu được thì ghi rõ từng ảnh> |

## Video lệch
**Không gọi tỷ lệ lượt xem/người đăng ký là outlier.** Số đăng ký hiện tại không phải mức xem thường của kênh, tỷ lệ này không chứng minh cầu hay cơ hội thị trường. Muốn xác định outlier, chuyển `10x-yt-video-thang` với mẫu video trung lập và median của chính kênh.

Phép tính duy nhất của skill này: chia lượt xem cho số người đăng ký của chính video đó, bằng hai số đọc từ nguồn trong bảng cầu. Kênh nhỏ mà video có lượt xem gấp nhiều lần số người đăng ký là một quan sát để kiểm tra thêm; không dùng riêng tỷ lệ này để cho cổng CẦU đạt hay kết luận ngách sẽ thắng.
- <kênh> · <lượt xem> ÷ <người đăng ký> ≈ <N> lần · cụm «<cụm>» `[SUY LUẬN]`

## Lời hứa của ngách
Lời hứa với người xem: <một câu: xem xong người xem được gì; không số kết quả, không hứa quá chứng cứ>
Trả được trong video: <CÓ — «<câu nguyên văn của CHÍNH HỌ trong câu trả lời họ đưa, cho thấy họ làm được hoặc đã làm>» | CHƯA — thiếu gì, cần hỏi họ gì>

## Verdict từng cổng (ngách được chọn)
| Cổng | Kết quả | Căn cứ |
|---|---|---|
| FIT | PASS hoặc FAIL | <câu họ trả lời (a) (b) (c), (c) dẫn dòng bảng cầu> |
| CẦU | PASS hoặc FAIL | <dòng bảng cầu> |
| THỊ TRƯỜNG | PASS hoặc FAIL | <tín hiệu loại nào, dòng bảng cầu nào; hoặc «không dính tín hiệu loại nào»> |
| NỐI | PASS hoặc FAIL | <căn cứ (a) chuyện thật ở câu 2, (b) người cụ thể ở câu 1, hoặc (c) tên sản phẩm; chép nguyên văn> |
| ĐỊNH VỊ | PASS hoặc FAIL | <câu định vị và câu trả lời «ai khác nói được»> |

Tín hiệu loại ngách: <không | có: nêu rõ>
Ai khác nói được câu định vị này? <tên kênh có thật + khác ở đâu | «chưa thấy kênh nào trong bảng nói được» `[SUY LUẬN]`>
VERDICT: GO hoặc NO-GO · <lý do một câu, chỉ vào cổng quyết định>

## Giới hạn của số này
- Ô tìm kiếm chỉ cho thấy cầu **tìm kiếm**. Nguồn lượt xem khác (đề xuất, duyệt trang chủ) chưa đo ở bước này; `10x-yt-dang` và `10x-yt-doc-so` đo tiếp khi có video thật.
- <Chỗ nào còn «chưa đọc» hoặc `[CẦN NGUỒN]`, và tra ở đâu.>
````

Quy ước định dạng, vì `ngach.md` được máy đọc lại để kiểm:

- **Từ «chốt» chỉ xuất hiện đúng một lần**, ở dòng `Ngách chốt:`. Ở chỗ khác dùng «được chọn», «để dành», «loại».
- Có **3 đến 5 dòng ứng viên** (dòng bắt đầu `| ƯV-`). Ứng viên gắn nhãn bằng **chữ cái**, không dùng số.
- **Bảng cầu không có số thứ tự và không có số nào ngoài số YouTube gốc người dùng đã đưa hoặc máy đọc trên Chrome có nguồn**, chép đúng từng chữ. Cột «Của» dùng nhãn chữ cái.
- Cột kết quả của năm cổng chỉ có **PASS** hoặc **FAIL**. Không có tổng điểm, thang điểm, xếp hạng, phần trăm cho ngách.
- Khi có số ngưỡng trong lời giải thích (một năm, 100.000) thì viết **bằng chữ** hoặc nằm trong phần ghi chú của skill, không đưa vào bảng cầu.
- **Mục «Video lệch»**: 1 đến 3 dòng, mỗi dòng đúng dạng `<kênh> · <lượt xem> ÷ <người đăng ký> ≈ <N> lần · cụm «<cụm>» [SUY LUẬN]`. Chỉ lấy video mà **cả hai số là số thường** trong bảng cầu (dạng `346.000` hoặc `801`), chép đúng từng chữ; số viết tắt (`41 N`, `1,2 Tr`) hoặc «chưa đọc» thì bỏ qua, không quy đổi. `<N>` làm tròn đến một chữ số thập phân (dấu phẩy), chia hai lần cho chắc. Chọn tối đa 3 video có `<N>` lớn nhất trong các cụm của ngách được chọn. Không video nào đủ hai số thì ghi một dòng «Không có video nào đủ hai số để chia.» Không đặt ngưỡng «lệch là từ bao nhiêu lần»; ngưỡng chưa có số đo thật `[ĐỀ XUẤT]` để sau khi có video đăng. Dòng giải thích phía trên không được chứa dấu ÷.
- **Mục «Lời hứa của ngách»** đúng hai dòng. «Lời hứa với người xem» không chứa số nào ngoài số có trong dữ liệu họ đưa. «Trả được trong video» mở bằng `CÓ` (kèm một câu «…» nguyên văn **của chính họ**; tên video hay chữ của kênh khác trong bảng cầu không tính) hoặc `CHƯA` (nói thiếu gì). Đây không phải cổng thứ sáu và không đổi VERDICT: `CHƯA` thì ghi vào «Còn thiếu» và dặn không đặt tiêu đề hứa điều đó cho tới khi `10x-yt-dong-goi` kiểm lời hứa.

### `ho-so-kenh/nguoi-xem.md` (bản đầu)

````markdown
# Người xem của kênh <tên kênh> (bản đầu)

Mẫu: <n người hoặc khách người dùng kể; 1 là chính họ hoặc một người họ nghĩ tới> · độ tin: thấp (bản đầu, từ lời người dùng)

## Lớp 1. Họ là ai
- `[TRÍCH]` «<chữ người dùng kể ở câu 1, cộng khách thật nếu có>» hoặc `[SUY LUẬN]` <điều rút ra> (từ <nguồn>)

## Lớp 2. Họ đang tìm gì (chữ họ gõ vào ô tìm kiếm)
- `[SỐ LIỆU]` <cụm> (từ bảng cầu trong ngach.md, đọc ngày <ngày>)

## Lớp 3. Họ kẹt ở đâu
- `[TRÍCH]` hoặc `[SUY LUẬN]` …

## Lớp 4. Họ nói gì (nguyên văn người thật)
- `[TRÍCH]` «<câu nguyên văn>» · nguồn: <khách nói với bạn, bạn kể lại, ngày …>
hoặc đúng một dòng: chưa có, cần `10x-yt-dao-binh-luan`
````

### Khi dừng (⛔)

Khi một cổng dừng chặn, đầu ra **chỉ có** khối dưới đây. Không có `ngach.md`, không có dòng «Ngách chốt», không có bảng cầu, không có verdict.

```
⛔ DỪNG: thiếu <tên dữ liệu thiếu, một câu>.
Vì sao dừng: <một câu, ví dụ «chưa đủ số cầu đọc từ YouTube; mình không đoán số thay bạn»>
Cần tra: <các cụm cần đọc, theo từng ứng viên, nếu đã có ứng viên>
Cách tra: <đúng các bước ở references/phieu-do-cau.md, tóm trong 3 dòng>
Khi có số, quay lại và dán vào, mình làm tiếp từ bước 4.
```

Cổng dừng 4 (lời nhờ nêu thị trường khác `kenh.md`) dùng cùng khuôn nhưng dòng đầu là «⛔ DỪNG: yêu cầu nói thị trường <X>, còn kenh.md ghi <Y>.», dòng «Cần tra» đổi thành câu hỏi «đổi kenh.md sang <X>, hay giữ <Y> và bỏ yêu cầu này?», và **không** có dòng nào mang số hay khung của <X>.


## Cổng tự kiểm trước khi ghi tệp

Trước khi ghi `ngach.md`, tự kiểm từng dòng. Dòng nào đỏ thì sửa hoặc dừng, không ghi:

1. [ ] Có **đúng một** dòng `Ngách chốt:` và **từ 3 đến 5** dòng ứng viên.
2. [ ] **Mọi số trong bảng cầu** là số YouTube gốc người dùng đã đưa hoặc máy đọc trên Chrome có nguồn, chép đúng từng chữ. Số nào bạn không tìm thấy nguyên văn trong nguồn đã ghi của bảng cầu thì xoá và ghi «chưa đọc».
3. [ ] Cả năm cổng đều có **PASS hoặc FAIL** kèm căn cứ trích được. Không có tổng điểm, không có điểm bù.
4. [ ] Tín hiệu loại ngách đã được xét và ghi kết quả (không, hoặc có kèm lý do), kể cả khi mọi cổng khác PASS.
5. [ ] Câu «ai khác nói được câu định vị này?» có câu trả lời cụ thể, tên kênh lấy từ dữ liệu.
6. [ ] `nguoi-xem.md` lớp 4 có câu `[TRÍCH]` nguyên văn, hoặc đúng dòng «chưa có, cần `10x-yt-dao-binh-luan`».
7. [ ] Không có số hay tên (kênh, người, công cụ) bạn nhớ từ huấn luyện thay vì đọc trong dữ liệu của họ.
8. [ ] Họ đã nghe đọc lại và gật.
9. [ ] Mục «Video lệch»: mỗi dòng có hai số **có nguyên văn** trong nguồn đã ghi của bảng cầu, và phép chia đã làm lại lần hai cho ra cùng `<N>`.
10. [ ] Mục «Lời hứa của ngách» có đúng hai dòng; `CÓ` kèm câu nguyên văn, `CHƯA` nói thiếu gì; không số lạ.

## Đầu ra gửi người dùng

Sau khi ghi tệp, trả về đúng một khối ngắn:

```
🎯 Ngách được chọn: <tên> · VERDICT: <GO | NO-GO>

Cổng quyết định: <cổng nào, một câu, kèm dòng bảng cầu>

Đã ghi: ho-so-kenh/ngach.md, ho-so-kenh/nguoi-xem.md (bản đầu)

Còn thiếu: <ví dụ «lớp 4 của chân dung người xem chưa có câu nguyên văn»; «ô chưa đọc: …»>

Ra ngoài: <nếu dùng Chrome: đã được bạn đồng ý, chỉ đọc youtube.com trên Chrome của bạn qua Claude in Chrome, không phí, không khoá; nội dung đọc vào phiên Claude, ảnh lưu trong ho-so-kenh/bang-chung-cau/ hoặc ghi ảnh không lưu được | nếu dùng đường tay: không gọi mạng, số do bạn tự đọc rồi dán>. Thiếu số thì dừng, ghi cần tra; chỉ ghi trong ho-so-kenh/. [Nếu phiên đã chạy lệnh đọc nào (grep, wc…) thì nói đúng ở đây; không viết «không lệnh» khi đã chạy.]

Bước kế tiếp: <10x-yt-dao-binh-luan nếu họ có bình luận để dán | 10x-yt-video-thang nếu họ có danh sách video đối thủ | làm lại ngách nếu NO-GO>
Chạy 10x-yt-cua để cập nhật dòng ke-tiep trong kenh.md.
```

Viết đúng chữ «Đã ghi:» và «Ra ngoài:» ở đầu dòng, có dấu hai chấm, **không in đậm** (máy đếm hai dòng này). Dòng «Bước kế tiếp» nêu **đúng một** tên skill. Nếu chưa biết họ có bình luận hay danh sách video, hỏi họ **một câu** rồi mới nêu.
