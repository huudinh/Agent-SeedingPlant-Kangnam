# sp-D · ĐỌC SỐ TUẦN TRƯỚC & ĐÁNH GIÁ NỘI DUNG

> Sổ này trả lời: **CPI/CPL/CPB tính thế nào, tuần trước yếu ở tầng nào, nội dung nào tốt/kém, và cải tiến gì là cải tiến đúng người.**
>
> ⚠️ Sổ này là **bản rút gọn để lên kế hoạch**. Chẩn đoán số liệu đầy đủ (30 mã cảnh báo, chủ sở hữu từng mã) là việc của `Agent-AdsReport-Kangnam` — đừng làm lại ở đây.

---

## 1. ★ ĐỊNH NGHĨA CHỈ SỐ — CHỐT MỘT LẦN

> Hai người cãi nhau về CPL suốt một tháng, cuối cùng phát hiện một người tính `chi ÷ lead-Meta`, người kia tính `chi ÷ lead-CRM-đã-lọc-rác`. **Không thống nhất định nghĩa thì mọi kết luận phía sau đều vô nghĩa.**

| Tầng | Chỉ số | Công thức | Nguồn |
|---|---|---|---|
| Hiển thị | **CPM** | chi ÷ impression × 1.000 | Meta |
| | **Frequency** | impression ÷ reach | Meta |
| Click | **CTR** | click ÷ impression | Meta |
| Inbox | **CPI** | chi ÷ **hội thoại tin nhắn bắt đầu** | Meta |
| Lead | **CPL** | chi ÷ **lead hợp lệ** | Meta (chi) + CRM (lead) |
| Booking | **CPB** | chi ÷ **booking** | Meta + CRM |

### Ba định nghĩa phải ghi rõ trong mọi đầu ra

| Từ | Định nghĩa dùng trong bộ agent này |
|---|---|
| **Lead** | Một liên hệ có **SĐT dùng được** + **dịch vụ quan tâm**, đã qua lọc rác |
| **Booking** | Lịch hẹn có **ngày–giờ–cơ sở cụ thể** và **khách đã xác nhận**. *"Để em sắp xếp rồi báo lại"* ⛔ **không phải booking** |
| **Mốc quy ngày** | Quy về **ngày phát sinh CHI PHÍ**, không phải ngày telesales gọi |

⛔ **Lead-Meta ≠ Lead-CRM.** Chênh 15–30% là bình thường; **> 30% là số chưa dùng được** → chặn cổng A.
★ Đầu ra **luôn ghi rõ đang dùng loại nào**. Không ghi = người đọc tự hiểu theo cách của họ = cãi nhau tuần sau.

### Quy ước ghi số
- Tiền: `412k` · `18,2tr` · `1,25 tỷ` — ⛔ không ghi `412000`
- Tỷ lệ: 1 chữ số thập phân — `1,8%`
- Lệch: **cả % và số tuyệt đối** — `+40% (295k → 412k)`
- Cỡ mẫu: luôn kèm — `(37 lead / 18,2tr)`
- Kỳ: `07–13/10`, ⛔ không ghi *"tuần này"*

---

## 2. ★ PHÂN RÃ CPL — CHẠY MỖI KHI CPL TĂNG

```
CPL  =  (CPM / 1000)  ÷  ( CTR × click→inbox% × inbox→lead% )
```

⛔ **Không phân rã thì mọi kết luận đều là *"CPL tăng, xem lại đi"* — vô dụng.**

CPL tăng 40% có **bốn nguyên nhân hoàn toàn khác nhau, bốn người khác nhau xử**:

| Thành phần xấu đi | Nghĩa là | Ai xử | ★ Agent này có làm được gì không |
|---|---|---|---|
| **CPM** tăng | Đấu giá đắt lên · tệp hẹp · mùa cao điểm | Adnet (tệp, bid, lịch) | ⛔ **Không.** Đổi hook không cứu được CPM |
| **CTR** giảm | ★ **Hook/creative yếu hoặc bão hoà** | Adnet (creative) | ✅ **Đây là việc của agent này** |
| **click→inbox** giảm | Điểm đến hỏng: lời chào tự động lỗi, landing chậm | Adnet + Kỹ thuật | ⛔ Không — nhưng phải **ghi rõ** để không ai đổ cho nội dung |
| **inbox→lead** giảm | Trực page: chậm trả lời, thiếu người ca tối | Trực page | ⛔ Không — nhưng hội thoại ở `sp-C` §7 cho biết thiếu clip gì |

★ **Luật quan trọng nhất của sổ này:**
```
⛔ KHÔNG ĐỀ XUẤT ĐỔI NỘI DUNG KHI THÀNH PHẦN XẤU ĐI KHÔNG PHẢI CTR.

CPL tăng vì CPM → đổi hook là tốn một tuần sản xuất để chữa nhầm bệnh.
Agent này phải nói thẳng: "tuần này KHÔNG phải vấn đề nội dung".
```

⚠️ Nói được câu *"tuần này không phải lỗi nội dung"* là giá trị, không phải né việc. Một agent nội dung luôn kết luận *"cần làm thêm content"* là một agent vô dụng.

### CPM tăng nhưng CPL giữ nguyên
→ **Không có vấn đề gì.** Chỉ ghi nhận. CPM chỉ có nghĩa khi dùng để **giải thích** CPL.

---

## 3. BỐN TẦNG RÒ — CHỈ XUẤT MỘT PHIẾU CHO TẦNG NHỎ NHẤT

| Tầng | Tỷ lệ | Rò khi | Chủ |
|---|---|---|---|
| ① | click → inbox | ≤ −30% median | Adnet + Kỹ thuật |
| ② | inbox → lead | ≤ −25% median, inbox ≥ 30 | Trực page |
| ③ | lead → booking | ≤ −25% median, lead ≥ 20 | Telesales |
| ④ | booking → đến | ≤ −25% median, booking ≥ 15 | Lễ tân / CSKH |

⛔ **Nhiều tầng cùng rò → chỉ kết luận ở tầng NHỎ NHẤT**, các tầng sau ghi vào ô *"hệ quả kéo theo"*.
> Bắn ba kết luận cho ba phòng ban là cách nhanh nhất để ba phòng đổ lỗi cho nhau trong hai tuần.

⚠️ **Tầng ② kiểm hai việc trước khi kết luận lỗi trực page:** ① thời gian phản hồi lần đầu *(quá 5 phút là tụt mạnh)* · ② **ca trực tối / cuối tuần có người không**. Phần lớn rò tầng ② là **lỗi xếp ca, không phải lỗi kỹ năng**.

---

## 4. SO VỚI CÁI GÌ — LUẬT MEDIAN

```
⛔ KHÔNG so với mục tiêu. ⛔ KHÔNG so với "tháng trước".
✅ So với MEDIAN 7 NGÀY cùng đơn vị, cùng loại ngày.
```

| Muốn biết | Đặt cạnh |
|---|---|
| Ad này tốt không | Median các ad **cùng nấc, cùng chân dung** |
| Bác sĩ này hiệu quả không | **Median team** cùng khu vực, cùng chuyên khoa |
| Khu vực này yếu không | Median các khu vực cùng kỳ |
| Tuần này xấu không | Median 4 tuần gần nhất, **loại tuần có ưu đãi lớn** |

### Bốn thứ CHẶN kết luận — kiểm trước khi kết luận bất kỳ điều gì

| Tình huống | Luật |
|---|---|
| Đang so **cuối tuần với ngày thường** | ⛔ **HUỶ** kết luận |
| **Ngày đầu sau khi ưu đãi kết thúc**, CPL tăng ≥ 30% | ⛔ **GIẢI THÍCH**, không quy trách nhiệm |
| **CPM tăng ≥ 30% đồng loạt ở ≥ 70% ad set** | ⛔ Đây là **thị trường**, không phải đội. Không ai sửa được bằng đổi creative |
| Ad **vừa bị từ chối / hạn chế** trong kỳ | ⛔ Số của ad đó **không dùng để chấm nội dung** |

★ Bốn mục này là **chống báo động giả**. Thiếu chúng, agent sẽ đề xuất làm lại nội dung mỗi thứ Hai sau cuối tuần — và đội sẽ ngừng đọc kế hoạch sau ba tuần.

---

## 5. ★ CHẤM NỘI DUNG — BA BẬC

Chấm **nội dung** (hook + format), không chấm ad. Cần cột `HOOK` trong file số liệu — thiếu thì xem `sp-B` §4.

| Chấm | Điều kiện | Việc tuần này |
|---|---|---|
| 🟢 **TỐT** | CTR ≥ median **và** CPL ≤ median, đủ mẫu | **Nhân bản** — xem §6 |
| 🟡 **TRUNG BÌNH** | Một trong hai chỉ số đạt | Giữ chạy, **làm 1 biến thể** đổi đúng một biến |
| 🔴 **KÉM** | CTR ≤ −30% median **và** CPM trong dải ±15% | **Bỏ hook, giữ ý** — xem §6 |

★ Điều kiện *"CPM trong dải ±15%"* ở bậc KÉM là điều kiện **bảo vệ người viết**: CTR thấp mà CPM cũng vọt thì đó là **đấu giá**, không phải hook dở.

### Bốn dấu hiệu bão hoà — nội dung chưa dở nhưng đã hết tác dụng

| Dấu hiệu | Ngưỡng | Nghĩa |
|---|---|---|
| Bão hoà tệp | frequency 7 ngày ≥ **2,5** **và** CTR giảm ≥ 20% | Người ta đã xem chán |
| Trôi dần | CTR giảm **3 ngày liên tiếp**, tổng ≥ 15% | Đang chết dần |
| Phụ thuộc 1 creative | 1 ad chiếm ≥ **60%** chi ad set | Winner chết là mất cả ad set |
| **Thiếu challenger** | ≥ **14 ngày** không có creative mới trong ad set tiêu ≥ 20% ngân sách | ★ **Mã phòng bệnh duy nhất** |

⚠️ **Frequency 3,0 mà CTR giữ nguyên là tệp trung thành, không phải bão hoà.** Tắt đi là mất một ad set tốt.

★ **"Thiếu challenger" là mã quan trọng nhất với agent này** — nó cảnh báo một việc **chưa xảy ra**. Không có challenger thì khi winner xuống sức sẽ không có gì thay, và lúc đó mới làm nội dung mới là **đã chậm 7–10 ngày**. → Kế hoạch tuần **luôn phải có ô challenger**, kể cả tuần số đẹp (`sp-G` §3).

---

## 6. CẢI TIẾN — BỐN ĐƯỜNG, ⛔ MỖI LẦN ĐỔI MỘT BIẾN

| Đường | Khi nào | Đổi gì | Giữ gì |
|---|---|---|---|
| **NHÂN BẢN** | Nội dung 🟢 TỐT | Chân dung / khu vực / bác sĩ | **Giữ nguyên hook** |
| **BIẾN THỂ** | 🟡 TRUNG BÌNH | **Đúng một biến**: hook, hoặc 3 giây đầu, hoặc CTA | Phần còn lại |
| **GIỮ Ý — BỎ HOOK** | 🔴 KÉM nhưng mã `O` vẫn cao trong hội thoại | Viết lại hook từ đầu | Giữ ý, giữ format |
| **BỎ HẲN** | 🔴 KÉM **và** mã `O` thấp | — | — |

```
⛔ KHÔNG ĐỔI ≥ 3 BIẾN CÙNG LÚC (hook + format + bác sĩ).

Không phải lỗi đạo đức — là lỗi phương pháp: đổi ba biến cùng lúc thì dù
kết quả tốt lên cũng KHÔNG HỌC ĐƯỢC GÌ, lần sau lặp lại không ra.
```

### Đường hay bị bỏ qua: **GIỮ Ý — BỎ HOOK**
Hook kém không có nghĩa là **ý** kém. Khi hội thoại vẫn cho thấy mã `O` đó cao, nghĩa là **nhu cầu có thật, cách gọi tên đang sai**. Bỏ cả ý là mất một nhu cầu có thật.

---

## 7. LUẬT PORT — ĐEM HOOK SANG MIỀN KHÁC

```
⚠️ Một hook 🟢 TỐT ở miền này KHÔNG tự động TỐT ở miền khác.
```

| Khu vực | Đặc điểm đã đo |
|---|---|
| **NAM** | Kho nội dung dày nhất, nhiều nội dung TỐT nhất. Hook *"gọi tình trạng"* thắng rõ |
| **BẮC** | ⚠️ Yếu hơn Nam. Nhiều nội dung TỐT ở Nam **chấm KÉM khi port sang Bắc** |
| **MIỀN TÂY** | ★ Công thức riêng rất mạnh: **"lên thành phố làm"** — *chị em miền Tây không làm ở miền Tây mà rủ nhau lên thành phố* |
| **VIỆT KIỀU** | Nỗi sợ riêng: **về nước ngắn ngày, sợ không kịp hồi phục và cắt chỉ** → đúng mã `O-09` |

★ **Port thì quay lại hook bằng giọng và bối cảnh miền đó**, giữ nguyên thân video. ⛔ Không chỉ đổi dòng chữ trên màn hình.

---

## 8. BẢNG "TUẦN TRƯỚC YẾU GÌ" — ĐẦU RA CHUẨN CỦA B2

```
KỲ            : 07–13/10   ·   LEAD ĐẾM THEO: CRM
CHI           : 182tr      ·   CPL 412k (442 lead)   ·   CPB 1,86tr (98 booking)

① PHÂN RÃ CPL : CPM +8%  ·  CTR −31%  ·  click→inbox −4%  ·  inbox→lead +2%
   → THÀNH PHẦN XẤU  : CTR
   → KẾT LUẬN        : ✅ ĐÂY LÀ VẤN ĐỀ NỘI DUNG — việc của kế hoạch tuần này

② TẦNG RÒ NHỎ NHẤT : không có tầng nào vượt ngưỡng

③ CHẤM NỘI DUNG    : 🟢 4  ·  🟡 9  ·  🔴 6  ·  chưa đủ mẫu 3

④ BÃO HOÀ          : 2 ad set frequency ≥2,5 kèm CTR giảm
                     ⚠️ 1 ad set 19 NGÀY không có challenger

⑤ CHẶN KẾT LUẬN    : không

⑥ CẢI TIẾN         : nhân bản 4  ·  biến thể 9  ·  giữ ý bỏ hook 4  ·  bỏ hẳn 2
```

---

## 9. TỰ KIỂM SỔ NÀY

- [ ] Đã ghi **lead đếm theo Meta hay CRM** chưa?
- [ ] Đã **phân rã CPL** trước khi kết luận chưa?
- [ ] Thành phần xấu đi có phải **CTR** không? Không phải thì đã nói thẳng *"không phải vấn đề nội dung"* chưa?
- [ ] Có đang so cuối tuần với ngày thường không?
- [ ] Mọi chấm điểm có kèm **cỡ mẫu** không?
- [ ] Có ad nào **bị từ chối** mà vẫn bị đem ra chấm nội dung không?
- [ ] Đã kiểm **thiếu challenger** chưa — kể cả khi tuần này số đẹp?
- [ ] Có đường cải tiến nào đổi **≥ 3 biến cùng lúc** không?
