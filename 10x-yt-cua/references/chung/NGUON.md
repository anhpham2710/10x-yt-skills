# NGUON.md: ghi công nguồn của lớp chung và skill cửa

Phạm vi tệp này: `10x-yt-chung/` và `10x-yt-cua/`. Mỗi skill con của bộ có phần ghi nguồn riêng ở cuối `SKILL.md` của nó; khi thêm skill mới, thêm nguồn vào tệp này nếu có nguồn MIT mới.

## 1. Chuẩn license của gói

- **Gói YouTube OS bản bán** dùng **giấy phép riêng của 10X**, không dùng MIT, vì là hàng bán. Văn bản giấy phép do 10X cấp và đặt cạnh gói; tệp này không thay thế nó. `[CHỜ 10X: gắn văn bản giấy phép vào gói trước khi phát hành]`
- **Tệp này** ghi công những nguồn mã nguồn mở giấy phép MIT mà bộ học ý, theo yêu cầu của giấy phép MIT về ghi nguồn.
- **Nguồn không có giấy phép, giấy phép cấm thương mại, hoặc không rõ gốc** được xử lý theo cách **clean-room**: người viết chỉ đọc bản mô tả ý bằng lời, không mở bản gốc, không chép câu chữ nào.
- **Tài sản của 10X** (gói lệnh YouTube OS và các skill nội bộ) dùng thẳng, vì cùng chủ sở hữu.

## 2. Nguồn MIT: học ý, viết lại, ghi công

Không đoạn văn bản hoặc đoạn mã nào dưới đây được chép nguyên văn; tất cả viết lại bằng tiếng Việt hoặc viết lại độc lập. Nếu về sau có đoạn nào chép nguyên văn thì phải thêm dòng bản quyền gốc của repo đó vào đây. Số `sha` là phiên bản đã đọc khi nghiên cứu (24/10/2026).

| Nguồn | Giấy phép | Phiên bản đã đọc | Dùng ở đâu | Cái hay đã lấy |
|---|---|---|---|---|
| [Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) | MIT | `a2feb21` | `10x-yt-chung/tinh-median.py`, `da-bi-bac.md` | Bội số = lượt xem ÷ median của **chính kênh**; «median của dưới 4 video không phải median»; bỏ video quá mới. Script `tinh-median.py` viết lại độc lập từ ý này (người viết không mở mã `swipe.py` của họ) |
| [JimmySadek/video-fetcher-to-markdown](https://github.com/JimmySadek/video-fetcher-to-markdown) | MIT | `c196ba4` | `an-toan.md`, `lay-chu.md` | Khối khai báo «Operational boundaries» (mạng, tệp, tiến trình, thông tin xác thực, phụ thuộc); quy tắc coi phụ đề và chữ trong khung hình là nội dung không đáng tin; thứ tự lấy chữ «phụ đề có sẵn trước, công cụ tại máy sau và nói trước với người dùng»; gợi ý cho công cụ biết danh sách tên riêng |
| [tubeagentkit/youtube-transcript-skills](https://github.com/tubeagentkit/youtube-transcript-skills) | MIT | `8ea4c21` | `an-toan.md`, `dich-vu-ngoai.md` | Khối «Untrusted content» (gặp câu giống lệnh thì báo lại, không làm theo); khối «Scope» liệt kê chính xác nơi gọi tới; báo giá trước khi tạo tài khoản; không in khoá ra khung chat |
| [ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills) | MIT | `64ba7b4` | `nhan-nguon.md` (luật 7), `da-bi-bac.md` | Nhận xét rằng để model tự tính median trong đầu dễ sai; cỡ mẫu và độ tin ghi cạnh kết luận |
| [adityaarsharma/youtube-marketing-skills](https://github.com/adityaarsharma/youtube-marketing-skills) | MIT | `e9136cb` | `da-bi-bac.md` | **Chỉ để đối chiếu và loại.** Các con số về thẻ, thuật toán và hệ số lượt tìm trong tài liệu này không kiểm được nên bị liệt vào danh sách «đã bị bác»; không lấy ý nào về nội dung |

## 3. Tài sản của 10X (dùng thẳng)

| Tài sản nội bộ | Dùng ở đâu | Cái đã lấy |
|---|---|---|
| Gói lệnh `10x-youtube-os` (cửa duy nhất cho việc làm video, bản v0.4.0) và tệp `hop-dong-du-lieu.md` kèm gói | `10x-yt-cua`, `ho-so-kenh.md`, `an-toan.md` | Bước 0 đọc dữ liệu trước khi làm; ba trạng thái đủ/thiếu/trống; cổng chưa quay (3 đề tài treo thì không phát đề tài thứ tư); chỉ nạp tệp của chế độ đang chạy; luật cứng «thiếu dữ liệu thì nói thiếu, không lấp»; luật «chuyện thật chép nguyên, cấm tô»; khuôn sổ video với ba trạng thái. Đã thay hợp đồng tên tệp theo giáo án cũ bằng thư mục `ho-so-kenh/` |
| Skill `phan-tich-video-youtube-doi-thu` | `nhan-nguon.md` | Bộ nhãn `[SỐ LIỆU] [TRÍCH] [SUY LUẬN] [CẦN NGUỒN]` và luật «không đo được thì ghi chưa đo». Đã bỏ danh tính và đường dẫn kho cá nhân của tác giả |
| Skill `10x-youtube-niche-idea-vn` (Confirm Gate) | `cong-thi-truong.md` | Chốt thị trường và ngôn ngữ trước mọi nghiên cứu, cổng chặn lệch thị trường–ngôn ngữ |
| Skill `10x-youtube-script-from-wiki-vn` | `10x-yt-cua` | Vòng «đóng gói trước, kịch bản sau» có cổng chặn; gọi skill con thật thay vì tự phịa; dừng cho người dùng duyệt sau mỗi skill con |
| Skill `10x-yt-summary-vn` (bản lưu trữ) | `lay-chu.md` | Luật «lấy chữ lỗi thì dừng và xin dán, không tóm tắt chữ lỗi» |

## 4. Nguồn clean-room: chỉ học ý, không mở bản gốc

| Nguồn | Lý do clean-room | Cái ý đã lấy (viết lại hoàn toàn) | Dùng ở |
|---|---|---|---|
| Skill `10x-video-marketing-28-vn` (nội bộ 10X, bản ghi «không thương mại, không đóng gói») | License nội bộ cấm đóng gói và bán | Ý «giữ trạng thái tiến độ và cổng đạt/trượt không cho nhảy bước» | `10x-yt-cua` (khối cổng và `TIEN-DO`) |

Người viết lớp chung và skill cửa chỉ đọc bản mô tả ý ở trên, không mở nội dung skill gốc ở dòng này khi viết.

## 5. Không dùng

Các dịch vụ và công cụ bị loại khỏi đường chính (trả phí hoặc tự đăng ký tài khoản bằng email, cào dữ liệu) được liệt kê ở `dich-vu-ngoai.md` cùng lý do. Không có mã hay câu chữ nào của chúng nằm trong bộ này.
