# Mẫu tệp đầu ra, hai ví dụ đã điền, và kiểm máy đọc dòng nào

Đọc ở Bước 7 và 8 của `SKILL.md`. Nội dung ví dụ ở mục 4 **không phải dữ liệu thật của ai**: tên quà, tên video, đề tài đều là giả định trung tính để thấy độ dài, nhãn và cách ghi. **Đừng chép nội dung** sang đầu ra thật; tên quà và đường dẫn phải đến từ chữ người dùng.

## 1. Khuôn tệp `ho-so-kenh/goi/<ma>-loi-moi.md`

Khuôn đầy đủ nằm ở mục «Khuôn đầu ra» của `SKILL.md`. Ghi chú thêm:

- Các dòng `ma:` đến `ghi-chu:` nằm **ngay dưới tiêu đề**, mỗi dòng riêng.
- Dòng `Lời mời:` xuất hiện **đúng một lần** trong cả tệp. Các nơi khác cần nhắc tới lời mời thì viết «lời mời nói» hoặc «dòng ở mục 2», **không** bắt đầu một dòng bằng `Lời mời:`.
- Dòng `Dòng mô tả/ghim:` xuất hiện đúng một lần.
- Chữ của người dùng (tên quà, tên offer, đường dẫn) chỉ nằm ở mục 1 dưới dạng trích nguyên văn, và được **chép lại đúng từng chữ** ở mục 2, 3. Không viết lại ở chỗ nào khác.
- Mục 4 chỉ liệt kê số dòng và năm từ đầu của lời mời cũ; dòng nào chứa từ bán thì ghi «(lời bán, bỏ)».
- Mục 5 (tự kiểm) viết kết quả bằng chữ trung tính. Ở mức `lanh` hoặc không có offer, **không** viết các từ bán ngay cả khi giải thích (xem `khung-loi-moi.md` mục 5).

## 2. Cách điền bảng tự kiểm

| # | Cột «Bằng chứng» ghi gì |
|---|---|
| T1 | «1 dòng `Lời mời:`; 2 lời mời khác ở kịch bản (dòng 8, 31) đã liệt kê ở mục 4» |
| T2 | «Mức lạnh, bậc B1, không từ nào trong danh sách từ bán» |
| T3 | «chưa có sản phẩm bán (kenh.md)» hoặc «có sản phẩm bán, bậc ≤ tối đa» |
| T4 | Câu kịch bản (số dòng) mà vế lợi ích truy về |
| T5 | Mục 1 chứa chuỗi tên quà; hoặc «không có tên quà trong đầu ra» |
| T6 | «Đứng sau `Cầu nối:` (dòng …)» |
| T7 | «N từ; không có đường dẫn trong câu nói» |
| T8 | «`Video kế:` và `Cầu nối:` còn nguyên» |
| T9 | «Ngôn ngữ vi, xưng "mình/bạn" như kịch bản» |
| T10 | «Chữ người dùng gắn [TRÍCH]; phần suy ra gắn [SUY LUẬN]» |

## 3. Kiểm máy đọc dòng nào

Bảng này cho người viết skill, người viết lệnh kiểm trong `_test/kiem/` và người soát. Mỗi kiểm máy `KM-lm-*` của kế hoạch test (`docs/youtube-suite/04-ke-hoach-test.md` §5.12) đọc đúng những dòng sau.

| Kiểm máy | Ca | Đọc | Xanh khi | Bước/khuôn sinh ra nó |
|---|---|---|---|---|
| `KM-lm-1` đúng một lời mời | LM-1, LM-2 | Đếm dòng bắt đầu bằng `Lời mời:` trong tệp đầu ra | Đúng 1 | Bước 5 (một câu); kiểm T1; khuôn mục 2 |
| `KM-lm-2` mọi tên quà/offer/URL có trong đầu vào | LM-1, LM-2 (và đối chứng hỏng) | Mục 1, dòng `Lời mời:`, dòng `Dòng mô tả/ghim:` | Mọi tên và đường dẫn tìm được nguyên văn (`grep -F`) trong chữ người dùng đưa (`tra-loi.md`, kịch bản). Ca không offer: không có tên quà nào trong đầu ra | «Luật không bịa quà»; Bước 4; kiểm T5 |
| `KM-lm-3` ca không offer, mức lạnh, không từ bán | LM-2 | Toàn bộ tệp đầu ra | Không chứa từ nào trong danh sách từ bán (`khung-loi-moi.md` mục 5) | Bước 3 (lạnh ⇒ B1); Bước 5 mục 6; kiểm T2 |
| `KM-lm-4` ≥ 3 chỉ số đo được và link có tham số theo dõi | LM-3 (chế độ «đường đầy đủ», kênh của chủ bộ skill) | Bảng đường đi và các dòng link | Xem tệp chế độ đường đầy đủ, nếu máy có | `references/duong-day-du/duong-day-du.md` |

Ca đối chứng hỏng (H-gỡ): gỡ khối **«Luật không bịa quà»** trong `SKILL.md`, đầu vào LM-2 (không offer, mức lạnh). **ĐỎ đo bằng** `KM-lm-2` = 1 khi đầu ra có tên quà không có trong đầu vào. Bản thật giữ khối đó nên đầu ra chỉ mời bước trong kênh và `KM-lm-2` = 0.

Ca cổng phụ (H-vào): `F-khong-offer` với người dùng nói «mình định làm một cái checklist» ⇒ bản thật coi là kế hoạch, không mời nhận checklist.

## 4. Hai ví dụ đã điền (không phải dữ liệu thật)

### 4.1 Mức lạnh, không có quà, chưa có sản phẩm bán

````markdown
# Lời mời: Làm slide thuyết trình cho người không biết thiết kế · lượt 2026-10-25

- ma: 04-slide-cho-nguoi-khong-biet-thiet-ke
- che-do: mot-dong
- muc-ham-nong: lanh (nguồn: nguoi-dung-noi · "người xem chưa biết mình")
- track: A (nguồn: kenh.md)
- bac-moi: B1
- ghi-chu: Mọi thứ dưới đây là giả thuyết cho tới khi video đăng và 10x-yt-doc-so đọc số.

## 1. Nguồn quà / offer (chữ của người dùng, không phải của skill)

- Quà/offer: không có, chỉ mời bước trong kênh
- Đường dẫn: không có

## 2. Lời mời nói (một dòng, đặt sau Cầu nối)

Lời mời: Nếu phần vừa rồi giúp được bạn, xem tiếp video mình sửa một slide đang rối, mình để ngay bên dưới.
Nguồn lời mời: bước trong kênh, không dùng quà · 2026-10-25
Đặt ở: sau dòng «Cầu nối:» của chốt tập, trước lời chào kết

## 3. Dòng cho mô tả hoặc bình luận ghim

Dòng mô tả/ghim: Xem tiếp: [CẦN NGUỒN: đường dẫn video kế]

## 4. Lời mời khác đang có trong kịch bản (cần bỏ)

- dòng 3 · "Nhớ đăng ký kênh và bấm" (lời nhắc ở mở đầu)

## 5. Tự kiểm

| # | Kiểm | Kết quả | Bằng chứng |
|---|---|---|---|
| T1 | Một lời mời duy nhất | PASS | 1 dòng `Lời mời:`; 1 lời mời khác (dòng 3) đã liệt kê ở mục 4 |
| T2 | Khớp mức hâm nóng | PASS | Mức lạnh, bậc B1, không từ nào trong danh sách từ bán |
| T3 | Khớp sản phẩm bán | PASS | chưa có sản phẩm bán, bậc B1 |
| T4 | Không hứa vượt bằng chứng | PASS | Lợi ích «giúp được bạn» truy về `Tóm một câu:` (dòng 41) |
| T5 | Truy nguồn tên | PASS | Không có tên quà hay offer trong đầu ra |
| T6 | Đặt sau điều có ích | PASS | Đứng sau `Cầu nối:` (dòng 44) |
| T7 | Một câu, ngắn | PASS | 22 từ; không có đường dẫn trong câu nói |
| T8 | Video kế không bị thay | PASS | `Video kế:` và `Cầu nối:` còn nguyên |
| T9 | Ngôn ngữ và giọng | PASS | vi; xưng «mình/bạn» như kịch bản |
| T10 | Nhãn nguồn | PASS | Mức hâm nóng ghi nguồn; chỗ thiếu đường dẫn mang `[CẦN NGUỒN]` |

## 6. Việc người dùng làm tay

- Dán dòng «Lời mời:» vào chốt tập, bỏ lời mời ở mục 4.
- Đưa dòng «Dòng mô tả/ghim:» cho 10x-yt-dang, điền đường dẫn video kế khi đã đăng.
````

### 4.2 Mức ấm, có quà, có sản phẩm bán

````markdown
# Lời mời: Làm slide thuyết trình cho người không biết thiết kế · lượt 2026-10-25

- ma: 04-slide-cho-nguoi-khong-biet-thiet-ke
- che-do: mot-dong
- muc-ham-nong: am (nguồn: nguoi-dung-noi · "họ đã xem vài video của mình")
- track: B (nguồn: kenh.md)
- bac-moi: B2
- ghi-chu: Mọi thứ dưới đây là giả thuyết cho tới khi video đăng và 10x-yt-doc-so đọc số.

## 1. Nguồn quà / offer (chữ của người dùng, không phải của skill)

- Quà/offer: "<tên quà đúng từng chữ người dùng gõ>" [TRÍCH] (người dùng nói 2026-10-25)
- Đường dẫn: <đường dẫn đúng từng chữ người dùng đưa>

## 2. Lời mời nói (một dòng, đặt sau Cầu nối)

Lời mời: Mình có sẵn <tên quà> để bạn sửa slide của mình, link ở phần mô tả.
Nguồn lời mời: quà ở mục 1 · 2026-10-25
Đặt ở: sau dòng «Cầu nối:» của chốt tập, trước lời chào kết

## 3. Dòng cho mô tả hoặc bình luận ghim

Dòng mô tả/ghim: <tên quà>: <đường dẫn>
````

Ở ví dụ 4.2, `<tên quà>` và `<đường dẫn>` là chỗ chép nguyên văn chữ người dùng; ví dụ này cắt bớt mục 4 đến 6 cho gọn, bản thật vẫn đủ sáu mục.
