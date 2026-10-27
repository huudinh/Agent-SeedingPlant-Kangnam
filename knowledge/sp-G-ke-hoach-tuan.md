# sp-G · KẾ HOẠCH NỘI DUNG TUẦN — ĐẦU RA

> Sổ này trả lời: **đầu ra gồm mấy bảng, mỗi bảng bao nhiêu cột, cột nào bắt buộc, và bảng nào giao cho ai.**

---

## 1. ĐẦU RA CÓ **BỐN BẢNG + HAI KHỐI**

| # | Bảng | 1 dòng = | Giao cho |
|---|---|---|---|
| ① | **ĐỌC SỐ TUẦN TRƯỚC** | 1 nội dung đã chạy | Khối Ads |
| ② | **INSIGHT HỘI THOẠI** | 1 mã `O` | Khối nội dung |
| ③ | ★ **KẾ HOẠCH TUẦN** | **1 bài đăng** | Bác sĩ + biên tập cơ sở |
| ④ | **ORDER SẢN XUẤT** | **1 clip cần quay** | `Agent-OrderMedia` → ekip |
| ⑤ | Khối **CỜ PHÁP CHẾ** | 1 cờ + **câu thay thế** | Pháp chế |
| ⑥ | Khối **[CHỜ XÁC NHẬN]** | 1 thứ còn thiếu + ai cấp + chặn mấy dòng | Vận hành |

⚠️ **Bảng ③ và ④ không phải một bảng.** Bảng ③ là **lịch đăng** *(gồm cả bài không cần quay: ảnh, caption, seeding)*. Bảng ④ chỉ gồm **clip cần ekip quay**. Gộp hai bảng là cách làm ekip nhận nhầm việc.

---

## 2. ★ BẢNG ③ — KẾ HOẠCH TUẦN · 18 CỘT

| # | Cột | Nội dung | Bắt buộc |
|---|---|---|---|
| 1 | `MÃ` | `KH-T45-001` | 🔴 |
| 2 | `NGÀY` | `T2 03/11` | 🔴 |
| 3 | `KHUNG GIỜ` | `sáng` · `hành chính` · `20–23h` | 🔴 |
| 4 | `BÁC SĨ` | `BS03 Huyên` | 🔴 |
| 5 | `KÊNH` | page bác sĩ · page thương hiệu · group | 🔴 |
| 6 | `LOẠI BÀI` | `WORKSTYLE` · `LIVESTYLE` · `ADS PERFORMANCE` | 🔴 |
| 7 | `FORMAT` | `L03` | 🔴 |
| 8 | `CHÂN DUNG` | `CD3` | 🔴 |
| 9 | `NẤC 5A` | `A2` | 🔴 |
| 10 | `MÃ O ĐÓNG` | `O-05` | 🔴 |
| 11 | ★ `HOOK` | câu chữ đầy đủ, **không viết tắt** | 🔴 |
| 12 | `CTA` | câu chữ đầy đủ | 🔴 |
| 13 | ★ `TRUY NGƯỢC` | `HT-031` hoặc `số liệu: ad #12 CTR −34%` | 🔴 |
| 14 | `KHU VỰC` | `Bắc` · `Nam` · `Miền Tây` · `Việt kiều` | 🟠 |
| 15 | `ĐƯỜNG CẢI TIẾN` | `nhân bản` · `biến thể` · `giữ ý bỏ hook` · `mới` | 🟠 |
| 16 | `CẦN QUAY?` | `có` → sinh dòng ở bảng ④ · `không` | 🔴 |
| 17 | `CỜ PHÁP CHẾ` | 🟢 · 🟡 · 🔴 | 🔴 |
| 18 | `GHI CHÚ` | lý do, điều kiện, ai duyệt | 🟠 |

### Hai cột không ai được bỏ

```
Cột 11 HOOK  — ⛔ phải là CÂU CHỮ THẬT, không phải mô tả.
               ⛔ SAI : "hook về ca khó"
               ✅ ĐÚNG: "Mũi đã nâng mà đầu mũi bóng đỏ — còn sửa lại được không?"

Cột 13 TRUY NGƯỢC — ⛔ trống là dòng BỊ LOẠI khỏi kế hoạch.
               Không truy ngược được = hook bịa (sp-C ⛔).
```

★ Cột 13 là **cột tự bảo vệ của cả agent**. Khi ai đó hỏi *"sao tuần này làm clip này?"*, cột 13 trả lời thay.

---

## 3. CÂN ĐỐI TUẦN — SÁU LUẬT

| Luật | Nội dung | Vì sao |
|---|---|---|
| ① | **Mỗi bác sĩ đang chạy có ≥ 1 bài `WORKSTYLE`** mỗi tuần | Ngắt chuyên môn là mất nhân hiệu |
| ② | Tỷ trọng ~**40% WORKSTYLE · 35% LIVESTYLE · 25% ADS** | `sp-E` §2 |
| ③ | ★ **≥ 1 ô CHALLENGER** mỗi tuần, **kể cả tuần số đẹp** | `sp-D` §5 — winner chết thì phải có sẵn đồ thay |
| ④ | **≥ 1 dòng cho ô ① của bảng giao** (`sp-C` §5) | Lỗ hổng là ưu tiên 1 |
| ⑤ | ⛔ **Không hai bác sĩ cùng chuyên khoa trùng format trong tuần** | Tự đấu giá (`sp-F` §3) |
| ⑥ | **Nấc rải đủ `A1`→`A4`**, ⛔ không dồn hết vào `A4` | Dồn `A4` là đốt tệp cũ, không nuôi tệp mới |

### ★ Luật ③ — ô challenger

```
Mỗi tuần, kế hoạch PHẢI có ≥ 1 dòng được đánh dấu [CHALLENGER]:
  · nội dung MỚI hoàn toàn, chưa từng chạy
  · nhắm cùng tệp với winner hiện tại
  · ngân sách nhỏ, chỉ để biết nó có sống không

⛔ Tuần nào bỏ ô này cũng được — cho tới tuần winner chết.
   Khi đó làm nội dung mới là ĐÃ CHẬM 7–10 NGÀY.
```

⚠️ Đây là luật **khó bán nhất cho người đọc kế hoạch**, vì nó tiêu tiền vào thứ chưa chắc thắng trong một tuần số đang đẹp. Vẫn giữ. Ghi kèm lý do mỗi tuần.

### Luật ⑥ — kiểm nhanh phân bố nấc

| Phân bố | Chẩn đoán |
|---|---|
| > 50% dòng ở `A4` | 🔴 Đang vắt tệp cũ. Tháng sau sẽ hết người để vắt |
| 0 dòng ở `A1` | 🔴 Không nuôi tệp mới. CPM sẽ tăng dần và không ai hiểu vì sao |
| > 60% hội thoại ở `A3` *(từ `sp-C` §3)* **và** kế hoạch cũng dồn `A3` | 🔴 Đang làm nặng thêm vấn đề — phễu thiếu `A1`–`A2`, không thiếu `A3` |

---

## 4. BẢNG ④ — ORDER SẢN XUẤT

Chỉ gồm dòng có `CẦN QUAY? = có`. Mục đích: **nối thẳng vào `Agent-OrderMedia`.**

| # | Cột | Ví dụ |
|---|---|---|
| 1 | `MÃ ORDER` | `OD-T45-MUI3-002` |
| 2 | `MÃ KẾ HOẠCH` | `KH-T45-007` |
| 3 | `DỊCH VỤ` | `Mũi` |
| 4 | `CHÂN DUNG` | `CD3` |
| 5 | `NẤC 5A` | `A2` |
| 6 | `FORMAT` | `L03` |
| 7 | `HOOK` | câu chữ đầy đủ |
| 8 | `CTA` | câu chữ đầy đủ |
| 9 | `BÁC SĨ` | `BS03 Huyên` |
| 10 | `KHU VỰC` | `Bắc` |
| 11 | `NGÀY CẦN XONG` | `31/10` |
| 12 | `ĐIỀU KIỆN CHẶN` | `cần consent CASE-01` · `cần BS duyệt mốc hồi phục` |

★ Cột 12 phải ghi **điều kiện chặn đã biết trước**, để ekip không xếp lịch quay một clip chưa có consent.

```
⛔ AGENT NÀY DỪNG Ở BẢNG ④.
   Lời thoại theo mốc giây, shot list, đạo cụ, call sheet → Agent-OrderMedia.
   Tự viết kịch bản chi tiết ở đây là bỏ qua cả thư viện khuôn kịch bản của nhà.
```

---

## 5. KHỐI ⑤ — CỜ PHÁP CHẾ

```
🔴 KH-T45-007 · L11 · "bảo hành trọn đời"
   VI PHẠM  : L04 — cam kết vượt khả năng chứng minh; chính sách chưa có văn bản
   THAY BẰNG: "Chính sách bảo hành bằng văn bản — bác sĩ tư vấn trực tiếp"
   CHẶN     : dòng này không đăng cho tới khi có văn bản
```

⛔ **Cờ không có dòng `THAY BẰNG` là cờ chưa hoàn thành.** Gắn cờ rồi để đó là đẩy việc sang người khác — xem `sp-A` §4.

---

## 6. KHỐI ⑥ — [CHỜ XÁC NHẬN]

In **mỗi lần xuất kế hoạch**, kể cả khi lặp lại y nguyên tuần trước. Ba cột:

| Thứ còn thiếu | Ai cấp | Chặn mấy dòng |
|---|---|---|

⚠️ Cột **"chặn mấy dòng"** là cột làm việc này được giải quyết. *"Thiếu bảng giá"* thì không ai vội; *"Thiếu bảng giá → chặn 9 dòng kế hoạch tuần này"* thì có người xử.

---

## 7. ĐỊNH DẠNG FILE

| Yêu cầu | Luật |
|---|---|
| Bảng ③ ④ | CSV / sheet — **một dòng một bài**, ⛔ không gộp ô |
| Cột `HOOK` `CTA` | Văn bản thuần, ⛔ không xuống dòng trong ô |
| Mã | ⛔ Không đổi mã giữa các bảng — `KH-T45-007` ở bảng ③ phải là `KH-T45-007` ở bảng ④ |
| Số | Theo quy ước `sp-D` §1 — `412k`, `18,2tr`, `1,8%` |
| Khối ⑤ ⑥ | Văn bản, ⛔ không nhét vào bảng |

⛔ **Không trang trí.** Không khung, không màu nền, không icon trang trí. Cờ 🟢🟡🔴 là **dữ liệu**, không phải trang trí.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Đủ 4 bảng + 2 khối chưa?
- [ ] Cột `HOOK` có phải **câu chữ thật** không, hay là mô tả?
- [ ] Mọi dòng có cột `TRUY NGƯỢC` không? Dòng trống đã bị loại chưa?
- [ ] Có **≥ 1 ô CHALLENGER** không?
- [ ] Có **≥ 1 dòng cho lỗ hổng ô ①** không?
- [ ] Phân bố nấc có dồn `A4` không? Có dòng `A1` nào không?
- [ ] Hai bác sĩ cùng chuyên khoa có trùng format không?
- [ ] Mỗi cờ 🔴 có **câu thay thế** không?
- [ ] Khối `[CHỜ XÁC NHẬN]` có ghi **chặn mấy dòng** không?
- [ ] Đã dừng đúng ở bảng ④, không lấn sang kịch bản chi tiết chứ?
