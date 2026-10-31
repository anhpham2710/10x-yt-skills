# Chế độ «đường đầy đủ»: video → quà → danh sách → offer (chỉ kênh của chủ bộ skill)

> **Không thuộc gói bán.** Xem `KHONG-PHAT-HANH.md` cùng thư mục. Tệp này thay Bước 5 và 6 của `SKILL.md`; các Bước 1, 3, 4, 7, 8 vẫn chạy. Mọi tên quà, tên offer, đường dẫn, tên danh sách trong đầu ra lấy từ chữ người dùng đưa hoặc hồ sơ của họ (xem «Luật không bịa quà» trong `SKILL.md`). Không có thì `[CẦN NGUỒN]`.

Chế độ này vẫn tuân **một lời mời duy nhất mỗi video**: bốn chỗ đặt dưới đây là **bốn cách nói cùng một hành động, cùng một đích**, không phải bốn lời mời khác nhau.

## Đầu vào riêng của chế độ

| Cần | Là gì | Thiếu thì |
|---|---|---|
| **Danh sách quà có thật** | Mỗi quà: tên (chữ người dùng), một câu nó giúp làm việc gì (chữ người dùng), đường dẫn nhận quà | ⛔ D1 |
| **Đích của quà** | Nơi người xem để lại liên hệ để nhận quà, bằng chữ người dùng gọi (trang đăng ký, biểu mẫu, nhóm…) | ⛔ D1 (quà không có đích thì chưa phải quà) |
| **Offer ở cuối đường** (nếu có) | Tên, đường dẫn tìm hiểu | Bỏ chặng offer khỏi bảng, ghi `[CẦN NGUỒN: offer]`; đường vẫn dựng tới chặng đăng ký |
| **Nơi người dùng đọc số bấm và số đăng ký** | Công cụ họ đang có (bảng thống kê của trang đích, công cụ rút gọn link, công cụ email…) | Vẫn dựng bảng; cột nguồn đọc ghi `[CẦN NGUỒN: nơi đọc số]`; nói thẳng «chưa có chỗ đọc thì đường này chưa đo được» |
| Mức hâm nóng của video | Như Bước 3 của `SKILL.md` | Mặc định `lanh` |

### ⛔ D1: không có quà thật

Người dùng chưa có quà nào đã tồn tại (kể cả khi họ nói «sắp làm») hoặc quà chưa có đích nhận ⇒ **dừng chế độ này**. Dòng đầu của câu trả lời bắt đầu `⛔ D1`. Nói: «Chưa có quà thật thì chưa dựng được đường. Mình viết cho video này một lời mời trong kênh (bậc B1).» Rồi chạy chế độ «một dòng» ở bậc B1. **Không đặt tên quà giúp.**

## Quy trình

### D1. Chọn quà theo đề tài (truy nguồn, không đoán)

1. Đọc kịch bản: tìm **việc đầu tiên người xem sẽ muốn làm sau khi nghe xong** (thường nằm ở `Tóm một câu:` và `Cầu nối:`).
2. Với mỗi quà trong danh sách, hỏi: quà này **giúp làm đúng việc đó** không? Căn cứ là **hai đoạn chữ**: một câu của kịch bản (số dòng) và câu người dùng mô tả quà. Ghi cả hai ở bảng chọn quà.
3. Khớp ⇒ chọn quà đó, ghi `[SUY LUẬN]` (khớp là phán đoán, chưa phải số đo). Nhiều quà cùng khớp ⇒ chọn quà **nhỏ nhất** (ít bước nhất), nói lý do, để người dùng đổi.
4. **Không quà nào khớp** ⇒ không ép. Ghi `[CẦN NGUỒN: quà khớp đề tài này]`, hạ lời mời của video này xuống B1, nói thẳng.

### D2. Bậc mời

Dùng bảng bậc tối đa ở Bước 3 của `SKILL.md`. Mức `lanh` ⇒ B1; chế độ này khi đó dựng 4 chỗ cho lời mời B1 (đích là video kế hoặc đăng ký kênh), phần «quà → danh sách → offer» để trống, ghi lý do. Mức `am`, `nong` ⇒ B2 (quà) hoặc B3 (offer). Chưa có sản phẩm bán ⇒ B1. Không B4.

### D3. Bốn chỗ đặt lời mời

Cùng một hành động, cùng một đích, **bốn dạng**:

| Mã chỗ | Là gì | Dạng chữ | Nhãn dòng trong tệp đầu ra |
|---|---|---|---|
| `noi` | Câu nói trong chốt tập, sau `Cầu nối:` | Một câu nói, không đọc đường dẫn | `Lời mời:` (đúng một lần trong cả tệp) |
| `mo-ta` | Dòng đầu phần liên kết của mô tả | Một dòng + đường dẫn có tham số | `Chỗ mo-ta:` |
| `ghim` | Bình luận ghim | Một dòng, có thể thêm câu hỏi gợi người xem trả lời | `Chỗ ghim:` |
| `man-hinh-ket-thuc` | Màn hình kết thúc hoặc thẻ | Tên đích ngắn người dùng sẽ chọn trong YouTube Studio (không có chữ dài) | `Chỗ man-hinh-ket-thuc:` |

Bốn nhãn dòng **khác nhau**, và chỉ dòng `noi` bắt đầu bằng `Lời mời:` (để kiểm máy đếm đúng một lời mời). Chỗ `ghim` không dùng cách viết hàm ý «đảm bảo». Skill không đăng hộ: người dùng tự dán và tự ghim.

### D4. Đường dẫn có tham số theo dõi

Với mỗi chỗ có đường dẫn (`mo-ta`, `ghim`, `man-hinh-ket-thuc`), chép đường dẫn **nguyên văn người dùng đưa**, rồi thêm tham số:

```
<đường dẫn nguyên văn>?utm_source=youtube&utm_medium=<mo-ta|ghim|man-hinh>&utm_campaign=<ma>&utm_content=<mã quà ngắn do người dùng đặt>
```

- Đường dẫn đã có `?` thì nối bằng `&`, không thêm `?` thứ hai.
- `<ma>` là mã video trong hồ sơ. `<mã quà ngắn>` do **người dùng** đặt (tên ngắn không dấu); chưa có thì hỏi một câu, không tự đặt.
- Mỗi chỗ một giá trị `utm_medium` **khác nhau**, để về sau biết chỗ nào có người bấm.
- Công cụ của người dùng không đọc tham số này thì hỏi họ cách gắn mã của công cụ đó, rồi đổi cho khớp; không bịa.
- Không rút gọn link hộ, không gọi dịch vụ rút gọn. Tham số chỉ là nhãn; **số bấm do công cụ của người dùng đếm**.

### D5. Bảng đường đi: video → bấm → đăng ký → (offer)

Mỗi chặng có **ít nhất một chỉ số đo được**, và cả bảng có **ít nhất ba** `[ĐỀ XUẤT]` (lý lẽ: tối thiểu một chỉ số mỗi chặng video → bấm → đăng ký). Ô số để trống nghĩa là chưa đo, không phải 0.

| Chặng | Chỉ số | Nguồn đọc | Số đo | Ngày đo |
|---|---|---|---|---|
| Video | `giu-chan-tai-moc-moi`: phần trăm người xem còn lại ở giây nói lời mời | Đường cong giữ chân của video trong YouTube Studio | | |
| Bấm | `luot-bam-theo-cho`: lượt bấm của từng link (`mo-ta`, `ghim`, `man-hinh`) | Công cụ đếm bấm hoặc thống kê trang đích của người dùng | | |
| Đăng ký | `luot-dang-ky-theo-chien-dich`: số người để lại liên hệ gắn `utm_campaign=<ma>` | Công cụ nhận đăng ký của người dùng | | |
| Đăng ký | `ti-le-dang-ky-tren-bam`: số đăng ký chia số bấm | **Tính bằng phép chia ghi cả hai số**, không nhẩm | | |
| Offer (tuỳ chọn) | `luot-xem-trang-offer-tu-danh-sach`: lượt vào trang tìm hiểu offer từ người đã vào danh sách | Công cụ của người dùng; nằm ngoài YouTube | | |

Luật dùng bảng:

1. Skill **không đặt ngưỡng «tốt» hay «xấu»** cho bất kỳ chỉ số nào (xem `da-bi-bac.md`). So sánh về sau là so với **chính các video của kênh**, bằng `10x-yt-doc-so`.
2. Hẹn đo lại theo mốc của `doc-so` `[ĐỀ XUẤT] 48 giờ / 7 ngày / 30 ngày` (cùng mốc `KM-ds-2` của kế hoạch test); điền ngày cụ thể vào cột «Ngày đo».
3. **Không điền số giả lập vào ô số.** Bảng mới tạo thì cột «Số đo» và «Ngày đo» trống.
4. Khi người dùng đưa số thật, mới điền, mang `[SỐ LIỆU]` kèm nguồn và ngày.

### D6. Tự kiểm bổ sung (cộng với T1 đến T10 của `SKILL.md`)

| # | Kiểm | PASS khi |
|---|---|---|
| F1 | Bốn chỗ cùng một đích | `noi`, `mo-ta`, `ghim`, `man-hinh-ket-thuc` cùng một hành động và cùng một đích; không chỗ nào mời thêm việc thứ hai |
| F2 | Link có tham số | Mọi đường dẫn trong tệp đầu ra mang đủ `utm_source`, `utm_medium`, `utm_campaign`; ba chỗ có ba `utm_medium` khác nhau |
| F3 | Bảng đủ chỉ số | ≥ `[ĐỀ XUẤT] 3` chỉ số, mỗi chặng video → bấm → đăng ký có ≥ 1 chỉ số, cột nguồn đọc không trống |
| F4 | Quà truy nguồn | Quà chọn có bảng hai đoạn chữ (kịch bản ↔ mô tả quà); hoặc `[CẦN NGUỒN: quà khớp đề tài này]` và hạ B1 |
| F5 | Không số bịa | Ô «Số đo» trống hoặc mang `[SỐ LIỆU]` kèm nguồn, ngày |
| F6 | Lạnh thì không bán | Mức `lanh` ⇒ không từ bán (`khung-loi-moi.md` mục 5) ở bất kỳ chỗ nào của tệp, kể cả bảng |

### D7. Ghi tệp

Cùng một tệp `ho-so-kenh/goi/<ma>-loi-moi.md`, đổi dòng đầu khuôn thành `che-do: duong-day-du`, và thêm ba mục sau mục 3 của khuôn thường (đánh số lại các mục sau):

````markdown
## 3b. Bốn chỗ đặt lời mời (cùng một hành động, cùng một đích)

Chỗ mo-ta: <một dòng + đường dẫn có tham số>
Chỗ ghim: <một dòng + đường dẫn có tham số>
Chỗ man-hinh-ket-thuc: <tên đích ngắn>

## 3c. Chọn quà theo đề tài

| Đoạn kịch bản (số dòng) | Câu người dùng mô tả quà | Kết luận |
|---|---|---|
| "<câu nguyên văn>" [TRÍCH] | "<câu nguyên văn>" [TRÍCH] | Khớp [SUY LUẬN] | Không khớp ⇒ [CẦN NGUỒN: quà khớp đề tài này] |

## 3d. Bảng đường đi

(bảng ở mục D5; ô số để trống khi mới tạo)
````

Dòng `Dòng mô tả/ghim:` của khuôn thường được **thay** bằng ba dòng `Chỗ …:` ở mục 3b; trong tệp chế độ này không có dòng `Dòng mô tả/ghim:`.

Bàn giao: đưa bảng ở mục 3d cho `10x-yt-doc-so` khi người dùng đã có số (tệp `nhat-ky-thu.md` do `doc-so` ghi; skill này không ghi vào đó).

## Kiểm máy của chế độ này

| Kiểm máy | Đọc | Xanh khi |
|---|---|---|
| `KM-lm-4` | Mục 3d: các dòng chỉ số; mục 3b: các đường dẫn | ≥ `[ĐỀ XUẤT] 3` dòng chỉ số có tên chỉ số + nguồn đọc; mọi đường dẫn chứa `utm_` (đủ ba tham số); cả bốn chỗ đặt có mặt |
| `KM-lm-1` (LM-3 không bắt buộc, nhưng giữ) | Số dòng bắt đầu `Lời mời:` | Đúng 1 |
| `KM-lm-2` | Tên quà, tên offer, đường dẫn gốc (trước dấu `?`) | Có trong chữ người dùng đưa |
