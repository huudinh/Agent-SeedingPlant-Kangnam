# sp-I · MODULE ĐƠN VỊ — BÁC SĨ KANGNAM

> ⚠️ **Đây là module đơn vị về CON NGƯỜI.** Mọi dữ kiện riêng của từng bác sĩ — trạng thái chạy, chuyên khoa, tính cách, kênh, trạng thái xác minh — nằm ở đây.
> **Đổi đơn vị → thay file này + `sp-J`, KHÔNG sửa `SYSTEM-PROMPT.md` hay các sổ `sp-A`…`sp-H`.**
>
> ⛔ **Luật tối thượng của sổ này:** dữ kiện **về một con người** đưa lên truyền thông phải là dữ kiện **đã xác minh**. Thà thiếu một dòng giới thiệu hơn mất chứng chỉ hành nghề của người khác.

---

## 0. ⚠️ ĐỘ TIN CỦA SỔ NÀY

| Dấu | Nghĩa |
|---|---|
| ✅ **DỮ KIỆN** | Lấy nguyên từ sheet hồ sơ bác sĩ nội bộ |
| 🔶 **SUY RA** | Agent suy ra từ dữ kiện — dùng được, nhưng ghi rõ là suy ra |
| ⚠️ **CHƯA CÓ DỮ LIỆU** | ⛔ Không điền bừa |

```
⛔ SỔ NÀY CHỨA DỮ LIỆU CÁ NHÂN.
   Sheet nguồn có email và MẬT KHẨU đăng nhập của từng tài khoản.
   → ⛔ Đã CỐ Ý loại khỏi sổ này. ⛔ Không bao giờ chép lại vào đây.
   → ⛔ Không in SĐT cá nhân ra đầu ra, dù sheet nguồn có.
```

---

## 1. TOÀN CẢNH — 8 BÁC SĨ TRONG HỒ SƠ

| Mã | Tên | Tên thương hiệu | Chuyên khoa | Khu vực | Trạng thái QC | Biên tập |
|---|---|---|---|---|---|---|
| `BS01` | Vũ Hữu Chỉnh | Dr. Victor Vũ | Hàm mặt | Bắc | 🟢 **Đang chạy** | Phương |
| `BS02` | Nguyễn Đức Quỳnh | Daniel Nguyễn | Cấy mỡ, thẩm mỹ mắt | Bắc | 🟢 **Đang chạy** | Phương |
| `BS03` | Nguyễn Văn Huyên | Henry Nguyễn | Thẩm mỹ mắt, thẩm mỹ mũi | Bắc | 🟢 **Đang chạy** | Linh |
| `BS04` | Nguyễn Khắc Hảo | Dr. Edward Nguyễn | Hàm mặt | Nam | 🟢 **Đang chạy** | Luyến |
| `BS05` | Hoàng Văn Tiệm | Dr. Lucas Hoàng | Cắt mí, nâng ngực, cấy tóc | Nam | 🟢 **Đang chạy** | Luyến |
| `BS06` | Nguyễn Mạnh Cường | Galvin Nguyễn | Nâng ngực, hút mỡ | Bắc | ⛔ **Dừng** | Linh |
| `BS07` | Nguyễn Quốc Chí | Harvey Nguyễn | Nâng mũi, cắt mí | Nam | 🔴 **Dừng + vướng chứng chỉ** | Luyến |
| `BS08` | Nguyễn Hữu Đoàn | Mark Nguyễn | Cấy mỡ, tạo hình khuôn mặt | Nam | ⛔ **Dừng** | Luyến |

✅ Nguồn: sheet hồ sơ bác sĩ nội bộ.

```
★ CHỈ 5/8 ĐANG CHẠY.  ⛔ BS06 · BS07 · BS08 KHÔNG CÓ DÒNG NÀO TRONG KẾ HOẠCH TUẦN.
```

⚠️ **Website công bố "15 bác sĩ", hồ sơ nội bộ chỉ có 8.** Trang đội ngũ còn có ít nhất ba người không có trong hồ sơ: **Dr. Richard Huy · Dr. Felix Trần · Dr. Frankie Vũ**.
→ ⛔ Agent **không lập kế hoạch cho người không có trong hồ sơ** — không biết trạng thái, không biết chuyên khoa, không biết ai biên tập.
→ ⚠️ `[CHỜ XÁC NHẬN]` — ba người này có nằm trong phạm vi seeding không?

---

## 2. 🔴 TRẠNG THÁI XÁC MINH CHỨNG CHỈ — PHẦN QUAN TRỌNG NHẤT

> Đây là **cổng chặn nặng nhất của cả agent**. Đọc trước khi gắn bất kỳ tên nào vào bất kỳ dòng nào.

| Bác sĩ | Kết quả tra cứu | Hệ quả |
|---|---|---|
| `BS01` **Vũ Hữu Chỉnh** | 🔴 **Không tra ra thông tin** trên cổng tra cứu | ⛔ **Không nêu chức danh / bằng cấp / số năm / số ca** |
| `BS02` **Nguyễn Đức Quỳnh** | 🔴 **Tra ra tên bác sĩ khác** | ⛔ **Không nêu chức danh / bằng cấp / số năm / số ca** |
| `BS07` **Nguyễn Quốc Chí** | 🔴 **Trạng thái: nghỉ việc từ năm trước** | ⛔ **Không nhắc tên. Phải rà soát & gỡ nội dung cũ** (`sp-H` §3d) |
| `BS03` `BS04` `BS05` `BS06` `BS08` | ⚠️ **Chưa ghi nhận vấn đề, cũng chưa ghi nhận ĐÃ ĐỐI CHIẾU XONG** | 🟡 Nêu chức danh ở mức **đã có trên website chính thức**, ⛔ không thêm |

✅ Nguồn: tab rà soát hồ sơ E-E-A-T trong sheet bác sĩ.

### Hệ quả cụ thể cho kế hoạch tuần

```
⛔ BS01 và BS02 — ĐANG CHẠY QUẢNG CÁO nhưng VƯỚNG chứng chỉ.

→ Vẫn được lên kế hoạch nội dung CHUYÊN MÔN:
     ✅ giải thích kỹ thuật · phân tích ca · quan điểm nghề · livestyle
→ ⛔ KHÔNG được kèm claim về bản thân:
     ⛔ "Trưởng khoa RHM"  ⛔ "19 năm kinh nghiệm"  ⛔ "14.250 ca"
→ Mọi dòng của hai người này mang cờ 🟡 và ghi chú:
     "⚠️ chưa đối chiếu được chứng chỉ — bỏ mọi claim về chức danh/kinh nghiệm"
```

★ **Ranh giới một câu:** *bác sĩ được nói về NGHỀ, chưa được nói về MÌNH.*

⚠️ **Đây là phát hiện nặng, không phải chi tiết kỹ thuật.** Hai bác sĩ đang chạy quảng cáo với chức danh "Trưởng khoa" / "Phó khoa" trong khi chứng chỉ chưa tra ra hoặc tra ra người khác — chạm `L01` + `L02` + `L08` cùng lúc.

```
⚠️ [CHỜ XÁC NHẬN] — ai cấp: khối vận hành + pháp chế   ★ CẤP BÁCH NHẤT
   ① Đối chiếu chứng chỉ hành nghề BS01, BS02 — đúng tên, đúng phạm vi, còn hiệu lực
   ② Văn bản bổ nhiệm chức danh của từng người
   ③ Xác nhận BS07 đã nghỉ việc → rà soát toàn bộ nội dung cũ có tên người này
```

---

## 3. HỒ SƠ NHÂN HIỆU TỪNG NGƯỜI

> Dùng để viết nội dung `WORKSTYLE` / `LIVESTYLE`. Chỉ 4/8 người có dữ liệu đời sống.

### `BS01` · Vũ Hữu Chỉnh — *"Chuẩn như bác Chỉnh"*

| | |
|---|---|
| **Chuyên khoa** | Hàm mặt ✅ |
| **Tính cách thương hiệu** | Chuẩn chỉnh · chuyên môn cao · chân thật · hài hước ✅ |
| **Vai đặc biệt** | Bác sĩ mổ chính của chương trình thực tế lột xác ✅ |
| **Đời sống** | Pickleball · bia · karaoke · tụ tập · đọc thơ, hát vu vơ ✅ |
| ⛔ **Ranh giới** | ★ **Không thích quay, lên hình.** Ít dùng thiết bị di động ✅ |
| **Cách dạy nghề** | Đố điều dưỡng *"với ca này, đố các em phải làm thế nào?"* ✅ |
| **Hay dỗi khi** | Khách không làm theo chỉ định · dỗi marketing ✅ |
| **Người đó muốn** | ★ Một tuyến **bài chào buổi sáng đăng hàng ngày** · nội dung các ngày lễ · **3 bài/ngày** đủ cả livestyle, workstyle, ads ✅ |

🔶 **Cách ghép format:** người này **ngại camera nhưng thích dạy**. → ⛔ Tránh `L02` talk dài trước ống kính. ✅ Dùng `L03` *(phân tích ca — nói qua ảnh/CT, ít thời lượng khuôn mặt)*, **ảnh + caption dài**, và biến *"đố điều dưỡng"* thành một tuyến riêng: bác sĩ ra đề cho ekip trong lúc làm việc — người đó đang làm việc mình thích, không phải diễn.

⚠️ *"Hay dỗi marketing"* là dữ kiện vận hành thật: ⛔ **đừng đổi format của người này giữa tuần**. Chốt trước cả tuần, một lần.

### `BS02` · Nguyễn Đức Quỳnh

| | |
|---|---|
| **Chuyên khoa** | Cấy mỡ *(cấy mỡ đa tầng)* · thẩm mỹ mắt ✅ |
| **Tính cách** | Nhanh nhạy · học vấn cao · vui vẻ · luôn cập nhật xu hướng, công nghệ mới ✅ |
| **Đời sống** | Gia đình *(vợ con, bố mẹ)* · **đu trend MXH kể cả nhảy** · học tập · chia sẻ báo/sách/podcast ✅ |

🔶 **Cách ghép format:** người duy nhất trong hồ sơ **chịu đu trend** → `L09` công nghệ + định dạng động, Reels. ✅ `LIVESTYLE` dễ nhất trong cả nhóm.
⚠️ Vướng chứng chỉ *(§2)* → ⛔ bỏ mọi claim *"học vấn cao"*, *"9 năm"*, *"8.000 ca"*.

### `BS03` · Nguyễn Văn Huyên — *"Ca mũi khó, có bác Huyên"* ★

| | |
|---|---|
| **Chuyên khoa** | Thẩm mỹ mắt · thẩm mỹ mũi *(mũi khó, sửa hỏng)* ✅ |
| **Tính cách** | Kĩ tính · sâu lắng · thẳng thắn ✅ |
| **Câu cửa miệng** | *"chị hiểu chứ"* ✅ |
| **Đời sống** | Phong cách tổng tài · học tập từ bác sĩ khác, hội thảo · hát trong khi mổ để giải toả căng thẳng cho khách · trêu khách · sinh hoạt khoa học ✅ |
| **Công tác tỉnh** | Thanh Hoá — hay chia sẻ ẩm thực, du lịch địa phương, **gu thẩm mỹ khác biệt giữa các vùng miền** ✅ |

★ **Đây là bác sĩ mạnh nhất cho `CD3` *(sửa lại)* và `O-05`.** *"Ca mũi khó, có bác Huyên"* là khẩu hiệu **đã có sẵn**, gắn thẳng vào tuyến `L03`.
🔶 Chi tiết *"gu thẩm mỹ khác biệt giữa các vùng miền"* là **nguyên liệu hiếm**: nó đóng được luật port vùng miền (`sp-D` §7) bằng giọng của chính bác sĩ.

### `BS06` · Nguyễn Mạnh Cường

| | |
|---|---|
| **Chuyên khoa** | Nâng ngực · hút mỡ ✅ · ⛔ **ĐANG DỪNG** |
| **Tính cách** | Thân thiện · nhẹ nhàng · cẩn thận · ấm áp · giản dị ✅ |
| **Đời sống** | Giản dị trong ăn mặc, du lịch, thể thao · **đi xe máy wave** · bắt mạch cho khách · hay đeo tai nghe · chia sẻ nhiều về gia đình ✅ |

⚠️ Hồ sơ `LIVESTYLE` **tốt nhất trong cả nhóm** nhưng người này **đang dừng quảng cáo** → ⛔ không lên kế hoạch. 🔶 Nếu bật lại, đây là người dựng nhân hiệu nhanh nhất.
🔴 **Mâu thuẫn số liệu:** cột hồ sơ ghi *6 năm · ~3.000 ca*, phần mô tả ghi *6 năm · 6.000 ca*. → ⛔ **Không dùng con số nào** cho tới khi chốt.

### `BS04` `BS05` `BS07` `BS08` — ⚠️ CHƯA CÓ DỮ LIỆU TÍNH CÁCH

```
⚠️ Bốn người này chỉ có: chuyên khoa · khu vực · tính cách một dòng · kênh.
   ⛔ KHÔNG có dữ liệu livestyle/workstyle.

→ 🔶 Hệ quả: chỉ lên được nội dung WORKSTYLE dạng chuyên môn chung.
→ ⛔ KHÔNG tự bịa sở thích, đời sống, câu cửa miệng cho họ.
→ BS04 BS05 đang CHẠY mà thiếu dữ liệu này là LỖ HỔNG ĐÁNG LẤP NHẤT (§6).
```

Dữ kiện có sẵn:
- `BS04` **Nguyễn Khắc Hảo** — hàm mặt · Nam · *"Quyết nhanh, làm gọn"* · 🔶 *bên ngoài tưởng cứng nhắc nhưng ấm áp bên trong* ✅
- `BS05` **Hoàng Văn Tiệm** — cắt mí, nâng ngực, cấy tóc · Nam · *ham học, học mọi lúc mọi nơi; hướng nội với cuộc sống, hướng ngoại với chuyên môn và bệnh nhân* ✅
- `BS07` **Nguyễn Quốc Chí** — 🔴 **nghỉ việc**, ⛔ không dùng
- `BS08` **Nguyễn Hữu Đoàn** — cấy mỡ, tạo hình mặt · Nam · *hàn lâm, thích chia sẻ, học thuật* ✅ · ⛔ đang dừng

```
🔴 LỖI DỮ LIỆU: BS08 Nguyễn Hữu Đoàn đang mang khẩu hiệu
   "Trẻ hóa tự nhiên, chọn bác Quỳnh"  — tên trong khẩu hiệu là BS02.
→ Nhiều khả năng là lỗi chép trong sheet nguồn.
→ ⛔ Không dùng khẩu hiệu này cho bất kỳ ai cho tới khi được xác nhận.
```

---

## 4. ⚠️ SỐ NĂM & SỐ CA — ĐANG CÓ MÂU THUẪN

| Bác sĩ | Cột hồ sơ | Mô tả tự do | Trạng thái |
|---|---|---|---|
| `BS01` | 19 năm · ~14.250 ca | 19 năm · 14.250 ca | ✅ khớp — nhưng 🔴 **vướng chứng chỉ** → chưa dùng |
| `BS02` | 9 năm · ~8.000 ca | 9 năm · ~8.000 ca | ✅ khớp — nhưng 🔴 **vướng chứng chỉ** → chưa dùng |
| `BS03` | 12 năm · >13.000 ca | 12 năm · >13.000 ca | 🟡 dùng được, ⚠️ ghi *"theo hồ sơ nội bộ"* |
| `BS06` | 6 năm · **~3.000** ca | 6 năm · **6.000** ca | 🔴 **XUNG ĐỘT — ⛔ không dùng** |
| `BS04` `BS05` `BS07` `BS08` | có số | không có mô tả | 🟡 chưa đối chiếu nguồn đếm |

⚠️ **Website công bố "3.000.000+ ca" toàn hệ thống** — con số này ⛔ **không chia được cho từng bác sĩ** và ⛔ không dùng thay cho số ca cá nhân.

```
⛔ LUẬT: số năm và số ca là CLAIM VỀ MỘT CÁ NHÂN (L01 L04).
   Không có nguồn đếm rõ ràng → viết "bác sĩ chuyên khoa [X]" không kèm số.
```

---

## 5. KÊNH CỦA TỪNG BÁC SĨ

| Bác sĩ | Page FB | TikTok | YouTube | Web |
|---|---|---|---|---|
| `BS01` | ✅ | ✅ | ⚠️ chưa có | ✅ |
| `BS02` | ✅ | ✅ | ⚠️ chưa có | ✅ |
| `BS03` | ✅ | ✅ | ✅ | ✅ |
| `BS04` | ✅ | ⚠️ chưa có | ✅ | ✅ |
| `BS05` | ✅ | ✅ | ✅ | ✅ |
| `BS06` | ✅ | ✅ | ✅ | ✅ |
| `BS07` | ✅ | ⚠️ chưa có | ⚠️ | ✅ |
| `BS08` | ✅ | ⚠️ chưa có | ✅ | ✅ |

⚠️ **Mọi người đều có trang hồ sơ trên website chính thức.** → Đây là nguồn **duy nhất đã công khai** để trích chức danh, trong lúc chờ đối chiếu chứng chỉ.

★ `BS03` là người **duy nhất đủ cả 4 kênh** → ưu tiên thử nghiệm nội dung đa nền tảng ở người này trước.

---

## 6. ★ LỖ HỔNG E-E-A-T — XẾP THEO ĐÒN BẨY

Rút từ tab rà soát hồ sơ. Đây là **việc ngoài Facebook** nhưng ảnh hưởng trực tiếp tới mã `O-05` và `O-06`.

| # | Lỗ hổng | Ảnh hưởng | Ai xử |
|---|---|---|---|
| ① | 🔴 **Chứng chỉ 3 người chưa đối chiếu được** | ⛔ Chặn mọi claim chức danh | Vận hành + pháp chế |
| ② | 🔴 **BS04 BS05 đang chạy mà không có dữ liệu tính cách** | ⛔ Không làm được `LIVESTYLE` → nhân hiệu đứng im | Biên tập cơ sở *(Luyến)* |
| ③ | 🟠 **Chưa có case khách hàng chuẩn hoá** *(tình trạng · phương pháp · thời gian · kết quả · ai mổ · ở đâu)* | Thiếu bằng chứng cho `L03` `L08` | Vận hành |
| ④ | 🟠 **Chưa có báo chí** — chưa có bài phỏng vấn/trích dẫn trên báo lớn hay báo chuyên ngành | `O-05` `O-06` không đóng được bằng Facebook một mình | PR |
| ⑤ | 🟡 **Chưa có LinkedIn, site/blog riêng** | Mất nguồn để AI trích dẫn | → `Agent-KN-GEO-Plant` |
| ⑥ | 🟡 **Chưa có Google Maps hồ sơ bác sĩ** | Mất tín hiệu địa phương | GEO |
| ⑦ | 🟡 **Thiếu TikTok / YouTube ở một số người** | Mất kênh phân phối | Biên tập |
| ⑧ | 🟡 **Chưa rõ page nào đã có tích xanh** | `O-06` | Vận hành |

★ **Mục ② là mục agent này có thể tự đẩy nhanh nhất**: nó chỉ cần **một buổi phỏng vấn 30 phút** với mỗi bác sĩ, theo đúng khung mà `BS01`/`BS03` đã có. ⛔ Không cần ngân sách, không cần pháp chế.

⚠️ **Mục ④ ⑤ ⑥ không phải việc của agent này** — nhưng phải **in vào đầu ra** khi `O-05` cao, vì Facebook một mình không đóng nổi `O-05` (`sp-E` §3).

---

## 7. BẢNG CHẶN TỔNG — TRA NHANH

| Dòng kế hoạch loại này | Bị chặn bởi | Trạng thái |
|---|---|---|
| Có tên `BS06` `BS07` `BS08` | §1 | ⛔ **CHẶN** — đang dừng |
| Nội dung cũ còn tên `BS07` | §2 | 🔴 **GỠ / DỪNG PHÂN PHỐI** |
| Nêu **chức danh / bằng cấp / số năm / số ca** của `BS01` `BS02` | §2 | 🔴 **CHẶN** |
| Dùng số ca của `BS06` | §4 | 🔴 **CHẶN** — hai nguồn xung đột |
| Dùng khẩu hiệu *"Trẻ hoá tự nhiên, chọn bác Quỳnh"* | §3 | 🔴 **CHẶN** — sai tên trong sheet |
| Nội dung `LIVESTYLE` cho `BS04` `BS05` | §3 | 🟡 **HỎI LẠI** — chưa có dữ liệu, ⛔ không bịa |
| Bác sĩ nói kỹ thuật **ngoài chuyên khoa của mình** | `sp-H` L02 | 🔴 **CHẶN** |
| Kế hoạch cho người **không có trong hồ sơ** *(Richard Huy, Felix Trần, Frankie Vũ)* | §1 | 🟡 **HỎI LẠI** |
| `L02` talk dài trước camera cho `BS01` | §3 | 🟡 **ĐỔI FORMAT** — người đó không thích lên hình |

★ **Bốn thứ cần xin để mở phần lớn các chặn trên:**
`① đối chiếu chứng chỉ BS01 BS02 + văn bản bổ nhiệm chức danh` · `② dữ liệu tính cách/đời sống cho BS04 BS05` · `③ chốt số ca BS06` · `④ xác nhận phạm vi seeding có gồm 3 bác sĩ chỉ có trên website không`.

Agent **in bốn dòng này vào khối `[CHỜ XÁC NHẬN]` mỗi lần xuất kế hoạch**, cho tới khi được cấp.

⚠️ **Mục ① là mục cấp bách nhất.** Hai bác sĩ **đang chạy quảng cáo** với chức danh chưa đối chiếu được — đây không phải bất tiện nội bộ mà là rủi ro pháp chế **đang phát sinh**.

---

## 8. TỰ KIỂM SỔ NÀY

- [ ] Mọi dòng có tên bác sĩ đã tra §1 *(trạng thái chạy)* và §2 *(xác minh)* chưa?
- [ ] Có claim chức danh/số năm/số ca nào của `BS01` `BS02` lọt ra không?
- [ ] Có dòng nào của `BS06` `BS07` `BS08` không?
- [ ] Có bịa sở thích/đời sống cho `BS04` `BS05` `BS07` `BS08` không?
- [ ] Format của `BS01` có bắt người đó nói dài trước camera không?
- [ ] Có email / SĐT / mật khẩu nào lọt ra không?
- [ ] Đã in khối `[CHỜ XÁC NHẬN]` với bốn mục ở §7 chưa?
