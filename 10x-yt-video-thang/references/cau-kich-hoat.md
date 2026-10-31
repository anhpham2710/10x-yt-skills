# Bộ 10 câu kiểm kích hoạt của `10x-yt-video-thang`

Dùng để đối chiếu `description` trong `SKILL.md`: câu về video thắng của đối thủ phải trúng skill này, câu ngoài lề hoặc câu thuộc skill anh em thì không. Đây là bộ tự kiểm do người viết skill soạn; bộ chính thức của kế hoạch test sẽ nằm ở `_test/du-lieu/kich-hoat.md` khi vé dữ liệu test làm xong, khi đó đối chiếu lại.

Cách đối chiếu: với mỗi câu, hỏi «description có nêu việc này ở phần *Dùng khi*, hoặc việc này thuộc nhóm *KHÔNG dùng cho* không?».

## Năm câu phải TRÚNG

| # | Câu người dùng | Cụm trong description |
|---|---|---|
| 1 | «Video nào của mấy kênh đối thủ đang chạy tốt nhất?» | «đối thủ video nào đang chạy» |
| 2 | «Mình có bảng video của 4 kênh cùng ngách, tìm giúp video nào thắng.» | «tìm video outlier trong ngách», «video nào của kênh kia thắng» |
| 3 | «Vì sao video này của kênh kia nhiều view hơn hẳn các video còn lại của họ?» | «vì sao video này nhiều view», «mổ video thắng» |
| 4 | «Trong ngách này đối thủ chưa làm gì, mình có chỗ nào chen vào?» | «khoảng trống trong ngách», «đối thủ chưa làm gì» |
| 5 | «Nghiên cứu đối thủ trên YouTube giúp mình trước khi nghĩ đề tài.» | «nghiên cứu đối thủ trên YouTube» |

## Năm câu KHÔNG được trúng

| # | Câu người dùng | Skill đúng | Cụm trong description |
|---|---|---|---|
| 6 | «Giúp mình chốt ngách cho kênh YouTube.» | `10x-yt-ngach` | «chốt ngách hay chân dung người xem» |
| 7 | «Đọc 200 bình luận này xem người xem hay hỏi gì.» | `10x-yt-dao-binh-luan` | «đào bình luận» |
| 8 | «Đặt tiêu đề cho video mình sắp quay.» | `10x-yt-dong-goi` | «đặt tiêu đề hoặc làm thumbnail cho video của mình» |
| 9 | «Video tuần trước của mình ít view, sửa gì?» | `10x-yt-doc-so` | «đọc số của chính kênh mình» |
| 10 | «Tóm tắt giúp mình video này: <đường dẫn>» | (ngoài bộ) | «tóm tắt hay dịch video của người khác» |

## Kết quả đối chiếu (người viết)

Đối chiếu bằng mắt từng câu với phần *Dùng khi* và *KHÔNG dùng cho* của `description`: 5/5 câu phải trúng có cụm khớp, 5/5 câu không được trúng rơi vào nhóm loại trừ. Đây là kiểm bằng đọc, chưa phải chạy thật với model; số đo thật là việc của ca kích hoạt trong kế hoạch test.
