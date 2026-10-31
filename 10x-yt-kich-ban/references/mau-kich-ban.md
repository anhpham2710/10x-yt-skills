# Khuôn `ho-so-kenh/kich-ban/<ma>.md`

Đây là khuôn đầu ra của `10x-yt-kich-ban`. Giữ **đúng tên các mục và các nhãn dòng** (mỗi nhãn một dòng, viết đúng chữ) vì `10x-yt-soat` và các lệnh kiểm tự động đọc theo đó. Hợp đồng dữ liệu chỉ khoá tên tệp (`references/chung/ho-so-kenh.md`, mục 1 và 3.4); phần thân dưới đây do skill này định nghĩa.

`<ma>` là mã đề tài chép nguyên từ `goi/<ma>.md` và cột `ma` của `de-tai.md`. Không đặt mã khác.

## 1. Khuôn trống

````markdown
# Kịch bản: <ma> · <đề tài, chép từ goi/<ma>.md>

kich-ban-nguon: goi/<ma>.md · cong-loi-hua: PASS · <ngày của dòng PASS>
outline-duyet: <YYYY-MM-DD> · "<nguyên lời người dùng khi duyệt dàn ý>"

> Mọi thứ trong tệp này là giả thuyết cho tới khi video được đăng và có số. Tệp này chưa qua soát; người viết không tự chấm mình. Việc kế: 10x-yt-soat.

## 1. Lời hứa và chất liệu
Lời hứa phải trả: <chép nguyên từ goi/<ma>.md, mục 8>
Điều video không được hứa thêm: <chép nguyên từ goi/<ma>.md, mục 8>
Đường giữ chân của video trước: <chép từ nhat-ky-thu.md hoặc so-video.csv, kèm nhãn và ngày> | chua-co

Kho chất liệu (chép nguyên lời người dùng, đánh số):
- M1 `[TRÍCH]` "<nguyên văn>" — <chuyện | số | case | quy trình | lời khách>, nguồn: <người dùng kể ngày … | tệp chất liệu dòng …>
- M2 …

## 2. Hook
Khung: <tên khung, lấy từ references/khung-hook.md> · chất liệu dùng: <M?>
Lời hook:
> <các câu nói ra, mỗi câu một dòng bắt đầu bằng "> ">
Số từ: <số đã đếm> (mục tiêu ≤ 60 từ `[ĐỀ XUẤT]`, tương đương khoảng 20 giây)
Hook trả lời lời hứa: "<lời hứa>" ← "<câu trong hook trả lời nó>"
(cảnh chiếu hoặc việc làm trong hook, nếu có): <mô tả>

## 3. Thân
### Đoạn 1 · <tên ngắn>
Ý: <một câu>
Bằng chứng: <M? | D? | [CẦN NGUỒN: cần gì]>
Ví dụ: <M? | [CẦN NGUỒN: cần gì]>
Nói:
- <gạch đầu dòng nói được>
- <gạch đầu dòng nói được>
Nối: <mở vòng | ngắt nhịp | nhắc lý do> — <câu nối>

### Đoạn 2 · <tên ngắn>
(cùng khuôn)

## 4. Chốt tập
Tóm một câu: <điều video đã trả lời>
Video kế: <ma và đề tài từ de-tai.md | chua-co-de-tai-ke>
Cầu nối: <câu nói ra, dẫn từ video này sang video kế>
Lời mời: <một dòng>
Nguồn lời mời: <loi-moi | người dùng viết | [CẦN NGUỒN: lời mời]>
Căn cứ video kế: <vì sao tập này + nguồn: câu người xem ở binh-luan.md | lượt xem ở so-video.csv | truy nguồn ở de-tai.md; chưa có dữ liệu người xem thì nói thẳng>
Màn hình cuối: <trỏ sang tập ở Video kế (ghi tên); chừa vài giây cuối không nói điều quan trọng>

## 5. Bảng dữ kiện
| # | Dữ kiện (số hoặc tên) | Nhãn | Nguyên văn trong chất liệu | Dùng ở |
|---|---|---|---|---|
| D1 | <số hoặc tên đúng như viết trong phần Nói> | `[SỐ LIỆU]` hoặc `[TRÍCH]` | "<câu chứa nó, chép nguyên từ chất liệu>" (M?) | Đoạn ? |

## 6. Chỗ còn thiếu
- Đoạn ?: `[CẦN NGUỒN: <cần gì>]`. Người dùng có thể lấp bằng: <một câu hỏi cụ thể>
(Không có chỗ thiếu thì ghi: "Không có.")

## 7. Phương án hook đã bỏ
- <khung> · "<hook>" · bỏ vì <lý do ngắn>

## 8. Tự kiểm
(bảng K1 đến K12 trong SKILL.md, mỗi dòng có số đã đếm và ✔ hoặc ✘)
````

Ghi chú về khuôn:

- Dòng `kich-ban-nguon:` và `outline-duyet:` nằm **ngay dưới tiêu đề**, mỗi dòng riêng. Không có dòng `soat-truoc-quay:` ở đây: dòng đó do `10x-yt-soat` ghi, không phải skill này.
- Mọi chữ **nói ra** nằm ở đúng hai chỗ: dòng `> ` trong mục 2 và gạch đầu dòng sau nhãn `Nói:` trong mục 3, cộng dòng `Cầu nối:` và `Lời mời:` ở mục 4. Các dòng còn lại là ghi chú cho người làm, không nói ra.
- Phương án hook bỏ **không** nằm trong mục 2, để lệnh đếm từ của hook chỉ đếm hook thật.

## 2. Mỗi kiểm máy đọc dòng nào

Bảng này cho người viết skill, người viết lệnh kiểm trong `_test/kiem/` và người soát. Mỗi kiểm máy `KM-kb-*` của kế hoạch test (`docs/youtube-suite/04-ke-hoach-test.md` §5.7) đọc đúng những dòng sau.

| Kiểm máy | Đọc | Xanh khi | Bước trong SKILL.md sinh ra nó |
|---|---|---|---|
| `KM-kb-1` hook ngắn | Các dòng `> ` trong mục 2 | Tổng số từ ≤ 60 `[ĐỀ XUẤT]`. Dòng `Số từ:` khớp số đếm thật | Bước 3 (hook), kiểm K1 |
| `KM-kb-2` số có nhãn và có trong chất liệu | Mọi số và tên riêng trong các dòng `> `, trong gạch đầu dòng sau `Nói:`, `Cầu nối:`, `Lời mời:`; cùng bảng ở mục 5 | Mỗi số/tên đi kèm một dấu `[D#]`; mỗi `D#` có dòng trong bảng, có nhãn, và cột «Nguyên văn trong chất liệu» là chuỗi có thật trong chất liệu đầu vào | Luật chất liệu; Bước 4 và 6; kiểm K3, K4 |
| `KM-kb-3` có dàn ý chờ duyệt | Dòng `outline-duyet:` | Có dòng, có ngày, có lời duyệt trong dấu ngoặc kép; nhật ký phiên cho thấy lượt người dùng duyệt đứng **trước** lượt viết bản đủ | Bước 2 (cổng dàn ý), kiểm K5 |
| `KM-kb-4` có chốt tập nêu video kế | Mục 4: dòng `Video kế:` và `Cầu nối:` | Cả hai dòng có chữ sau dấu hai chấm | Bước 5, kiểm K7 |
| `KM-kb-7` chốt tập có căn cứ và màn hình cuối | Mục 4: dòng `Căn cứ video kế:` và `Màn hình cuối:` | Khi `Video kế:` là mã thật, cả hai dòng có từ 3 từ trở lên | Bước 5, kiểm K7 |
| `KM-kb-5` thiếu chất liệu thì `[CẦN NGUỒN]` | Dòng `Bằng chứng:` và `Ví dụ:` của từng đoạn; mục 6 | Đoạn mà chất liệu không có phần cần thì dòng đó mang `[CẦN NGUỒN: …]`, và đoạn đó được liệt kê ở mục 6 | Luật chất liệu; kiểm K6 |

Ca cổng phụ `F-thieu-goi` (không có gói đạt): bản thật **dừng** bằng một dòng bắt đầu `⛔`, **không tạo** tệp `kich-ban/<ma>.md` và không có mục `## 2. Hook`. Lệnh kiểm DỪNG của 04 (`grep -c '^⛔\|^DỪNG'` ≥ 1 và số lần xuất hiện `## 2. Hook` = 0) chạy được trên đầu ra đó.

## 3. Ví dụ đã điền (chỉ để thấy dáng; ĐỪNG chép nội dung)

Đề tài giả định, trung tính, tiếp nối ví dụ trong `10x-yt-dong-goi/references/mau-goi.md`. Nội dung dưới đây **không phải dữ liệu thật** của ai; nó chỉ cho thấy độ dài, nhãn và cách ghi.

````markdown
# Kịch bản: 04-slide-cho-nguoi-khong-biet-thiet-ke · Làm slide thuyết trình cho người không biết thiết kế

kich-ban-nguon: goi/04-slide-cho-nguoi-khong-biet-thiet-ke.md · cong-loi-hua: PASS · 2026-10-24
outline-duyet: 2026-10-25 · "ok, đi theo dàn ý này"

> Mọi thứ trong tệp này là giả thuyết cho tới khi video được đăng và có số. Tệp này chưa qua soát; người viết không tự chấm mình. Việc kế: 10x-yt-soat.

## 1. Lời hứa và chất liệu
Lời hứa phải trả: chiếu một slide rối thật của mình, chỉ đúng chỗ rối, nói video sẽ sửa thành một ý.
Điều video không được hứa thêm: thời gian làm xong, mức người nghe «chú ý hơn».
Đường giữ chân của video trước: chua-co

Kho chất liệu:
- M1 `[TRÍCH]` "Mình có hai bản slide cũ, một bản rối một bản đã gọn lại." — case, nguồn: người dùng kể 2026-10-25
- M2 `[TRÍCH]` "Bản rối có tám dòng chữ trên một slide, người nghe không biết nhìn vào đâu." — case, nguồn: người dùng kể 2026-10-25
- M3 `[TRÍCH]` "Bản gọn chỉ còn một câu và một hình." — case, nguồn: người dùng kể 2026-10-25

## 2. Hook
Khung: Lời hứa thẳng, kèm cảnh đang diễn ra · chất liệu dùng: M1, M2
Lời hook:
> Slide này có tám dòng chữ [D1], và chính mình cũng không biết nhìn vào đâu.
> Trong video này mình chỉ ra đúng chỗ khiến nó rối, rồi sửa nó thành một ý.
> Đi vào luôn nào.
Số từ: 36 (mục tiêu ≤ 60 từ `[ĐỀ XUẤT]`, tương đương khoảng 20 giây)
Hook trả lời lời hứa: "chỉ đúng chỗ rối, sửa thành một ý" ← "mình chỉ ra đúng chỗ khiến nó rối, rồi sửa nó thành một ý"
(cảnh chiếu): chiếu ngay slide rối cũ lên màn hình từ giây đầu

## 3. Thân
### Đoạn 1 · Chỗ rối nằm ở đâu
Ý: người nghe rối vì slide hỏi họ nhìn vào đâu mà không trả lời.
Bằng chứng: M2
Ví dụ: M1 (bản rối)
Nói:
- Quay lại slide rối. Có tám dòng chữ [D1], và không dòng nào lớn hơn dòng nào.
- Người nghe không có chỗ để bắt đầu.
Nối: mở vòng — Có một việc đơn giản hơn là bớt chữ, lát nữa mình chỉ.

### Đoạn 2 · Cùng nội dung, sửa thành một ý
Ý: sửa slide là chọn một câu cho người nghe nhớ.
Bằng chứng: M3
Ví dụ: [CẦN NGUỒN: một slide trước và sau mà người dùng đã dùng thật, để chiếu cạnh nhau]
Nói:
- Đây là bản gọn: chỉ còn một câu và một hình.
Nối: ngắt nhịp — Bạn thử đoán mình đã bỏ những gì.

## 4. Chốt tập
Tóm một câu: slide dễ nghe là slide chỉ có một ý.
Video kế: 05-cach-chon-hinh-cho-slide
Cầu nối: Còn cái hình trong bản gọn thì mình chọn thế nào? Mình làm ở video sau.
Lời mời: Nếu bạn có một slide đang rối, bấm đăng ký để xem video sau mình sửa tiếp.
Nguồn lời mời: người dùng viết
Căn cứ video kế: de-tai.md ghi tập này truy từ video đã đăng cùng chủ đề; chưa có dữ liệu người xem (binh-luan.md, so-video.csv).
Màn hình cuối: trỏ sang 05-cach-chon-hinh-cho-slide; chừa vài giây cuối không nói điều quan trọng.

## 5. Bảng dữ kiện
| # | Dữ kiện (số hoặc tên) | Nhãn | Nguyên văn trong chất liệu | Dùng ở |
|---|---|---|---|---|
| D1 | tám dòng chữ | `[TRÍCH]` | "Bản rối có tám dòng chữ trên một slide, người nghe không biết nhìn vào đâu." (M2) | Hook, Đoạn 1 |

## 6. Chỗ còn thiếu
- Đoạn 2, ví dụ: `[CẦN NGUỒN: một slide trước và sau mà người dùng đã dùng thật]`. Người dùng có thể lấp bằng: "Bạn có thể đưa mình tên hai tệp slide cũ và mới để chiếu cạnh nhau không?"

## 7. Phương án hook đã bỏ
- Câu hỏi của người xem · "Làm slide mà không biết thiết kế thì bắt đầu từ đâu?" · bỏ vì `binh-luan.md` chưa có, không có câu nguyên văn để dẫn

## 8. Tự kiểm
(K1 đến K12, mỗi dòng có số đã đếm và ✔ hoặc ✘)
````

## 4. Ca đối chứng hỏng: luật nào nằm ở dòng nào

Kế hoạch test (`docs/youtube-suite/04-ke-hoach-test.md` §5.7) có hai ca đối chứng hỏng. Bảng này chỉ chỗ để người dựng ca gỡ đúng một luật mà không sót, và để thấy bản gỡ phải ĐỎ.

| Ca | Luật bị gỡ | Nằm ở đâu trong `SKILL.md` | Gỡ rồi, đầu ra ĐỎ ở |
|---|---|---|---|
| H-gỡ | «Thiếu chất liệu ⇒ `[CẦN NGUỒN]`» | Mục «Luật chất liệu: thiếu thì `[CẦN NGUỒN]`, không bịa» (cả mục); câu «Áp **Luật chất liệu**…» ở Bước 2, ý 3; lựa chọn `[CẦN NGUỒN: cần gì]` trong khuôn Bước 4; dòng K6 ở Bước 7; mục 6 «Chỗ còn thiếu» của khuôn | Đầu vào KB-3 (chất liệu bị cắt mất số liệu của một đoạn): đoạn đó không có `[CẦN NGUỒN]` ⇒ `KM-kb-5` = 1, và nếu kịch bản điền số cho đoạn đó thì số không có trong chất liệu ⇒ `KM-kb-2` = 1 |
| H-vào | «Gói chưa qua cổng lời hứa thì không viết» | Bảng «Cổng dừng», dòng ⛔ 4; Bước 0, ý 5 | Đầu vào `F-thieu-goi`: bản thật dừng bằng dòng `⛔` và không tạo tệp. Bản gỡ ⛔ 4 sẽ sinh hook và thân ⇒ kiểm DỪNG đỏ |

Chú ý: luật «số/tên không chép được nguyên văn từ chất liệu thì không được nằm trong lời nói» (Bước 6, ý 4) là **luật riêng**, không bị gỡ cùng H-gỡ. Vì vậy với bản gỡ, `KM-kb-5` đỏ chắc chắn (đoạn thiếu không có `[CẦN NGUỒN]`), còn `KM-kb-2` đỏ khi mô hình tự điền số.
