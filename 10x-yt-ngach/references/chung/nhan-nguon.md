# Nhãn nguồn: chống bịa trong mọi đầu ra

Mỗi con số, mỗi câu trích và mỗi nhận định trong đầu ra của bộ `10x-yt-*` phải mang một nhãn cho biết nó từ đâu ra. Không nhãn thì người đọc không phân biệt được «dữ liệu thật» với «máy nghĩ ra cho trôi», và người dùng chuyên gia không có cách tự phát hiện (xem `an-toan.md`, mục chuyện thật).

## 1. Năm nhãn

| Nhãn | Dùng khi | Điều kiện để được gắn |
|---|---|---|
| `[SỐ LIỆU]` | Con số đọc từ nguồn người dùng đưa hoặc tính bằng script | Ghi kèm nguồn và ngày: «`[SỐ LIỆU]` 41.000 lượt xem, kênh X, ghi ngày 2026-10-24, từ bảng người dùng dán». Số tính bằng `tinh-median.py` ghi «tính bằng tinh-median.py» |
| `[TRÍCH]` | Câu nguyên văn của người thật (bình luận, câu người dùng kể, tiêu đề video) | Chép đúng từng chữ, đặt trong dấu ngoặc kép, kèm nguồn (video nào, bình luận của ai khi biết). Không sửa chính tả, không rút gọn giữa câu |
| `[SUY LUẬN]` | Điều rút ra từ `[SỐ LIỆU]` hoặc `[TRÍCH]` | Nêu rõ suy ra từ dòng nào. Là giả thuyết cho tới khi có số đo lại |
| `[CẦN NGUỒN]` | Điều cần là sự thật nhưng chưa có dữ liệu | Không được dùng làm cơ sở cho một quyết định. Nói luôn chỗ nào tra được |
| `[TÔI THÊM]` | Ý do skill đề nghị, không có trong dữ liệu của người dùng | Nói rõ đây là đề nghị, chưa có bằng chứng, người dùng có quyền bỏ |

## 2. Luật dùng

1. **Không đo được thì ghi «chưa đo».** Không điền số ước chừng cho đẹp bảng. Ô trống trong dữ liệu người dùng nghĩa là chưa đo, không phải 0.
2. **Trường vắng không phải bằng 0.** Một video không có cột CTR nghĩa là chưa có CTR của video đó, không phải CTR 0%.
3. **Mọi nhận định về nhóm phải có ít nhất `[ĐỀ XUẤT] 3` câu `[TRÍCH]` từ những người khác nhau** khi nói «nhiều người xem nói rằng…». Một người ồn không phải một nhóm.
4. **Ghi cỡ mẫu và độ tin** cạnh mọi kết luận từ tập dữ liệu: «n = 120 bình luận, độ tin trung bình (mẫu nhỏ, chỉ lấy theo "hàng đầu")».
5. **Câu «chắc là người xem cần» tự động rớt.** Đó là suy đoán không nhãn. Viết lại thành `[SUY LUẬN]` kèm dòng nguồn, hoặc bỏ.
6. **Số do model tự nhớ không phải `[SỐ LIỆU]`.** Con số về thuật toán, lượt tìm, CPM, thị phần mà model nhớ từ huấn luyện phải gắn `[CẦN NGUỒN]` hoặc bỏ. Danh sách con số đã bị loại ở `da-bi-bac.md`.
7. **Tính toán thì dùng script.** Median và bội số tính bằng `tinh-median.py`, không tính nhẩm. Model tính nhẩm median từ vài chục số dễ sai và sai im lặng.
8. **Tên người, tên kênh, tên công cụ** chỉ được nêu khi đọc được trong dữ liệu người dùng đưa. Không nhớ từ huấn luyện rồi viết như sự thật.
9. **Mọi thứ do skill sinh ra là giả thuyết** cho tới khi video được đăng và có số. Nói điều đó một lần ở đầu ra đầu tiên của mỗi phiên, đừng để người dùng tưởng là đáp án.

## 3. Ví dụ ngắn

Sai:

> Video này chắc chắn sẽ đạt 100.000 lượt xem vì chủ đề đang hot.

Đúng:

> `[SỐ LIỆU]` Ba video gần nhất của kênh X cùng chủ đề đạt 3,1×, 2,4× và 4,0× median của kênh (tính bằng tinh-median.py, ngày quét 2026-10-24, n = 11 video).
> `[SUY LUẬN]` Chủ đề này có cầu ở mức cao hơn trung bình kênh X. Chưa chứng minh được kênh bạn sẽ đạt mức tương tự; đây là giả thuyết để đo lại sau 3 video.

## 4. Nguồn gốc

Khung nhãn dựa trên bộ nhãn `[SỐ LIỆU] [TRÍCH] [SUY LUẬN] [CẦN NGUỒN]` trong quy trình phân tích video đối thủ của 10X (tài sản nội bộ của chủ gói). Nhãn `[TÔI THÊM]` lấy từ gói lệnh YouTube OS của 10X. Cách chọn tên và luật 1, 2, 3 và 6 viết lại độc lập cho bộ này; không chép từ nguồn ngoài. Xem `NGUON.md`.
