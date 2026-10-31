# Khung hook: cách mở video và chất liệu mỗi khung cần

Dùng ở Bước 2 (chọn khung cho dàn ý) và Bước 3 (viết hook). Hook là phần nói ra trong khoảng **20 giây đầu** (`[ĐỀ XUẤT]`, số của gói lệnh 10X, chưa kiểm bằng số đo), mục tiêu **không quá 60 từ** (`[ĐỀ XUẤT]`: 20 giây nhân khoảng 3 từ mỗi giây là nhịp nói tiếng Việt tự nhiên; số này cần đo lại trên video thật của kênh và chỉnh trước khi coi là chuẩn).

## 1. Hook làm đúng một việc

Người xem đã bấm vì tiêu đề và ảnh hỏi một điều. Hook trả lời điều đó **ngay**, rồi cho họ lý do ở lại. Hook không phải lời chào, không phải phần giới thiệu kênh, và không hứa điều gói chưa hứa.

Hook tốt trả lời được ba câu, theo thứ tự người xem tự hỏi:

1. **Có đúng thứ mình bấm vào không?** (khớp lời hứa của gói)
2. **Nói với mình không?** (nhận ra mình trong câu đầu)
3. **Người này có đáng tin không, và có đáng ở lại không?** (một dấu hiệu thật, không phải màn khoe)

## 2. Công thức hook cho video tiếng Việt

```
Lời hứa thẳng  +  Nhận ra người xem  +  Dấu hiệu đáng tin  +  «Đi vào luôn nào»
```

- **Lời hứa thẳng:** một câu nói điều video sẽ cho họ thấy hoặc biết, đúng chữ lời hứa trong `goi/<ma>.md`.
- **Nhận ra người xem:** gọi đúng người đang gặp chuyện đó. Ưu tiên chữ họ tự dùng, lấy từ `binh-luan.md` (chép nguyên, `[TRÍCH]`). Không có thì dùng `nguoi-xem.md`; không có cả hai thì viết trung tính và gắn `[CẦN NGUỒN]`, đừng nghĩ ra nỗi đau.
- **Dấu hiệu đáng tin:** một thứ **thật** từ kho chất liệu (một cảnh đang chiếu, một việc đã làm, một số đã đo). Không có thì bỏ phần này, đừng bù bằng danh xưng hay con số lấy từ trí nhớ.
- **«Đi vào luôn nào»:** câu chuyển cắt ngang mọi lời rào đón. Dùng cụm của riêng người nói nếu có.

Công thức này là hướng làm hook cho người xem Việt mà bộ skill đang dùng. Nó là `[SUY LUẬN]`: chưa kiểm bằng số của kênh nào. Kênh có `so-video.csv` thì sau vài video, `10x-yt-doc-so` sẽ đo xem hook kiểu này có giữ người xem hay không.

## 3. Bốn điều răn của hook

Bốn điều này là cách làm việc của bộ skill, viết lại bằng lời của bộ này. Ý của chúng đến từ tài liệu thiết kế (xem mục nguồn ở `SKILL.md`).

1. **Câu đầu đã mang giá trị.** Không mở bằng «xin chào các bạn», «trước khi vào video», «nhớ đăng ký». Chào hỏi và lời mời để sau.
2. **Hình, tiếng và chữ cùng nói một chuyện.** Hook đang nói về slide rối thì trên màn hình phải đang là slide rối. Ghi cảnh chiếu vào dòng `(cảnh chiếu)`.
3. **Rõ chủ đề trong một hơi.** Người xem nói lại được video này về cái gì sau câu thứ hai.
4. **Mở một câu hỏi mà thân video sẽ trả.** Hook mở vòng, thân đóng vòng. Hook chỉ trả lại đúng cú click, không kể hết.

## 4. Các khung mồi

Mỗi khung có cột **«Cần chất liệu gì»**. Quy tắc cứng: **chỉ gợi khung mà kho chất liệu của người dùng có thứ để lấp.** Khung nào chất liệu không đáp ứng thì không đưa vào danh sách phương án, và nếu nhắc tới thì chỉ nhắc một dòng «khung này cần X, bạn chưa có». Lý do: khung không có chất liệu thật sẽ khiến người viết (và model) bịa chuyện cho vừa khung, và đó là lỗi nặng nhất của kịch bản chuyên gia.

| Khung | Mở bằng | Cần chất liệu gì | Cạm bẫy |
|---|---|---|---|
| **Lời hứa thẳng** | Nói luôn điều video sẽ cho thấy | Chỉ cần lời hứa của gói | Dễ thành câu chung chung nếu không kèm cảnh hoặc chi tiết thật |
| **Cảnh đang diễn ra** | Chiếu hoặc kể thứ đang xảy ra: màn hình, sản phẩm, tờ giấy, cảnh làm việc | Một cảnh người dùng xác nhận sẽ quay (thường đã có ở `goi/<ma>.md` mục «câu hỏi 20 giây») | Mô tả cảnh mà chưa quay thì phải ghi `(cảnh chiếu)` là dự kiến |
| **Chuyện thật ngắn** | Một khoảnh khắc có thật, vài câu | Một chuyện người dùng đã kể, với chi tiết của họ | Cấm thêm chi tiết, cảm xúc, lời thoại họ chưa kể (`references/chung/an-toan.md`, mục 4) |
| **Sai lầm của chính mình hoặc của khách** | «Mình/khách mình từng làm sai chỗ này» | Một ca sai có thật | Không đổi tên khách nếu họ chưa đồng ý; dùng «một khách của mình» |
| **Con số của chính mình** | Một số người dùng đã đo, kèm cách đo | Một số có nguồn, ngày, phép đo | Không có số thật thì khung này **không được dùng**. Không bắc cầu bằng số ước chừng |
| **Câu người xem hỏi** | Dẫn nguyên câu hỏi người xem | Một câu `[TRÍCH]` từ `binh-luan.md` | Ít nhất `[ĐỀ XUẤT] 3` bình luận cùng ý mới được nói «nhiều người hỏi»; một câu thì chỉ nói «có người hỏi» |
| **Đối chiếu trước và sau** | Hai thứ cạnh nhau: rối và gọn, sai và đúng | Hai thứ thật để chiếu | Cặp giả dựng cho đẹp là bịa. Dựng lại cảnh thật thì ghi rõ «dựng lại» |
| **Cái giá của việc bỏ qua** | Đối tượng, điều họ muốn đạt, và điều họ mất nếu làm sai | Một hậu quả có thật, người dùng đã thấy hoặc có nguồn | Lĩnh vực nhạy (sức khoẻ, tiền bạc, pháp lý): không hù doạ, không hứa chữa, nói cái cần kiểm (xem `references/chung/an-toan.md`, mục 4 và luật của `10x-yt-dong-goi`, bước 5.4) |

Gợi ý khi chọn: khung **tốt nhất** là khung trả lời đúng cú click bằng chất liệu **mạnh nhất** người dùng có. Không chọn khung chỉ vì nó nghe hay.

Muốn thêm khung thì thêm vào bảng này kèm cột «Cần chất liệu gì». Khung nào không viết được cột đó thì chưa đủ điều kiện vào bảng.

## 5. Phương án và lựa chọn

- Viết **tối đa 6 phương án** hook, **mỗi khung một phương án**, chỉ từ các khung đã qua quy tắc chất liệu. Chất liệu chỉ cho hai khung thì chỉ có hai phương án; nói thẳng như vậy, đừng độn cho đủ sáu.
- Chọn **một** phương án, kèm lý do bằng một câu. Lý do phải so với **lời hứa của gói**, không so với «nghe hay hơn». Phương án còn lại ghi ở mục 7 của tệp kịch bản.
- Đếm từ của hook được chọn. Quá mục tiêu thì cắt, đừng nói nhanh hơn.

## 6. Hook gặp đường giữ chân của video trước

Nếu `nhat-ky-thu.md` hoặc `so-video.csv` cho biết video trước của kênh **rò ở đâu**, nối với ba kiểu rò (cách phân loại học từ kỹ năng `yt-retention` của Jake, giấy phép MIT, viết lại):

| Kiểu rò | Dấu hiệu | Hook của video này nên |
|---|---|---|
| **Rò ngay đầu** | Người xem đi gần hết trong những giây đầu | Bỏ mọi lời rào đón; nói lời hứa và chiếu cảnh ở câu đầu |
| **Vách** | Tụt mạnh tại một điểm | Ở đoạn tương ứng của video này, đặt điểm mở vòng hoặc đổi nhịp trước điểm đó |
| **Dốc** | Tụt đều, không có điểm gãy | Rút ngắn mỗi đoạn, thêm ví dụ thật, cắt phần lặp |

Ngưỡng để gọi là «rò» do `10x-yt-doc-so` định. Bản thiết kế bộ skill đề xuất 25% cho kiểu rò ngay đầu, ghi `[ĐỀ XUẤT]`, **không có nguồn**, và chưa được kiểm trên kênh nào. Kịch bản **không tự tính** ngưỡng đó. Kênh mới, chưa có đường giữ chân: ghi `chua-co`, dùng khuôn mặc định, và nói rõ đó là khuôn mặc định.

## 7. Đã bỏ khỏi bản cũ

- Ví dụ hook «sau N năm làm YouTube và N triệu lượt xem, tôi phát hiện…» của bản `10x-youtube-script-hook-vn`: ví dụ khoe số, chuyên gia mới sẽ chép nguyên và bịa thành tích. Đã bỏ.
- Đường dẫn trỏ vào kho riêng của tác giả bản cũ. Đã bỏ.
- Chọn hook theo «cấp bậc» người viết (bắt chước, biến tấu, sáng tạo). Chuyên gia mới không cần phân cấp; cần một hook đúng lời hứa từ chất liệu thật.
