# Khuôn báo cáo soát và dòng cờ

Đây là khuôn đầu ra của `10x-yt-soat`. Giữ **đúng nhãn các dòng và các cột** vì lệnh kiểm tự động và các skill sau (cửa, đăng) đọc theo đó. Hợp đồng dữ liệu chỉ khoá tên tệp và hai dòng cờ (`references/chung/ho-so-kenh.md`, mục 3.4); phần báo cáo do skill này định nghĩa.

Skill soát **không tạo tệp mới** trong `ho-so-kenh/`. Hợp đồng không có chỗ cho báo cáo soát, nên báo cáo nằm trong cuộc trò chuyện. Thứ được ghi vào hồ sơ chỉ có hai thứ: một dòng cờ trong `kich-ban/<ma>.md` và một dòng `soat:` trong `TIEN-DO` của `kenh.md`.

## 1. Khuôn báo cáo trong cuộc trò chuyện

````markdown
🔎 Soát <trước quay | trước đăng> video <ma>: <PASS | TRƯỢT>

Độc lập: <CÓ | KHÔNG: cùng phiên với lượt viết>
Đã đọc: goi/<ma>.md · kich-ban/<ma>.md · <số dòng của kịch bản> dòng

| # | Tiêu chí | Kết quả | Đã kiểm | Câu trích (khi FAIL) |
|---|---|---|---|---|
| S1 | Lời hứa trả trong 20 giây đầu | PASS | <số đếm> | |
| S2 | Mỗi dữ kiện có nhãn nguồn | FAIL | <số đếm và loại trượt> | "<câu nguyên văn>" |
| S3 | Không nghe chung chung, không nghe kiểu AI | PASS | <số đếm> | |
| S4 | Mỗi đoạn có lý do tồn tại | PASS | <số đếm> | |
| S5 | Chốt tập có cầu nối | PASS | <số đếm> | |
| S6 | Lời mời khớp mức hâm nóng | PASS | <số đếm> | |

Việc sửa (tối đa 3, việc quan trọng nhất trước):
1. [S2] <động từ + hướng sửa, không viết câu thay>. Xong khi: <phép kiểm đo được>.
2. …

Để vòng sau: <mã các tiêu chí FAIL chưa có trong danh sách trên | Không có>

Đã ghi: <dòng cờ và dòng TIEN-DO đã ghi | Không ghi cờ vì …>

Bước kế tiếp: <một tên>
````

Quy tắc cho từng phần:

- **Dòng đầu** có đúng một giá trị `PASS` hoặc `TRƯỢT` (có dấu, để người đọc không phải đoán). `PASS` khi và chỉ khi cả sáu hàng là PASS. Chỉ dòng cờ ghi vào tệp (mục 4) giữ `TRUOT` không dấu cho máy đọc.
- **Cột «Đã kiểm»** viết bằng lời thường, không mã nội bộ: không `M1`, `M2`, `M3` (trùng mã chất liệu của người dùng); nói «câu sáo mở», «đoạn thay người được», «chỗ phóng đại rỗng».
- **Bảng** luôn đủ sáu hàng `S1` đến `S6`, đúng thứ tự, kể cả khi PASS hết. Cột «Kết quả» chỉ có hai giá trị `PASS` hoặc `FAIL`. Không điểm số, không «gần đạt», không «PASS có điều kiện».
- **Cột «Đã kiểm»** luôn có **số đã đếm hoặc đối chiếu đã làm**, kể cả hàng PASS. Ví dụ: «7 số/tên · 7 có D · 7 khớp chất liệu», «hook 38 từ · câu hook đáp gói ở từ thứ 9», «4 đoạn · 4 trỏ được vào lời hứa · 0 CẦN NGUỒN». Chữ «ổn», «ok», «tốt» không phải kiểm.
- **Cột «Câu trích»** chỉ điền ở hàng FAIL. Xem mục 2 «Cách trích».
- **Việc sửa:** mỗi việc một dòng bắt đầu bằng số thứ tự và mã tiêu chí trong ngoặc vuông. Tối đa 3 việc, dù FAIL nhiều hơn. Thứ tự ưu tiên ở mục 3. Mỗi việc nói **cần làm gì** và **xong khi nào**, không soạn câu thay. Không trích lại câu đã trích ở bảng; chỉ ghi «câu ở hàng S2».
- **Để vòng sau:** chỉ liệt kê **mã** (ví dụ `S3, S5`), không viết thành việc, để dòng này không bị đếm như việc sửa.
- **Độ dài:** báo cáo thường 15 đến 25 dòng và **luôn ngắn hơn nửa số dòng của kịch bản** (soát không viết hộ).
- **Không** có mục «kịch bản đã chỉnh», «bản gợi ý», «ví dụ câu tốt hơn», điểm tổng, hay lời khen suông.

Nói **một lần** ở báo cáo đầu tiên của mỗi phiên: «PASS nghĩa là kịch bản qua sáu cổng kiểm này, chưa có nghĩa là video sẽ chạy tốt. Mọi thứ ở đây là giả thuyết cho tới khi video đăng và có số.»

## 2. Cách trích

Kiểm máy sẽ tìm câu trích **nguyên văn** trong tệp kịch bản. Vì vậy:

1. Chép **đúng từng chữ, đúng dấu tiếng Việt**, kể cả dấu `[D1]` hay nhãn nếu câu có. Không sửa chính tả, không đổi chữ in hoa.
2. Bỏ **chỉ** phần đánh dấu đầu dòng của tệp (`> `, `- `). Phần còn lại giữ nguyên.
3. Đặt trong dấu nháy kép thẳng `"`. Trích cả câu, hoặc một đoạn liền của câu nếu câu quá dài. Cắt ở **đầu hoặc cuối** được; **không** dùng dấu `…` ở giữa câu trích, vì nó biến câu thành chuỗi không có trong tệp.
4. Mỗi hàng FAIL **một** câu trích (câu nặng nhất). Còn chỗ khác cùng lỗi thì ghi vào cột «Đã kiểm» («và 2 chỗ nữa: Đoạn 2, Đoạn 3»).
5. Lỗi do **thiếu** một thứ: trích dòng nhãn nguyên văn hoặc dòng liền kề nơi thứ đó đáng lẽ có (ví dụ `Cầu nối:` hay dòng `Video kế:`), kèm «(dòng trống)» ở cột «Đã kiểm».
6. Câu có ký tự `|` thì không đặt trong ô bảng (làm vỡ bảng). Ghi «xem dưới bảng» trong ô và đặt câu trích ở dòng riêng ngay dưới bảng, bắt đầu bằng mã, ví dụ `S2: "…"`.
7. Trước khi trả, **tìm lại từng câu trích trong tệp**. Không tìm thấy thì sửa lại câu trích hoặc đổi hàng về PASS nếu bạn không còn tìm được lỗi.

## 3. Việc sửa: chọn và xếp thế nào

Một lượt chỉ cho tối đa 3 việc, vì người viết sửa 20 điều cùng lúc thì không biết điều nào gây ra điều nào (ý «một việc sửa, không phải 20 việc», xem mục nguồn ở `SKILL.md`). Cách chọn:

1. **Gộp** các hàng FAIL cùng một gốc thành một việc (ví dụ cùng một câu vừa trượt S1 vừa nằm trong đoạn trượt S4 thì vẫn là hai tiêu chí nhưng một chỗ sửa).
2. **Xếp theo mức hại**, `[ĐỀ XUẤT]` (chưa kiểm):
   1. S2: dữ kiện bịa hoặc không truy được; hại uy tín người nói và sai với người xem.
   2. S1: lời hứa không được trả; hỏng ngay giây đầu, kéo theo CTR đã mua bằng tiêu đề.
   3. S4: đoạn thừa hoặc đoạn chưa có gì để nói.
   4. S6: lời mời vượt mức; mất niềm tin.
   5. S5: chưa có cầu nối.
   6. S3: giọng chung chung.
3. Trong cùng một tiêu chí, ưu tiên loại nặng hơn (bảng «Loại trượt» ở `rubric.md`, tiêu chí S2).
4. Hàng FAIL không vào 3 việc đầu thì ghi mã ở «Để vòng sau». Sửa xong 3 việc, chạy soát lại: những cái hoãn sẽ hiện lại nếu còn.

Mỗi việc có hai phần, đều viết bằng chữ, không bằng câu mẫu:

- **Việc:** động từ và hướng. Ví dụ đúng: «Gắn nhãn và nguồn cho con số trong câu ở hàng S2, hoặc bỏ con số.» Ví dụ sai: «Đổi thành: "Slide này có tám dòng chữ [D1]…"».
- **Xong khi:** phép kiểm đo được người viết tự làm. Ví dụ: «mọi số trong hook có `[D#]` và dòng bảng có nguyên văn tìm lại được trong Kho chất liệu».

## 4. Dòng cờ và `TIEN-DO`

Dòng cờ nằm riêng một dòng trong `ho-so-kenh/kich-ban/<ma>.md`, **ngay dưới dòng `outline-duyet:`** (không có dòng đó thì ngay dưới tiêu đề). Đúng khuôn của hợp đồng:

| Chế độ | Dòng cờ | Khi nào ghi |
|---|---|---|
| Trước quay | `soat-truoc-quay: PASS · <YYYY-MM-DD>` hoặc `soat-truoc-quay: TRUOT · <YYYY-MM-DD>` | Cuối mỗi lượt soát trước quay |
| Trước đăng | `soat-truoc-dang: PASS · <YYYY-MM-DD>` hoặc `soat-truoc-dang: TRUOT · <YYYY-MM-DD>` | Cuối mỗi lượt soát trước đăng |

- Tệp đã có dòng cờ cùng loại thì **thay đúng dòng đó**; không thêm dòng thứ hai. Không đụng dòng nào khác của tệp kịch bản (kể cả dòng ghi «chưa qua soát» của người viết: nó là chữ của skill chủ).
- **Không ghi `PASS`** khi `goi/<ma>.md` chưa có `cong-loi-hua: PASS`. Vẫn trả bảng, nhưng dòng `Đã ghi:` nói «Không ghi cờ vì gói chưa qua cổng lời hứa» và chỉ sang `10x-yt-dong-goi`. Ghi `TRUOT` thì vẫn được.
- Trong `kenh.md`, phần `TIEN-DO`, đổi **đúng một dòng**: `soat:`. Trước quay PASS hoặc TRUOT, hoặc trước đăng TRUOT: `soat: dang · <ngày>`. Trước đăng PASS: `soat: xong · <ngày>`. Không đổi dòng nào khác (dòng `ke-tiep` là của cửa).
- Sau khi người dùng sửa kịch bản, dòng cờ `PASS` cũ **không còn đúng**. Chạy soát lại để thay dòng.

## 5. Mỗi kiểm máy đọc dòng nào

Bảng này cho người viết skill và người viết lệnh kiểm trong `_test/kiem/`. Mỗi kiểm máy `KM-so-*` của kế hoạch test (`docs/youtube-suite/04-ke-hoach-test.md` mục 5.8) đọc đúng những dòng sau của **đầu ra**.

| Kiểm máy | Đọc | Xanh khi | Bước trong SKILL.md sinh ra nó |
|---|---|---|---|
| `KM-so-1` bảng đủ 6 tiêu chí | Sáu hàng bắt đầu `\| S1` đến `\| S6` | Có đủ sáu hàng, mỗi hàng cột «Kết quả» là `PASS` hoặc `FAIL` | Bước 3 (chấm), khuôn ở mục 1; kiểm V1 ở Bước 5 |
| `KM-so-2` mỗi FAIL trích nguyên văn | Cột «Câu trích» của hàng FAIL (và dòng `S#: "…"` dưới bảng nếu có) | Mỗi hàng FAIL có một chuỗi trong dấu nháy kép, và chuỗi đó **tìm thấy nguyên văn** trong tệp kịch bản | Mục 2 «Cách trích»; Bước 3; kiểm V2 |
| `KM-so-3` ≤ 3 việc sửa có thứ tự | Các dòng bắt đầu `1.`, `2.`, `3.`… dưới «Việc sửa» | Không quá 3 dòng; số thứ tự liên tục từ 1; việc đầu thuộc tiêu chí ưu tiên cao nhất trong các hàng FAIL (mục 3) | Bước 4; kiểm V3 |
| `KM-so-4` lỗi gài bị bắt đúng tiêu chí | Hàng `S1` (ca SO-2) và hàng `S2` (ca SO-1) | SO-1: hàng `S2` là FAIL và câu trích là câu bị chèn. SO-2: hàng `S1` là FAIL và câu trích là hook lệch | Bước 3, tiêu chí S1 và S2 (`rubric.md`); luật «mỗi lỗi chỉ tính ở một tiêu chí» |
| `KM-so-5` không viết lại kịch bản | Tổng số dòng của báo cáo so với số dòng của tệp kịch bản | Số dòng báo cáo < `[ĐỀ XUẤT] 50%` số dòng kịch bản; không có khối câu mẫu thay thế | Luật «soát không viết hộ»; Bước 4; kiểm V4, V5 |

Ca cổng dừng: đầu vào thiếu `goi/<ma>.md` hoặc `kich-ban/<ma>.md` ⇒ bản thật dừng bằng một dòng bắt đầu `⛔`, **không có bảng** `S1` đến `S6`, và **không ghi** dòng cờ. Lệnh kiểm DỪNG chạy được: `grep -c '^⛔'` ≥ 1 và số hàng `| S1` = 0.

## 6. Ca đối chứng hỏng: luật nào nằm ở dòng nào

Kế hoạch test (mục 5.8) có một ca đối chứng hỏng: gỡ tiêu chí «mỗi dữ kiện có nhãn nguồn», cho chạy ca SO-1, và kỳ vọng **ĐỎ** ở `KM-so-4`.

| Ca | Luật bị gỡ | Nằm ở đâu | Gỡ rồi, đầu ra ĐỎ ở |
|---|---|---|---|
| H-gỡ | Tiêu chí S2 «mỗi dữ kiện có nhãn nguồn» | `SKILL.md`: dòng S2 trong bảng «Sáu tiêu chí», Bước 3 mục S2 (kiểm từng số một), dòng S2 của khuôn báo cáo, thứ tự ưu tiên của S2. `rubric.md`: cả mục S2 | Ca SO-1 (kịch bản chèn một câu có số không nhãn, không có trong chất liệu): hàng `S2` mất hoặc ra PASS, câu chèn không bị trích ⇒ `KM-so-4` = 1. Hàng `S2` mất cũng làm `KM-so-1` đỏ (thiếu hàng) |

Chú ý để bản gỡ thật sự đỏ: lỗi gài của SO-1 chỉ được **một** tiêu chí bắt, là S2 (luật «mỗi lỗi chỉ tính ở một tiêu chí» ở `rubric.md`). Nếu S3 hay S4 cũng bắt câu chèn, bản gỡ S2 vẫn xanh nhờ tiêu chí khác và ca đối chứng mất tác dụng. Vì vậy `rubric.md` mục S3 và S4 ghi rõ «Không tính ở đây: số không nhãn».

## 7. Ví dụ đã điền (chỉ để thấy dáng; ĐỪNG chép nội dung)

Tiếp nối ví dụ trong `10x-yt-kich-ban`. Đề tài, số và câu trích dưới đây **không phải dữ liệu thật** của ai; con số «70%» ở đây là ví dụ cho một lỗi, không phải sự thật. Giả định người viết chèn thêm vào Đoạn 1 của kịch bản mẫu một gạch: `- Nghiên cứu cho thấy 70% người nghe quên slide sau một ngày.` (không có `[D#]`, không có trong Kho chất liệu).

````markdown
🔎 Soát trước quay video 04-slide-cho-nguoi-khong-biet-thiet-ke: TRƯỢT

Độc lập: CÓ
Đã đọc: goi/04-slide-cho-nguoi-khong-biet-thiet-ke.md · kich-ban/04-slide-cho-nguoi-khong-biet-thiet-ke.md · 62 dòng

| # | Tiêu chí | Kết quả | Đã kiểm | Câu trích (khi FAIL) |
|---|---|---|---|---|
| S1 | Lời hứa trả trong 20 giây đầu | PASS | hook 36 từ · câu hook đáp gói ở từ thứ 12 · 0 điều bị cấm | |
| S2 | Mỗi dữ kiện có nhãn nguồn | FAIL | 2 số · 1 có D khớp chất liệu · 1 không nhãn (loại: Không nhãn) | "Nghiên cứu cho thấy 70% người nghe quên slide sau một ngày." |
| S3 | Không nghe chung chung, không nghe kiểu AI | PASS | 0 câu sáo mở · 0 đoạn thay người được · 1 chỗ phóng đại rỗng | |
| S4 | Mỗi đoạn có lý do tồn tại | FAIL | 2 đoạn · 2 trỏ được vào lời hứa · Đoạn 2 còn CẦN NGUỒN ở dòng Ví dụ | "sửa slide là chọn một câu cho người nghe nhớ." |
| S5 | Chốt tập có cầu nối | PASS | Video kế có trong de-tai.md · cầu nối qua phép thử | |
| S6 | Lời mời khớp mức hâm nóng | PASS | 1 dòng · nguồn: người dùng viết · mức 1, chưa có sản phẩm bán | |

Việc sửa (tối đa 3, việc quan trọng nhất trước):
1. [S2] Gắn `[D#]`, nhãn và nguyên văn cho con số ở câu hàng S2, hoặc bỏ con số. Xong khi: tìm lại được nguyên văn trong Kho chất liệu.
2. [S4] Lấp dòng Ví dụ của Đoạn 2 bằng chất liệu thật của người nói, hoặc cắt đoạn. Xong khi: không còn `[CẦN NGUỒN]` ở dòng Bằng chứng và Ví dụ.

Để vòng sau: Không có

Đã ghi: soat-truoc-quay: TRUOT · 2026-10-26 (kich-ban/04-….md); soat: dang · 2026-10-26 (kenh.md)

Bước kế tiếp: 10x-yt-kich-ban
````

Ghi chú cho ví dụ: ở hàng S4, câu trích là dòng `Ý:` của đoạn có vấn đề (Đoạn 2). Ở hàng S2, cột «Đã kiểm» phân loại lỗi theo bảng «Loại trượt» ở `rubric.md`.
