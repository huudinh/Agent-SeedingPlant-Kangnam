# sp-B · ĐỌC BA DÒNG ĐẦU VÀO

> Sổ này trả lời: **agent nhận gì, tên cột nào là gì, thiếu cột nào thì chặn, và tự suy ra được những ô nào.**

---

## 1. BA DÒNG ĐẦU VÀO

| # | Dòng | Dạng | Bắt buộc? | Thiếu thì |
|---|---|---|---|---|
| ① | **Chân dung + Hook/CTA template** | Sheet | 🔴 **BẮT BUỘC** | ⛔ Dừng — không có chân dung thì không ghép được nấc |
| ② | **Hội thoại inbox với khách** | Text / sheet / export | 🟠 **Cần** | Chạy được nhưng mất B3 → ghi `KẾ HOẠCH KHÔNG CÓ INSIGHT MỚI` |
| ③ | **Số liệu hiệu suất tuần trước** | Sheet / CSV export Meta | 🟠 **Cần** | Chạy được nhưng mất B2 → ghi `KHÔNG CÓ CƠ SỞ CẢI TIẾN` |
| ④ | **Hồ sơ bác sĩ** | Sheet | nằm ở `sp-I` | Dùng bản trong `sp-I`; sheet mới thì ⚠️ đối chiếu trước |

⚠️ **Có ① mà thiếu cả ② và ③** → bạn chỉ còn lặp lại kế hoạch cũ. Nói thẳng câu đó ra, đừng giả vờ là kế hoạch mới.

---

## 2. ① CHÂN DUNG + HOOK/CTA — 13 CỘT

Nguồn: sheet ma trận `5A × chân dung`.

### Khối A — điều chung theo nấc (7 cột)

| Cột | Nghĩa | Agent dùng để |
|---|---|---|
| `NẤC 5A` | `A1`…`A5` | Khoá chính — mọi dòng kế hoạch phải có |
| `KHÁCH ĐANG NGHĨ GÌ` | Câu hỏi trong đầu khách | Đối chiếu với hội thoại thật (B3) |
| `NỖI SỢ CHI PHỐI` | Nỗi sợ của nấc | ★ Nguồn gốc của **mã `O-`** (`sp-C` §2) |
| `TRIGGER ĐẨY SANG NẤC SAU` | Điều làm khách bước tiếp | Mục tiêu thật của clip |
| `NỘI DUNG KANGNAM PHẢI CÓ` | Nội dung bắt buộc của nấc | Checklist đủ/thiếu |
| `FORMAT CHỦ LỰC` | Format ưu tiên của nấc | Đầu vào B6 |
| `CTA CHUẨN CỦA NẤC` | CTA mặc định | Đầu vào B5 |

### Khối B — thông điệp riêng theo chân dung (6 cột `CD1`…`CD6`)

**Mỗi ô = 1 thông điệp cho chân dung đó ở nấc đó.**

```
★ Ô TRỐNG = LỖ HỔNG PHỄU, KHÔNG PHẢI "KHÔNG CẦN".
  Ô trống là việc, không phải khoảng trắng. Mỗi ô trống phải ra một dòng kế hoạch
  hoặc một dòng giải thích vì sao chủ ý bỏ trống.
```

### Mã chân dung — ⛔ giữ nguyên qua mọi dịch vụ

| Mã | Mũi | Nghĩa chung của mã |
|---|---|---|
| `CD1` | Khuyết điểm | **Chưa biết mình cần gì** — tệp rộng nhất, nuôi phễu |
| `CD2` | Hot Face | **Muốn đẹp nổi bật**, theo trend, theo người nổi tiếng |
| `CD3` | Sửa lại | **Đã làm, hỏng/không ưng** — nỗi sợ nặng nhất, giá trị cao nhất |
| `CD4` | Nam giới | **Tệp nam** — ngôn ngữ và nỗi sợ khác hẳn |
| `CD5` | Phong thuỷ | **Động cơ ngoài thẩm mỹ** (vận, sự nghiệp) |
| `CD6` | Khó, bệnh lý | **Có yếu tố y khoa** — bắt buộc bác sĩ duyệt |

⚠️ **Mã giữ nguyên, nội dung mã đổi theo chuyên khoa.** Mắt thì `CD5` lệch khỏi quy ước (xem `Agent-OrderMedia · om-J §1`) — gặp chuyên khoa ngoài mũi thì **ghi rõ đang suy ra, không ghi như dữ kiện**.

---

## 3. ② HỘI THOẠI INBOX — NHẬN DẠNG & CHUẨN HOÁ

### Dạng nào cũng nhận được

| Dạng | Nhận dạng bằng |
|---|---|
| Export Meta Inbox | Có cột `Conversation ID` / `Sender` / `Message` / `Created time` |
| Chép tay vào sheet | Có cột kiểu `Khách hỏi` / `Trực page trả lời` |
| Dán thô vào chat | Các dòng xen kẽ `KH:` / `TP:` hoặc `Khách:` / `Page:` |

### Năm trường agent cần moi ra từ mỗi hội thoại

| Trường | Lấy từ đâu | Thiếu thì |
|---|---|---|
| `MÃ HỘI THOẠI` | ID có sẵn, hoặc tự đánh `HT-001` | tự đánh |
| `CÂU HỎI ĐẦU TIÊN CỦA KHÁCH` | ★ tin nhắn đầu tiên do khách gửi | ⛔ bỏ hội thoại khỏi mẫu |
| `MÃ PHẢN ĐỐI` | gán theo `sp-C` §2 | `O-00 chưa phân loại` |
| `NẤC 5A SUY RA` | theo `sp-C` §3 | `A1` mặc định |
| `KẾT CỤC` | có SĐT / có lịch / rơi | `rơi` |

★ **Câu hỏi đầu tiên của khách là trường quý nhất trong cả file.** Nó là **hook đã được thị trường viết sẵn** — khách tự nói ra bằng chính giọng của họ. Mọi trường khác chỉ để đếm; trường này để **chép**.

### ⛔ Luật riêng tư khi đọc hội thoại

```
⛔ TUYỆT ĐỐI KHÔNG đưa vào bất kỳ đầu ra nào:
   · tên thật · số điện thoại · địa chỉ · ảnh khách gửi trong inbox
   · link profile Facebook của khách
   · tình trạng bệnh gắn với một người nhận dạng được

✅ ĐƯỢC đưa: câu hỏi đã viết lại bỏ hết yếu tố nhận dạng, kèm mã HT-nnn
```

Cách ghi đúng:
```
HT-017 · O-05 · A3 · "mổ xong ai theo dõi em, có phải bác sĩ mổ không?"  → rơi
HT-018 · O-01 · A3 · "trọn gói là bao gồm cả xét nghiệm chưa ạ"          → có SĐT
```
Cách ghi **sai** *(⛔ không bao giờ)*:
```
Chị Lan 0987xxx hỏi về cắt mí, ở Cầu Giấy, có tiền sử tiểu đường
```

---

## 4. ③ SỐ LIỆU TUẦN TRƯỚC — CỘT TỐI THIỂU

### Bắt buộc — thiếu là chặn cổng A

`Kỳ (ngày–ngày)` · `Tên ad / mã nội dung` · `Chi tiêu` · `Impression` · `Click` · `Inbox (hội thoại bắt đầu)` · `Lead`

### Rất nên có

`Booking` · `Reach` · `Frequency` · `Bác sĩ` · `Khu vực` · `Chân dung` · `Nấc` · `Format` · `Hook (câu chữ)`

### Cột `HOOK` là cột quan trọng nhất của file số liệu

⚠️ **Không có cột hook thì không chấm được nội dung** — chỉ chấm được ad.
Thiếu cột hook → agent phải ghi:
```
⚠️ File số liệu KHÔNG có cột HOOK → chỉ chấm được theo tên ad.
   Kết luận về nội dung ở dưới là SUY RA từ tên ad, độ tin thấp.
   Cần: khối Ads bổ sung cột HOOK vào báo cáo tuần.
```

---

## 5. MƯỜI Ô AGENT TỰ SUY RA — ⛔ không hỏi lại người dùng

| # | Ô | Suy từ | Luật |
|---|---|---|---|
| ① | `NẤC 5A` của hội thoại | câu hỏi đầu tiên | `sp-C` §3 |
| ② | `MÃ PHẢN ĐỐI` | câu hỏi đầu tiên | `sp-C` §2 |
| ③ | `CHÂN DUNG` | tình trạng khách tự kể | `sp-C` §4 |
| ④ | `CPI` | chi ÷ inbox | `sp-D` §1 |
| ⑤ | `CPL` | chi ÷ lead | `sp-D` §1 |
| ⑥ | `CPB` | chi ÷ booking | `sp-D` §1 |
| ⑦ | `TẦNG RÒ` | so 4 tỷ lệ chuyển với median | `sp-D` §3 |
| ⑧ | `CHẤM NỘI DUNG` | CTR + giữ chân so median | `sp-D` §5 |
| ⑨ | `BÁC SĨ PHÙ HỢP` | chuyên khoa + khu vực + trạng thái chạy | `sp-I` §2 |
| ⑩ | `FORMAT` | nấc + chân dung + format chuẩn của bác sĩ | `sp-F` §3 |

⚠️ Hỏi lại người dùng mười ô này là **làm phiền vô ích** — chúng suy ra được. Hỏi lại những thứ ở `[CHỜ XÁC NHẬN]` mới là hỏi đúng.

---

## 6. QUY ƯỚC MÃ

| Thứ | Mã | Ví dụ |
|---|---|---|
| Hội thoại | `HT-nnn` | `HT-042` |
| Mã phản đối | `O-nn` | `O-05` |
| Dòng kế hoạch tuần | `KH-T<tuần>-<nnn>` | `KH-T45-007` |
| Bác sĩ | `BS<stt>` | `BS03` = Nguyễn Văn Huyên |
| Order giao sản xuất | `OD-T<tuần>-<DV><CD>-<nnn>` | `OD-T45-MUI3-002` |

★ Mã order phải **khớp quy ước của `Agent-OrderMedia`** để hai agent nối được vào nhau.

---

## 7. TỰ KIỂM SỔ NÀY

- [ ] Có đủ ① chân dung chưa? Thiếu là dừng.
- [ ] Hội thoại đã moi được **câu hỏi đầu tiên của khách** chưa?
- [ ] Đã bỏ sạch tên/SĐT/địa chỉ khỏi mọi dòng chưa?
- [ ] File số liệu có cột `HOOK` không? Không có thì đã ghi cảnh báo chưa?
- [ ] Mười ô ở §5 đã tự điền, không hỏi lại người dùng chứ?
- [ ] Ô trống trong ma trận chân dung đã được tính là **việc**, không phải khoảng trắng chứ?
