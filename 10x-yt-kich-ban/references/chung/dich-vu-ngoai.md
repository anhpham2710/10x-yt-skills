# Bảng dịch vụ ngoài và đường miễn phí

Bộ skill chạy được trọn vẹn với **đường mặc định**: người dùng chép tay, xuất từ YouTube Studio, hoặc tự chạy `yt-dlp` tại máy. Cột «tuỳ chọn» chỉ để người dùng đã có sẵn công cụ đó dùng cho nhanh. Skill không bao giờ bắt mua, không tạo tài khoản hộ, không gửi dữ liệu ra ngoài ngầm.

## 1. Luật khi gọi một dòng của cột «tuỳ chọn»

Skill nào muốn dùng một dòng của cột «tuỳ chọn» phải:

1. **Khai** trong mục «An toàn và phạm vi» của SKILL.md (xem `an-toan.md`).
2. **Hỏi người dùng trước khi gọi**, nói rõ dữ liệu nào đi đâu và có tốn phí không.
3. **Chạy được trọn vẹn khi người dùng từ chối.** Từ chối thì rơi về đường mặc định, không cắt bớt việc.

Skill chỉ làm hộ khi người dùng đã tự cài, tự đăng nhập hoặc tự đưa khoá vào công cụ của họ. Skill không đọc, không in khoá.

## 2. Bảng

| Việc | Đường mặc định (miễn phí, thủ công) | Tuỳ chọn | Trả phí? | Dữ liệu đi đâu |
|---|---|---|---|---|
| Danh sách video và lượt xem của kênh khác | Mở trang kênh, chép tiêu đề, ngày đăng, lượt xem vào bảng CSV (mẫu: `mau-so-video.csv`) | `yt-dlp --flat-playlist -J` do người dùng tự cài và tự chạy tại máy | Không (`yt-dlp` là phần mềm nguồn mở) | Máy người dùng ↔ YouTube |
| | | vidIQ (nếu người dùng đã có tài khoản) | **Có**, theo credit. Hai công cụ outlier và kênh tương tự của vidIQ đo thấy không dùng được cho tiếng Việt (đo của 10X ngày 30/07), nên không đặt vào đường chính | vidIQ |
| | | YouTube Data API v3 | Miễn phí theo hạn mức, nhưng cần dự án Google Cloud và khoá. Không khuyên cho chuyên gia vì ngưỡng kỹ thuật | Google |
| Transcript | Người dùng chép «Hiện bản chép lời» trên YouTube, hoặc dán | `yt-dlp` lấy phụ đề; Whisper chạy tại máy | Không | Máy người dùng |
| | | Dịch vụ lấy transcript bằng khoá (TranscriptAPI, TranscriptOut, getyoutubetranscript…) | **Có**, và có dịch vụ bắt agent tự đăng ký tài khoản bằng email ⇒ **không dùng** | Nhà cung cấp |
| Bình luận | Chép từ trang video hoặc từ YouTube Studio (kênh của mình) | Bình luận trong vidIQ (nếu đã có) | **Có** (vidIQ) | vidIQ |
| | | Dịch vụ cào dữ liệu (Apify…) | **Có** và là cào dữ liệu người khác ⇒ **không dùng** | Apify |
| Số kênh của mình | YouTube Studio → chế độ nâng cao → xuất tệp, hoặc chép tay vào `so-video.csv` | — | Không | Tại máy |
| Cầu tìm kiếm | Gõ vào ô tìm kiếm YouTube và đọc gợi ý; Google Trends. Người dùng tự đọc số, skill ghi `[SỐ LIỆU]` kèm ngày | Claude in Chrome đọc trên Chrome của người dùng (hỏi trước, chỉ đọc youtube.com) | Không | Máy người dùng ↔ YouTube |
| | | Điểm từ khoá của vidIQ: điểm 0–100, không phải lượt tìm. Không phải bằng chứng cầu, không thay đường Chrome/tay; không lấy số từ lớp phủ vidIQ làm số YouTube gốc | vidIQ có | vidIQ |
| Thumbnail | Canva bản miễn phí hoặc ảnh chụp từ chính video | Dịch vụ sinh ảnh AI (Higgsfield, Gemini…) | **Có** (chạy theo credit, và ảnh mặt người dùng bị tải lên nhà cung cấp) | Nhà cung cấp |
| Dịch phụ đề hoặc bình luận | Không mặc định | Google Translate | Không, nhưng **gửi chữ ra ngoài** ⇒ phải hỏi trước | Google |

## 3. Cách nói với người dùng

- Nói cái gì đi đâu và có tốn tiền không **trước** khi gọi, bằng một câu: «Việc này cần gửi 80 bình luận cho dịch vụ X và tính theo credit. Bạn có muốn dùng không, hay mình làm theo cách chép tay?».
- Không gợi ý mua công cụ trả phí như cách duy nhất. Có đường miễn phí thì nêu đường miễn phí trước.
- Người dùng từ chối: «Được, mình làm theo cách chép tay» rồi làm, không nhắc lại.

## 4. Nguồn gốc

Bảng này và ba luật ở mục 1 lấy từ bảng dịch vụ ngoài trong tài liệu thiết kế nội bộ của bộ skill YouTube, do 10X khảo sát các công cụ trên thị trường. Việc báo giá và phạm vi trước khi tạo tài khoản học từ `tubeagentkit/youtube-transcript-skills` (MIT). Xem `NGUON.md`.
