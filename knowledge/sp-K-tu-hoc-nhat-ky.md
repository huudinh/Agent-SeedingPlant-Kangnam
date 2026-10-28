# sp-K · TỰ HỌC & NHẬT KÝ TUẦN

> Sổ này trả lời: **"khả năng tự học" thực ra là cái gì, học vào đâu, và tuần sau đọc lại ở chỗ nào.**

---

## 1. ⚠️ NÓI THẲNG: AGENT KHÔNG TỰ NHỚ

```
⛔ Agent KHÔNG nhớ gì giữa hai phiên làm việc.
   Dán 100 hội thoại tuần này, tuần sau mở phiên mới → agent không nhớ gì cả.
```

**"Khả năng tự học" của hệ này không nằm trong model. Nó nằm trong MỘT FILE.**

| Cách hiểu sai | Cách làm đúng |
|---|---|
| *"Agent dùng lâu sẽ tự giỏi lên"* | **Agent ghi ra cái đã học → người dán lại vào phiên sau** |
| *"Cứ dán dữ liệu hàng tuần là nó tự tích luỹ"* | **Dán dữ liệu + dán NHẬT KÝ của các tuần trước** |

★ Vì vậy mỗi lần xuất kế hoạch, agent **bắt buộc xuất kèm khối `NHẬT KÝ TUẦN`** ở §3 — đó là bộ nhớ duy nhất mà hệ này có.

⚠️ Khối nhật ký không phải báo cáo trang trí. **Không dán lại nhật ký vào tuần sau thì tuần sau agent sẽ đề xuất lại đúng những hook đã chết.**

---

## 2. BA THỨ ĐÁNG HỌC, BA THỨ KHÔNG

| ✅ Đáng ghi vào nhật ký | ⛔ Không đáng ghi |
|---|---|
| **Hook đã chạy + kết quả** — sống bao lâu, chấm gì | Mọi con số chi tiết của từng ad *(đã có ở báo cáo Ads)* |
| **Luật mới rút ra** — điều gì lặp lại 3 lần thì thành luật | Cảm nhận chủ quan *(“clip này nhìn hay hơn”)* |
| **Lý do ad bị từ chối** — lặp lại 3 lần thì viết vào `sp-H` | Việc đã xử xong, không tái diễn |

### Luật "ba lần thành luật"

```
Một việc xảy ra 1 lần  → ghi nhận
Một việc xảy ra 2 lần  → theo dõi
Một việc xảy ra 3 lần  → ★ VIẾT THÀNH LUẬT trong sổ tương ứng, không ghi nhật ký nữa
```

| Việc lặp 3 lần | Viết vào |
|---|---|
| Một kiểu hook luôn KÉM | `sp-F` §4 — thêm vào danh sách `H1`–`H7` |
| Một lý do từ chối ad | `sp-H` §2 — thêm vào danh sách 🔴/🟡 |
| Một mã `O` luôn cao mà nội dung không đóng được | `sp-C` §2 — ghi chú riêng cho mã đó |
| Một bác sĩ luôn từ chối một format | `sp-I` §3 — ghi vào ranh giới người đó |
| Một ngưỡng chỉ số bắn mà không ai xử | `sp-D` — nới ngưỡng hoặc bỏ |

★ **Nhật ký phình to là dấu hiệu xấu**, không phải dấu hiệu chăm chỉ. Nhật ký tốt là nhật ký **ngắn dần**, vì những gì học được đã chuyển thành luật trong các sổ.

---

## 3. ★ KHỐI `NHẬT KÝ TUẦN` — ĐẦU RA BẮT BUỘC

In ở cuối mỗi kế hoạch. Năm phần:

```
═══ NHẬT KÝ TUẦN 45 ═══

① SỔ HOOK
   hook                                    | chấm | tuần đã chạy | việc tuần này
   "Mũi đã nâng mà đầu mũi bóng đỏ..."     | 🟢   | T43,T44,T45  | nhân bản sang CD4
   "Hội thảo lột xác - giá sốc"            | 🔴   | T44          | bỏ hẳn (H7)
   "Cắt mí mấy ngày đi làm được?"          | 🟡   | T45          | biến thể đổi 3s đầu

② LUẬT MỚI RÚT RA TUẦN NÀY
   [lần 1] Hook có từ "hội thảo" chấm KÉM — theo dõi
   [lần 3] ★ Ad nêu tên thương mại vật liệu bị từ chối lần thứ 3
           → VIẾT VÀO sp-H §2 danh sách 🟡. Không ghi nhật ký nữa.

③ ĐANG THEO DÕI (chưa đủ 3 lần)
   · Nội dung LIVESTYLE của BS02 giữ chân cao bất thường — 2/3 lần
   · O-11 (người nhà phản đối) tăng từ 4 → 9 lần/100 — 2 tuần liên tiếp

④ DỰ ĐOÁN TUẦN NÀY + ĐỐI CHIẾU TUẦN TRƯỚC
   Tuần trước dự đoán: "L03 của BS03 sẽ giữ CPL dưới median"  → ✅ ĐÚNG (382k vs 412k)
   Tuần trước dự đoán: "hook giá sẽ thắng ở CD4"              → ❌ SAI (CTR −22%)
   Tuần này dự đoán  : "O-09 Việt kiều chưa ai làm → L10 sẽ có tỷ lệ inbox cao"

⑤ VIỆC CHẶN CÒN TỒN (từ tuần nào)
   · Chính sách bảo hành bằng văn bản — tồn từ T41, chặn 9 dòng
   · Đối chiếu chứng chỉ BS01 BS02 — tồn từ T44, chặn 6 dòng
```

### ★ Phần ④ là phần làm nên sự khác biệt

```
Agent phải GHI DỰ ĐOÁN TRƯỚC, rồi tuần sau tự đối chiếu ĐÚNG/SAI.
```

| Vì sao bắt buộc | |
|---|---|
| ① | Không ghi dự đoán thì **mọi kết quả đều giải thích được sau khi đã biết** — và không ai học được gì |
| ② | Tỷ lệ dự đoán đúng là **chỉ số sức khoẻ của chính agent**. Dưới 50% nghĩa là tri thức trong các sổ đang sai, không phải thị trường khó |
| ③ | Dự đoán SAI là thứ đáng ghi nhất. ⛔ **Không được lặng lẽ bỏ dự đoán sai** khỏi nhật ký |

⚠️ ⛔ **Không sửa dự đoán cũ cho khớp kết quả.** Nếu phát hiện dự đoán tuần trước ghi sai chỗ, ghi thêm dòng đính chính — ⛔ không xoá dòng cũ.

### Phần ⑤ — việc chặn phải có TUỔI

Ghi *"thiếu bảng giá"* thì không ai vội. Ghi *"thiếu bảng giá — tồn từ T41, chặn 9 dòng"* thì có người xử.
★ Một việc chặn tồn **> 4 tuần** → đẩy lên thành một dòng riêng ở đầu kế hoạch, không để trong nhật ký nữa.

---

## 4. NHỊP VẬN HÀNH TUẦN

| Thứ | Việc | Ai |
|---|---|---|
| **T2** | Đọc số tuần trước *(B2)* — số đã về đủ | Khối Ads + agent |
| **T3** | Bóc hội thoại *(B3)* + ghép chân dung *(B4)* | Agent |
| **T4** | ★ **Duyệt hook** — chốt hook & format với từng bác sĩ | Content Lead + bác sĩ |
| **T5** | Giao order sản xuất | → `Agent-OrderMedia` |
| **T6–CN** | Quay, dựng | Ekip |
| **T2 tuần sau** | Đăng theo lịch | Biên tập cơ sở |

★ **Thứ Tư là ngày quan trọng nhất.** Hook không được bác sĩ duyệt vào T4 thì T5 không giao được order, và cả tuần trôi. ⛔ Đừng gửi hook cho bác sĩ vào T6.
⚠️ `BS01` *(hay dỗi marketing, ít dùng thiết bị di động)* → chốt **một lần vào T4**, ⛔ không đổi giữa tuần (`sp-I` §3).

---

## 5. KHI NÀO SỬA TRI THỨC, KHI NÀO CHỈ GHI NHẬT KÝ

| Tình huống | Làm gì |
|---|---|
| Một hook chết | Ghi nhật ký ① |
| Ba hook cùng kiểu cùng chết | ★ Sửa `sp-F` §4 |
| Khối vận hành cấp bảng giá mới | ★ Sửa `sp-J` §4 — ⛔ không ghi nhật ký |
| Một bác sĩ được xác minh chứng chỉ | ★ Sửa `sp-I` §2 — ⛔ không ghi nhật ký |
| Một bác sĩ nghỉ việc / bật lại | ★ Sửa `sp-I` §1 **ngay**, kèm rà soát nội dung cũ |
| Facebook đổi luật | ★ Sửa `sp-E`, đánh dấu `[ĐỐI CHIẾU LẠI]` ngày sửa |
| Ngưỡng chỉ số bắn hoài không ai xử | ★ Sửa `sp-D` |

```
⛔ LUẬT: dữ kiện ĐƠN VỊ (giá, giấy phép, bác sĩ) luôn sửa vào sp-I / sp-J.
   ⛔ KHÔNG BAO GIỜ để dữ kiện đơn vị sống trong nhật ký — nhật ký không ai đọc lại
   khi cần tra một con số, và sẽ có người dùng lại số cũ.
```

★ Sau mỗi lần sửa sổ `knowledge/` → chạy lại `tools/gop-tham-khao.py` để gói tri thức khớp lại.

---

## 6. TỰ KIỂM SỔ NÀY

- [ ] Đã in khối `NHẬT KÝ TUẦN` đủ 5 phần chưa?
- [ ] Phần ④ có **dự đoán cho tuần này** không?
- [ ] Phần ④ có **đối chiếu dự đoán tuần trước**, kể cả cái SAI không?
- [ ] Có việc nào lặp lần thứ 3 mà chưa được **viết thành luật** không?
- [ ] Việc chặn có ghi **tồn từ tuần nào** và **chặn mấy dòng** không?
- [ ] Có dữ kiện đơn vị *(giá, giấy phép, bác sĩ)* nào đang nằm trong nhật ký thay vì trong `sp-I`/`sp-J` không?
- [ ] Nhật ký tuần này có **ngắn hơn** tuần trước không? *(dài ra là dấu hiệu không chuyển hoá được thành luật)*
