# Bộ 10 câu kiểm kích hoạt của `10x-yt-cua`

Dùng để đối chiếu `description` trong `SKILL.md`: câu việc YouTube phải trúng cửa, câu ngoài lề không. Đây là bộ tự kiểm do người viết skill soạn. Bộ chính thức của kế hoạch test (10 câu cố định, tiêu chí đạt từ 9/10 `[ĐỀ XUẤT]`) sẽ nằm ở `_test/du-lieu/kich-hoat.md` khi vé dữ liệu test làm xong; khi đó đối chiếu lại `description` với bộ chính thức và giữ tệp này như bản dự phòng.

Cách đối chiếu: với mỗi câu, hỏi «description có nêu việc này ở phần *Dùng khi*, hoặc việc này thuộc nhóm *KHÔNG dùng cho* không?».

## Năm câu phải TRÚNG cửa

| # | Câu người dùng | Vì sao trúng | Cụm trong description |
|---|---|---|---|
| 1 | «Tuần này mình nên làm video gì cho kênh YouTube?» | Việc chung, chưa chỉ định bước; cần đọc hồ sơ rồi chọn một việc | «video tuần này nên làm gì» |
| 2 | «Mình mới bắt đầu làm kênh YouTube, bắt đầu từ đâu?» | Chưa có hồ sơ; vào chế độ bắt đầu | «bắt đầu làm kênh YouTube», «chế độ bắt đầu để tạo kenh.md» |
| 3 | «Làm video tiếp theo đi» (đang có `ho-so-kenh/`) | Xin việc chung kế tiếp, đúng nhiệm vụ cửa | «làm video tiếp theo đi» |
| 4 | «Hồ sơ kênh YouTube của mình đã đủ chưa, bước kế tiếp là gì?» | Hỏi trạng thái và bước kế tiếp | «hồ sơ kênh YouTube», «đang ở bước nào» |
| 5 | «Mình hết ý tưởng video YouTube rồi» | Xin đề tài; cửa kiểm cổng chưa quay rồi chỉ đường | «hết ý tưởng video YouTube» |

## Năm câu KHÔNG được trúng cửa

| # | Câu người dùng | Vì sao không | Cụm trong description |
|---|---|---|---|
| 6 | «Viết giúp mình bài Facebook kể chuyện về một khách hàng» | Bài đăng mạng xã hội, không phải kênh YouTube | «KHÔNG dùng cho bài đăng Facebook…» |
| 7 | «Làm slide bài giảng 16:9 cho buổi đào tạo ngày mai» | Slide giảng dạy | «slide hoặc giáo án bài giảng» |
| 8 | «Dựng landing page bán khoá học của mình» | Trang bán hàng | «landing page» |
| 9 | «Tóm tắt giúp mình video YouTube này: <đường dẫn>» | Video của người khác, không phải việc làm kênh của họ (câu dễ nhầm vì có chữ YouTube) | «tóm tắt hay dịch video YouTube của người khác» |
| 10 | «Giải thích giúp mình hàm VLOOKUP trong Excel» | Hoàn toàn ngoài lề | (không nêu trong phần *Dùng khi*) |

## Kết quả đối chiếu (người viết, ngày viết cửa)

Đối chiếu bằng mắt từng câu với phần *Dùng khi* và *KHÔNG dùng cho* của `description`: 5/5 câu YouTube có cụm khớp, 5/5 câu ngoài lề không có cụm khớp hoặc rơi vào nhóm loại trừ. Đây là kiểm bằng đọc, chưa phải chạy thật với model; số đo thật là việc của `CUA-K` trong kế hoạch test.

Điểm cần theo dõi khi chạy thật:

- Câu 9 là câu dễ nhầm nhất (có chữ YouTube, có link). Nếu model kích hoạt cửa cho câu này thì thêm vào *KHÔNG dùng cho* một cách nói cụ thể hơn, không nới *Dùng khi*.
- Trong thời gian các skill `10x-youtube-*` cũ còn chạy song song, một câu như «đặt tiêu đề YouTube» có thể kích hoạt cả skill cũ lẫn cửa. Cửa chỉ nhận khi người dùng xin việc chung hoặc cần định hướng; việc đã rõ là việc của skill con (description đã nói).
