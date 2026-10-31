# Hai mục tiêu nguồn view: viết khác nhau chỗ nào

Tệp này dùng ở Bước 2 của `SKILL.md`. Người dùng chọn mục tiêu cho **từng video**; skill giải thích hai hướng bằng chữ người thường rồi viết theo hướng họ chọn.

## 1. Hai người xem, hai lúc

| | **Tìm kiếm** (`tim-kiem`) | **Đề xuất và trang chủ** (`de-xuat-trang-chu`) |
|---|---|---|
| Người xem là ai lúc thấy video | Người **đang gõ** một câu hỏi hoặc một việc cần làm vào ô tìm kiếm | Người **đang lướt**, chưa gõ gì, thấy video được gợi ý cạnh một video khác hoặc ở trang chủ |
| Cái kéo họ bấm vào | Video **đúng chữ họ gõ**: tiêu đề, hai câu đầu mô tả, tên chương khớp câu hỏi của họ | Lời hứa và hình ảnh của gói tiêu đề với thumbnail (việc của `10x-yt-dong-goi`); mô tả đóng vai phụ |
| Mô tả phải làm gì | Cho thấy video **trả lời đúng câu hỏi đó**, bằng chữ của họ | Cho người đã bấm vào hoặc đang cân nhắc thấy **chuyện, mâu thuẫn, thứ mang đi**, không cần chữ tìm kiếm |
| Hợp với loại đề tài | Đề tài là một câu hỏi hoặc một việc («cách làm X», «X là gì») | Đề tài là chuyện, góc nhìn, phát hiện, hoặc video nằm trong một chuỗi |

Hai dòng cuối của cột phải là `[SUY LUẬN]` của skill, không phải số đo. Skill **không** nói nguồn nào mang nhiều lượt xem hơn, **không** nói YouTube «ưu tiên» thứ gì; mọi tỉ lệ nguồn view chỉ đọc từ YouTube Studio của chính kênh (`references/chung/da-bi-bac.md`).

## 2. Bảng «viết khác» (đây là thứ giám khảo so DA-1 với DA-2)

| Phần | `tim-kiem` | `de-xuat-trang-chu` |
|---|---|---|
| Hai câu đầu mô tả | Chứa **nguyên văn** một cụm tìm kiếm thật, đặt trong câu đọc trơn. Nói video giải quyết việc gì và cho ra gì | Khoảnh khắc, chuyện hoặc mâu thuẫn video mở ra; câu 2 là thứ người xem mang đi. **Không nhồi cụm** |
| Đoạn trả lời thẳng | Câu hỏi là cụm tìm kiếm (hoặc dạng câu hỏi của nó) | Câu hỏi người xem hỏi **sau** khi xem xong (lấy `[TRÍCH]` từ bình luận nếu có) |
| Tên chương | Dùng chữ người xem gõ khi đúng ý đoạn | Theo mạch chuyện; đoạn có cú lật thì tên chương **không lộ** cú lật nếu bản quay còn giữ nó |
| Thẻ | 3–5 thẻ đúng cụm (kể cả biến thể chính tả) + 3–5 liên quan | Vẫn 6–12 thẻ nhưng thiên về chủ đề và chữ trong bản quay; vai trò nhỏ |
| Câu ghim | Một câu hỏi mở + một hai mốc chương chứa chữ người xem tìm | Một câu hỏi mở + lời dẫn sang tập kế |
| Màn hình kết thúc | Trỏ tập kế như thường | Trỏ tập kế, nhấn mạnh việc **xem tiếp**; nên có tập kế thật |

## 3. Cách hỏi người dùng

Hỏi đúng một câu (xem Bước 2). Họ phân vân thì nói thứ bạn đọc được:

- Có cụm tìm kiếm **có số và ngày đọc** trong `ngach.md` sát đề tài video ⇒ «đề tài này có chữ người xem gõ; hướng tìm kiếm có cơ sở» `[SUY LUẬN]`.
- Đề tài là chuyện hay góc nhìn, không có cụm khớp ⇒ «chưa thấy ai gõ câu này; hướng đề xuất hợp hơn, và mô tả sẽ không nhồi chữ tìm kiếm» `[SUY LUẬN]`.
- Họ muốn **cả hai** ⇒ chọn **một** làm mục tiêu chính cho lượt này, ghi vào tệp; nói rõ chọn cả hai thì `10x-yt-doc-so` không biết mô tả đã nhắm vào đâu để đo. Muốn thử cả hai ở hai video khác nhau thì làm hai lượt.

## 4. Vì sao phải ghi `muc-tieu-nguon-view` ở đầu tệp

`10x-yt-doc-so` đọc số theo nguồn (tìm kiếm, đề xuất, trang chủ) trong YouTube Studio của người dùng và so với mục tiêu **đã ghi ở đây**. Không ghi thì không đo được «đã nhắm đúng chưa». Skill này chỉ ghi mục tiêu; **không** đọc số, **không** kết luận gói đăng đã thành công hay chưa.

## 5. Nguồn gốc

Ý tách «người đang gõ» và «người đang lướt», cùng việc chọn nguồn theo từng video, viết lại độc lập cho bộ này. Ý «trước khi bấm vào / sau khi bấm vào» có nền ở skill `10x-youtube-dna-algo-vn` của 10X (tài sản nội bộ); các khẳng định thuật toán, hệ số và ngưỡng đăng ký trong skill đó **không** được mang sang (xem `references/chung/da-bi-bac.md`).
