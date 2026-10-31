# Rubric sáu tiêu chí: mô tả mức PASS và FAIL

Tệp này là phần «neo» của `10x-yt-soat`. Bản cũ chấm điểm mà chỉ neo một tiêu chí, nên hai lần chấm cho hai điểm khác nhau. Ở đây **mỗi tiêu chí có một phép thử có đáp án có/không** và một định nghĩa FAIL tìm ra được bằng cách đọc chữ trong tệp. Không có điểm số, không có điểm bù: một tiêu chí FAIL là FAIL.

Ba luật chung cho cả sáu tiêu chí:

1. **Mỗi lỗi chỉ tính ở MỘT tiêu chí.** Con số không nhãn chỉ rơi vào S2, không rơi thêm vào S3. Hook lệch lời hứa chỉ rơi vào S1. Nhờ vậy khi gỡ một tiêu chí khỏi skill, đúng lỗi của nó mới lọt, và người đọc biết sửa ở đâu.
2. **FAIL phải trích được một câu nguyên văn** nằm trong tệp (xem «Cách trích» ở `mau-bao-cao.md`). Không trích được thì chưa được ghi FAIL: đọc lại. Lỗi do **thiếu** một thứ (thiếu cầu nối, thiếu dòng nguồn) thì trích dòng nhãn hoặc câu liền kề nơi thứ đó đáng lẽ có.
3. **Chỉ chấm theo chữ trong tệp.** Không chấm theo thứ bạn đoán người viết «định nói». Không kiểm sự thật ngoài đời: skill này kiểm câu có **truy được về chất liệu người dùng đưa** hay không, không kiểm chất liệu đó có đúng với thế giới hay không.

Cách đọc hai chế độ: **trước quay** chấm `kich-ban/<ma>.md` (đọc theo khuôn của `10x-yt-kich-ban`). **Trước đăng** chấm bản chép lời của bản đã quay, đối chiếu với kịch bản đã qua soát. Chỗ hai chế độ khác nhau ghi ở từng tiêu chí.

Khi kịch bản **không theo khuôn** (viết tay, hoặc là bản chép lời thô): đọc theo nội dung. «Hook» là phần mở đầu; «đoạn» là mỗi khúc có một ý chính; «chốt tập» là phần cuối. Tiêu chí nào cần một thứ khuôn không có (ví dụ bảng dữ kiện) thì thứ thiếu đó được tính vào kết quả, theo từng tiêu chí dưới đây.

---

## S1. Lời hứa trả trong 20 giây đầu

**Việc kiểm:** hook có làm đúng điều tiêu đề và ảnh đã hứa, ngay ở những giây đầu.

**Lấy gì làm chuẩn:** lời hứa ghi ở `goi/<ma>.md`, mục «Lời hứa» (hoặc mục 8 «Chuyển cho 10x-yt-kich-ban»). Gói không có mục đó (ví dụ gói chỉ là một dòng tiêu đề) thì lấy lời hứa từ tiêu đề chính, ghi `[SUY LUẬN]` và nói đã làm vậy.

**Ba câu hỏi có đáp án:**

1. Có **một câu nguyên văn** trong hook đáp lại lời hứa không? «Trả lời» nghĩa là câu đó nói ra hoặc chiếu ra đúng loại thứ lời hứa nêu (kết quả, quá trình, cơ chế hay thông tin), không chỉ nhắc cùng chủ đề.
2. Câu đó nằm trong **20 giây đầu** không? Có mốc thời gian thì câu phải bắt đầu trước giây 20. Không có mốc thời gian thì câu phải nằm trong `[ĐỀ XUẤT] 60` từ đầu (cùng ngưỡng với `10x-yt-kich-ban`; 3 từ mỗi giây nhân 20 giây).
3. Hook có hứa **thêm** điều nằm trong «Điều video không được hứa thêm» của gói không?

**PASS khi:** cả ba đáp án đúng (có câu; câu nằm trong 20 giây đầu; không hứa thêm).

**FAIL khi** một trong các điều sau, trích câu hook nặng nhất:

- Hook nói về chủ đề chung hoặc kể chuyện khác, không có câu nào đáp lại lời hứa.
- Câu đáp lại lời hứa có, nhưng nằm sau giây 20 (hoặc sau 60 từ đầu). Mở bằng lời chào hay giới thiệu kênh làm câu trả lời trượt khỏi mốc cũng tính ở đây.
- Hook hứa điều gói cấm hứa thêm.
- Lời hứa chép trong kịch bản **khác** lời hứa của gói (người viết đã đổi lời hứa giữa chừng). Trích dòng `Lời hứa phải trả:` của kịch bản.

**Lời khai không phải bằng chứng:** dòng `Hook trả lời lời hứa: "…" ← "…"` do người viết tự điền. Skill kiểm xem câu được khai **có thật sự** trả lời không; câu khai mà không trả lời thì FAIL, trích chính câu hook đó.

**Ca ranh giới:** lời hứa «chỉ ra chỗ rối rồi sửa thành một ý» có hai vế. Hook «Slide này rối, và hôm nay mình sửa nó cho bạn xem.» chỉ trả vế sửa, không nói gì về «chỉ ra chỗ rối» hay «một ý»: FAIL nếu vế còn lại không xuất hiện trong 20 giây đầu. Hook «Mình chỉ ra đúng chỗ khiến slide này rối, rồi sửa nó thành một ý.» thì PASS dù chưa làm xong việc, vì lời hứa cần được **nêu và bắt đầu thực hiện** trong 20 giây đầu, chưa cần hoàn tất.

**Trước đăng:** chấm trên chữ **người nói thật sự nói** trong bản quay, không chấm trên kịch bản. Người nói bỏ đoạn hook đã duyệt, hay ứng tác mở bằng chuyện khác, thì FAIL.

---

## S2. Mỗi dữ kiện có nhãn nguồn

**Việc kiểm:** mọi số và tên riêng người xem sẽ nghe đều truy được về một câu có thật trong chất liệu của người dùng. Đây là tiêu chí chống bịa, và là việc chính của skill.

**Kiểm từng số một** (làm bằng cách liệt kê, không đọc lướt):

1. Liệt kê **mọi số và tên riêng** trong chữ nói ra: các dòng hook bắt đầu bằng `> `, các gạch sau `Nói:`, và các dòng `Cầu nối:`, `Lời mời:`. Gồm cả số viết bằng chữ chỉ lượng thật («hai khách», «ba tháng», «tám dòng»), tên người, tên kênh, tên công cụ, tên thương hiệu, năm, phần trăm, và **tên có chữ số**: tên chất hoặc thuật ngữ (omega 3, vitamin B12), tên nghiên cứu kèm năm (Nagao 2007), mã sản phẩm hoặc đời máy (iPhone 15). Tên có chữ số là số: thiếu `[D#]` thì trượt S2 như mọi số khác, không được bỏ qua vì «chỉ là tên chất». Không tính mạo từ «một ý», «một việc».
   **Liệt kê bằng lệnh:** chạy `grep -nE '[[:alpha:]][ -]?[0-9]|[0-9]'` trên các dòng hook, `Nói:`, `Cầu nối:`, `Lời mời:` của kịch bản rồi duyệt từng dòng lệnh ra; không đếm bằng mắt.
2. Với từng mục, bốn câu hỏi:
   - (a) Có dấu `[D#]` đi kèm không?
   - (b) `D#` đó có dòng trong bảng dữ kiện (mục 5 của kịch bản) và dòng có **nhãn** `[SỐ LIỆU]` hoặc `[TRÍCH]` không?
   - (c) Cột «Nguyên văn trong chất liệu» có phải **chuỗi tìm thấy nguyên văn** trong Kho chất liệu (mục 1 của kịch bản, các dòng `M#`) hoặc trong tệp chất liệu người dùng đưa không?
   - (d) Con số/tên **nói ra** có giống con số/tên trong nguyên văn không (không làm tròn khác, không đổi đơn vị, không đổi tên)?
3. **Số cấu trúc** (đếm các mục mình nêu: «ba lỗi», «hai bước»): đếm số mục kịch bản thật sự nêu, phải khớp.
4. **Khẳng định như sự thật chung không số** («đa số người xem bỏ đi sau giây đầu», «YouTube ưu tiên video dài») cũng là dữ kiện. Không có nhãn và không có câu chất liệu đỡ thì tính như một mục không có nguồn. Số về thuật toán, lượt tìm, CPM, thị phần: coi là không nguồn (`references/chung/da-bi-bac.md`).
5. **`[CẦN NGUỒN]` còn nằm trong chữ nói ra** (trong `> `, trong gạch `Nói:`) cũng là một mục không có nguồn: người nói sẽ đọc lên một chỗ trống. (`[CẦN NGUỒN]` ở dòng `Bằng chứng:` hay `Ví dụ:` thuộc S4, không tính ở đây.)

**PASS khi:** mọi mục liệt kê ở bước 1 qua đủ (a) đến (d), số cấu trúc khớp, và không còn khẳng định chung không nguồn.

**FAIL khi** có một mục trượt bất kỳ. Trích **câu chứa mục đó**, nguyên văn, kể cả `[D#]` nếu có. Phân loại trong cột «Đã kiểm» để người viết biết nặng nhẹ:

| Loại trượt | Nghĩa | Nặng |
|---|---|---|
| Không nhãn | Số/tên không có `[D#]` hoặc `D#` không có trong bảng | Nặng |
| Nhãn giả | Có `D#`, có nhãn, nhưng nguyên văn không tìm thấy trong chất liệu | Nặng nhất: trông như đã kiểm mà không phải |
| Lệch | Nguyên văn có thật nhưng số nói ra khác (làm tròn, đổi đơn vị) | Nặng |
| Chung không nguồn | Khẳng định như sự thật chung, không có câu đỡ | Vừa |
| Số cấu trúc lệch | Nói «ba lỗi» mà nêu hai hoặc bốn | Vừa |
| Chỗ trống đọc ra | `[CẦN NGUỒN]` nằm trong chữ nói ra | Vừa |

**Không có tệp chất liệu và kịch bản không có Kho chất liệu** (kịch bản ngoài khuôn): hỏi người dùng đúng một câu xin tệp hoặc đoạn chất liệu. Họ không có thì mọi số/tên trong kịch bản là «chưa truy được»: ghi FAIL kèm loại «Không nhãn» và nói rõ **không phải** kết luận rằng số đó sai, chỉ là chưa truy được.

**Trước đăng:** số/tên người nói thật sự nói phải nằm trong bảng dữ kiện của kịch bản đã soát. Số nào người nói ứng tác thêm trên hình mà không có trong bảng là «Không nhãn». Sửa bằng cách cắt câu đó khỏi bản đăng, hoặc đưa chất liệu để bổ sung bảng ở `10x-yt-kich-ban`.

---

## S3. Không nghe chung chung, không nghe kiểu AI

**Việc kiểm:** người xem nghe ra đây là chuyện của **người này**, không phải bài viết ai cũng có thể nói.

**Hai phép thử:**

- **Phép thay người.** Đổi nghề của người nói thành một nghề khác và giữ nguyên câu. Câu vẫn đúng và vẫn trơn thì nó chung chung. Câu có chi tiết riêng (cảnh, số, tên, case, lời của khách) thì phép thay làm câu sai.
- **Mẫu lỗi.** Ba mẫu hay gặp ở chữ do AI viết:
  - M1 (nội bộ; khi báo nói «câu sáo mở»): sáo mở và đệm không mang thông tin: «Trong thế giới ngày nay…», «Hôm nay mình sẽ chia sẻ…», «Bạn có bao giờ tự hỏi…», «Hãy cùng khám phá…», «Đây là bí quyết…».
  - M2 (nội bộ; khi báo nói «đoạn thay người được»): đoạn thay người được: cả đoạn chỉ gồm câu qua phép thay người, không câu nào có chi tiết riêng.
  - M3 (nội bộ; khi báo nói «chỗ phóng đại rỗng»): phóng đại rỗng và cân đối giả: «cực kỳ quan trọng», «thay đổi hoàn toàn», «không chỉ A mà còn B» dùng khi không có bằng chứng đi kèm.

**PASS khi:** hook và câu mở của mỗi đoạn không dính M1, và không có đoạn nào dính M2.

**FAIL khi:** có một câu M1 ở hook hoặc ở câu mở đoạn, hoặc có một đoạn M2. Trích câu M1, hoặc câu đầu của đoạn M2. M3 lẻ ở giữa gạch `Nói:` **không** làm FAIL; ghi vào cột «Đã kiểm» như một ghi chú («2 chỗ phóng đại rỗng») để người viết cắt khi sửa.

**Không tính ở đây:** số không nhãn (S2), hook lệch lời hứa (S1), đoạn thừa (S4). Một câu vừa sáo vừa có số không nhãn thì ghi số ở S2, sáo ở S3, mỗi nơi một lần.

**Ranh giới:** câu đúng nghề nhưng chưa có chi tiết riêng, ở **giữa** đoạn có chi tiết riêng ở câu khác, không phải M2. M2 là cả đoạn không có chi tiết riêng nào.

**Trước đăng:** chấm trên chữ nói thật. Chữ nói ứng tác có nhiều đệm khẩu ngữ («à», «thì là», «kiểu như») không phải M1; M1 chỉ là mẫu sáo ở trên.

---

## S4. Mỗi đoạn có lý do tồn tại

**Việc kiểm:** không đoạn nào ở trong video mà người xem không mất gì nếu bỏ đi, và không đoạn nào có ý mà không có gì đỡ.

**Làm bằng một bảng nhỏ trong đầu hoặc trên giấy:** mỗi đoạn một dòng, ghi (i) đoạn đó trả **vế nào của lời hứa** hoặc trả **câu hỏi nào mà đoạn trước đã mở**, (ii) dòng `Bằng chứng:` và `Ví dụ:` của nó có chất liệu thật không.

**Phép thử bỏ đoạn.** Bỏ đoạn đó đi: lời hứa của gói vẫn được trả đủ **và** cái nối của đoạn trước vẫn khớp với đoạn sau? Nếu có, đoạn đó thừa.

**PASS khi:** mọi đoạn trỏ được vào (i), và không đoạn nào mang `[CẦN NGUỒN]` ở dòng `Bằng chứng:` hay `Ví dụ:`.

**FAIL khi** có một trong các điều sau, trích câu `Ý:` của đoạn đó:

- Đoạn thừa theo phép thử bỏ đoạn.
- Đoạn mở một vòng bằng cái nối «mở vòng» mà không đoạn sau nào đóng nó.
- Đoạn có `Ý:` nhưng dòng `Bằng chứng:` hoặc `Ví dụ:` còn `[CẦN NGUỒN]` chưa lấp. Đoạn đó chưa có gì để nói thật, nên chưa quay được.

**Không tính ở đây:** số trong đoạn không nhãn (S2). Đoạn có `[CẦN NGUỒN]` ở dòng nguồn là S4; `[CẦN NGUỒN]` nằm trong chữ nói là S2.

**Ranh giới:** đoạn ngắn mà chỉ làm cầu nối cho hai đoạn quan trọng vẫn có lý do tồn tại nếu bỏ nó thì cái nối gãy. Đoạn «tóm lại» nhắc lại điều vừa nói mà không thêm gì thì thừa.

**Trước đăng:** chấm trên các khúc của bản quay. Người nói thêm một khúc ngoài kịch bản mà không trả vế nào của lời hứa thì FAIL, trích câu đầu của khúc đó.

---

## S5. Chốt tập có cầu nối

**Việc kiểm:** phần cuối đưa người xem sang video kế bằng một lý do cụ thể, không dừng ở «hẹn gặp lại».

**Ba câu hỏi:**

1. Dòng `Video kế:` có tên một video **cụ thể**, và video đó có trong `de-tai.md` (đọc được thì đối chiếu, không bỏ) với trạng thái khác `bo` không?
2. Dòng `Cầu nối:` có phải một câu **nói ra**, nêu một lý do cụ thể dẫn từ điều video này vừa mở hoặc chưa trả sang video kế?
3. Dòng `Tóm một câu:` có dùng cùng chữ với lời hứa của gói, không thêm lời hứa mới?

**Phép thử cầu nối.** Bỏ tên video kế khỏi câu cầu nối. Câu còn đúng với bất kỳ video nào thì nó chung chung («hẹn các bạn video sau», «đừng quên theo dõi»).

**PASS khi:** cả ba đáp án đúng.

**FAIL khi:**

- `Video kế:` trống, hoặc ghi `chua-co-de-tai-ke`. Chốt tập chưa có chỗ để nối: không thể có cầu nối thật. Việc sửa chỉ sang `10x-yt-de-tai`; skill soát không đặt tên video hộ.
- `Video kế:` nêu một video không có trong `de-tai.md` (tên bịa).
- `Cầu nối:` trống hoặc không qua phép thử cầu nối.
- `Tóm một câu:` hứa điều mới.

Trích câu `Cầu nối:` nếu có chữ; không có chữ thì trích dòng nhãn nguyên văn («Cầu nối:») hoặc dòng `Video kế:` liền kề và ghi «(dòng trống)» trong cột «Đã kiểm».

**Trước đăng:** chấm trên phần cuối của bản quay. Người nói bỏ cầu nối đã duyệt thì FAIL.

---

## S6. Lời mời khớp mức hâm nóng

**Việc kiểm:** lời mời cuối video không đòi người xem nhiều hơn mức video này đã xứng đáng được, và không phải thứ do máy nghĩ ra.

**Ba câu hỏi:**

1. Có **đúng một** dòng `Lời mời:` không?
2. Có dòng `Nguồn lời mời:` với nguồn hợp lệ (dòng đã lưu từ `10x-yt-loi-moi`, câu chính người dùng viết, hoặc `[CẦN NGUỒN: lời mời]` kèm chỉ sang `10x-yt-loi-moi`) không? Ưu đãi, quà, giá, khoá học do máy tự nghĩ ra thì FAIL.
3. Mức mời có vượt mức hâm nóng không? Dùng **thang mức mời** sau (`[ĐỀ XUẤT]`, chưa kiểm, `10x-yt-loi-moi` sẽ giữ thang đầy đủ):

| Mức | Lời mời | Video phải làm nóng tới đâu thì mới được mời |
|---|---|---|
| 1 | Xem video kế, đăng ký, để lại câu hỏi | Mọi video |
| 2 | Nhận quà hoặc tài liệu miễn phí có thật | Video đã giải trọn một vấn đề, có ít nhất một ca hoặc số thật của chính người nói (một dòng `M#` loại case hoặc số), và quà nối thẳng vào vấn đề vừa giải |
| 3 | Đặt lịch, nói chuyện trực tiếp | Như mức 2, và video nói rõ người nói làm gì cho ai, lấy từ chất liệu của họ |
| 4 | Mua | Như mức 3, và có sản phẩm bán, và thứ được mời là thứ có thật nêu ở `Nguồn lời mời:` |

**Chưa có sản phẩm bán:** chỉ được mức 1. Mời mua, hay mời nhận quà gắn với sản phẩm chưa có, là FAIL.

**PASS khi:** cả ba đáp án đúng: một dòng, nguồn hợp lệ, mức mời không vượt mức video đã làm nóng.

**FAIL khi:** thiếu hoặc nhiều hơn một dòng lời mời; thiếu hoặc sai nguồn; mức mời cao hơn mức cho phép. Trích dòng `Lời mời:`.

**Ranh giới:** video mới dạy một ý nhỏ, chưa có ca thật của người nói, mà mời nhận quà mức 2: FAIL, hạ xuống mức 1. Việc sửa chỉ nói «hạ về mức 1 hoặc bổ sung ca thật vào video»; không soạn câu mời thay.

**Trước đăng:** chấm trên lời mời người nói thật sự nói. Người nói đổi lời mời so với bản đã duyệt thì chấm lại như một lời mời mới.
