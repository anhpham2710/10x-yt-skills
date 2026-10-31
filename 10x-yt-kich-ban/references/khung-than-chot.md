# Khung thân và chốt: viết từng đoạn, giữ nhịp, nối sang video kế

Dùng ở Bước 4 (thân) và Bước 5 (chốt tập).

## 1. Bốn vai khi viết, không gộp làm một

Kịch bản viết qua bốn vai nối nhau. Mỗi vai một lượt, đừng làm cùng lúc:

| Vai | Làm gì | Không làm gì |
|---|---|---|
| **Gom** | Liệt kê hết chất liệu người dùng có, đánh số M1, M2… (Bước 1) | Không viết câu nào của kịch bản |
| **Viết** | Viết bản đủ theo dàn ý đã duyệt, không tự kiểm duyệt khi đang viết | Không thêm chất liệu mới; thiếu thì dùng `[CẦN NGUỒN]` |
| **Cắt** | Đọc lại, bỏ mọi câu không phục vụ lời hứa hoặc không giữ người xem; rút số từ | Không thêm ý mới ở lượt này |
| **Đọc** | Thêm cue cho người nói: chỗ ngắt, chỗ nhấn, cảnh chiếu, viết trong ngoặc tròn `( )` | Không đổi chữ, không paraphrase (việc đọc lên màn hình là của `10x-youtube-teleprompter-vn`) |

Vai **Soát** (chấm xem kịch bản có đạt không) **không thuộc skill này**. Soát là `10x-yt-soat`, chạy ở lượt khác, vì người viết tự chấm mình luôn thấy mình đạt.

Cách vai **Gom, Viết, Cắt, Đọc** tách ra học từ kỹ năng `10x-youtube-script-body-vn` của 10X (cái ý «bốn vai», viết lại).

## 2. Một đoạn thân gồm ba lớp rồi một cái nối

```
Ý        một câu, nói thành lời được
Bằng chứng   số, lời khách, kết quả đo, bước làm: lấy từ kho chất liệu
Ví dụ        một chuyện, một cảnh, một ca cụ thể: lấy từ kho chất liệu
Nối      một câu đẩy người xem sang đoạn sau
```

Ba lớp này là khuôn Ý → Bằng chứng → Ví dụ (học từ kỹ năng `10x-youtube-script-body-vn`, trong đó gọi là Luận điểm → Bằng chứng → Ví dụ).

Luật cho từng đoạn:

1. **Ý** chỉ một câu. Hai ý thì tách thành hai đoạn.
2. **Bằng chứng và Ví dụ** đều phải trỏ về một mục M của kho chất liệu hoặc một D của bảng dữ kiện. Đoạn nào không trỏ được thì xử lý theo **Luật chất liệu** trong `SKILL.md`.
3. **Nói** là gạch đầu dòng **nói được thành lời**, câu ngắn, một hơi một câu. Không viết văn để đọc: nếu đọc lên thấy giống bài báo thì viết lại. Mỗi gạch một câu hoặc một ý ngắn.
4. **Số và tên** trong lời nói mang dấu `[D#]` ngay sau nó (xem mục 4).
5. Một đoạn chỉ phục vụ một việc. Không có việc thì đoạn đó không tồn tại: bỏ.

Số đoạn thân: `[ĐỀ XUẤT]` 3 đến 5 đoạn, chỉnh theo độ dài video người dùng định quay. Đây là ước lượng, không phải luật.

## 3. Cái nối: mở vòng, ngắt nhịp, nhắc lý do

Mỗi đoạn kết thúc bằng **đúng một** trong ba loại nối. Mục đích là người xem có lý do chờ đoạn sau.

| Loại | Là gì | Ví dụ dáng câu |
|---|---|---|
| **Mở vòng** | Hứa một điều sẽ có ở đoạn sau, rồi giữ lời | «Lát nữa mình chỉ chỗ thứ hai, chỗ này nhiều người bỏ sót.» |
| **Ngắt nhịp** | Đổi nhịp đột ngột: một câu hỏi, một cảnh chiếu, một im lặng | «Bạn thử đoán mình đã bỏ những gì.» |
| **Nhắc lý do** | Quay lại lời hứa ở đầu: video này đang đi đến đâu | «Vẫn là chuyện hôm nay: sửa cái slide này thành một ý.» |

Luật:

- **Mở vòng phải đóng.** Đoạn nào hứa «lát nữa mình chỉ…» thì đoạn sau đó phải chỉ. Mở mà không đóng là bẫy người xem.
- Nối là câu **thật sự có thông tin**. Không dùng «hãy ở lại đến cuối video» hay «đừng bỏ qua phần sau»: câu rỗng, không cho người xem lý do.
- Đã có đường giữ chân của video trước (`khung-hook.md`, mục 6): đặt nối mạnh nhất ngay trước điểm kênh hay tụt.
- Không có con số «mỗi bao nhiêu phút phải có một điểm ngắt» trong skill này. Con số đó trong tài liệu cũ không có nguồn kiểm được (`references/chung/da-bi-bac.md`). Nhịp thật của kênh sẽ được đọc từ số đo ở `10x-yt-doc-so`.

## 4. Số, tên và bảng dữ kiện

Một số hoặc một tên riêng không có nguồn là chỗ kịch bản bịa dễ nhất, và người nghe sẽ tin vì nó nói ra bằng giọng chuyên gia.

**Cái gì là «dữ kiện» cần dấu `[D#]`:**

- Con số mang thông tin: số lượng đo hoặc đếm (khách, học viên, bài), năm kinh nghiệm, tiền, phần trăm, thứ hạng, thời hạn, số lần.
- Tên riêng: tên người, tên khách, tên kênh, tên công ty, tên công cụ, tên sách, tên địa danh.
- Một trích dẫn lời người khác.

**Cái gì không phải dữ kiện (không cần dấu):** mạo từ «một ý», «một câu», «một hình»; số đếm chính **cấu trúc nói** của bạn khi bạn đang liệt kê (khi nói «có ba chỗ dễ sai» rồi nêu đủ ba chỗ). Nhưng: số cấu trúc viết **bằng chữ**, và đếm lại cho khớp số mục bạn thực sự nêu. Đừng viết «3 chỗ» bằng chữ số trong phần nói, vì lệnh kiểm sẽ coi đó là một con số cần nguồn.

**Cách ghi:**

1. Trong phần lời nói, ngay sau số hoặc tên, đặt `[D1]`, `[D2]`… theo thứ tự xuất hiện.
2. Bảng ở mục 5 của tệp kịch bản có **một dòng cho mỗi D**: dữ kiện đúng như viết trong lời nói, nhãn (`[SỐ LIỆU]` hoặc `[TRÍCH]`, xem `references/chung/nhan-nguon.md`), **nguyên văn câu chứa nó trong chất liệu** (chép đúng từng chữ), và mã M của chất liệu.
3. **Chép lại nguyên văn là bắt buộc**, không phải trang trí. Không chép được nguyên văn nghĩa là chất liệu không có số/tên đó, tức là số/tên đó đang đến từ trí nhớ của model. Khi đó số/tên đó không được nằm trong lời nói.
4. Số làm tròn khác chất liệu (chất liệu nói «gần tám mươi», kịch bản nói «tám mươi») cũng là sai. Chép đúng mức người dùng đã nói.
5. Số từ thị trường, thuật toán, thị phần mà model nhớ được: **không dùng**. Xem `references/chung/da-bi-bac.md`.

## 5. Chốt tập: nối sang video kế

Chốt tập có bốn dòng, theo thứ tự:

1. **Tóm một câu:** video đã trả lời điều gì, cùng chữ với lời hứa của gói. Không thêm lời hứa mới.
2. **Video kế:** đề tài tiếp theo lấy từ `de-tai.md` (đề tài `treo` truy được cùng nguồn hoặc nối thẳng với câu hỏi mở của video này). Ghi mã và tên. Không có đề tài kế nào trong sổ thì ghi `chua-co-de-tai-ke` và **không bịa tên video**: cầu nối chỉ dựa vào câu hỏi mà video này mở ra mà chưa trả, ghi `[TÔI THÊM]`, và nhắc người dùng chạy `10x-yt-de-tai` để có đề tài kế.
3. **Cầu nối:** câu nói ra, dẫn từ điều vừa trả sang điều video kế sẽ trả. Nó phải cho người xem một lý do cụ thể để bấm tiếp, không phải «xem thêm video khác của kênh».
4. **Lời mời:** một dòng. Xem mục 6.

Rồi hai dòng ghi chú cho người quay và người dựng (không nói ra):

5. **Căn cứ video kế:** vì sao chọn tập này, kèm nguồn. Ưu tiên dữ liệu người xem có thật: câu nguyên văn trong `binh-luan.md` hỏi đúng điều tập kế trả (`[TRÍCH]`), hoặc lượt xem của video cùng đề tài trong `so-video.csv`. Không có thì chép cột truy nguồn của dòng đó trong `de-tai.md` và nói thẳng «chưa có dữ liệu người xem». Không bịa lượt xem hay lời của người xem.
6. **Màn hình cuối:** màn hình cuối trỏ sang đúng tập ở `Video kế:` (ghi tên), và chừa vài giây cuối không nói điều quan trọng. Chữ và cách cài trong YouTube Studio do `10x-yt-dang` làm.

Có `chua-co-de-tai-ke` thì bỏ dòng 5 và 6.

Mục tiêu của chốt tập là xếp các video thành chuỗi: người xem hết một video thì có việc tiếp theo muốn làm. Đây là phần giữ người xem ở lại kênh, nên không bỏ.

## 6. Lời mời: một dòng, khớp với việc kênh đang làm được

- Lời mời có **ba nguồn hợp lệ**: (a) dòng do skill `10x-yt-loi-moi` đã sinh và người dùng đã lưu, (b) một câu do chính người dùng viết khi được hỏi, (c) `[CẦN NGUỒN: lời mời]` và chỉ sang `10x-yt-loi-moi`. Skill này **không tự nghĩ ra ưu đãi, quà tặng, giá, khoá học** của người dùng.
- `kenh.md` ghi **chưa có sản phẩm bán**: lời mời chỉ được là bước tiếp theo trong kênh (xem video kế, đăng ký, để lại một câu hỏi). Không bán, không dẫn tới trang bán, vì họ chưa có gì để bán.
- **Có sản phẩm bán**: lời mời có thể trỏ tới thứ người dùng đã nói là họ có. Mức mời **vừa với mức người xem đã được làm nóng** trong video này: video mới dạy một ý nhỏ thì mời nhẹ, không mời mua gói đắt. Chỗ này `10x-yt-soat` sẽ kiểm.
- Lời mời đứng **sau** cầu nối, không trước. Người xem nên được cho thứ họ cần rồi mới được mời.

## 7. Đã bỏ khỏi bản cũ

- Trỏ vào tệp tham chiếu `script-writing-guide.md` không tồn tại trong bản `10x-youtube-script-body-vn`. Đã bỏ; nội dung cần thiết nằm ở đây.
- «Retention marker mỗi 2 phút» và các con số nhịp tương tự: không nguồn, đã bỏ (xem mục 3).
- Phần CTA nằm trong thân kịch bản: chuyển thành đúng một dòng lời mời ở chốt tập, và phần thiết kế lời mời là việc của `10x-yt-loi-moi`.
