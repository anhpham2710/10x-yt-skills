# KHÔNG PHÁT HÀNH: thư mục này không thuộc gói bán

Thư mục `references/duong-day-du/` chứa chế độ **«đường đầy đủ»** của skill `10x-yt-loi-moi`: dựng đường đo được từ video, qua quà, qua danh sách, tới offer. Chế độ này chỉ dành cho **kênh của chủ bộ skill** và cho sản phẩm đào tạo khác của họ.

**Quyết định (câu hỏi 1 của thiết kế 03, chủ bộ skill đã chốt Q1):** gói bán (PAID) chỉ mang chế độ «một dòng». Phần dựng đường lead không được lọt vào gói bán.

## Cách loại khỏi gói bán

1. Khi đóng gói bán, **xoá nguyên thư mục** `skills/10x-yt-loi-moi/references/duong-day-du/`. `SKILL.md` và các tệp còn lại chạy đúng khi thiếu thư mục này (đã viết sẵn: thiếu tệp thì chế độ «đường đầy đủ» không tồn tại, ⛔ 2).
2. Kiểm gói bán sau khi xoá: lệnh `ls skills/10x-yt-loi-moi/references` không được liệt kê `duong-day-du`, và `grep -rn "duong-day-du" <thư mục gói bán>` chỉ được ra dòng trong `SKILL.md` và `references/mau-loi-moi.md` (các dòng đó chỉ nói chế độ này không có trong gói). Không dòng nào được chứa nội dung của chế độ.
3. Đề xuất cho vé đóng gói (ngoài phạm vi vé viết skill): cho script đóng gói bỏ qua đường dẫn này.

## Luật nội dung của thư mục này

- **Không chứa tên miền, đường dẫn, tên quà hay tên offer thật** của chủ bộ skill hay của ai. Mọi thứ đó phải lấy từ chữ người dùng đưa hoặc hồ sơ của họ, nếu chưa có thì `[CẦN NGUỒN]`.
- Không trỏ vào kho ghi chú hay thư mục riêng của chủ bộ skill.
- Mọi ví dụ trong thư mục này dùng ngoặc `< >` cho chỗ lấy từ chữ thật.
