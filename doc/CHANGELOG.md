# CHANGELOG

---

## v1.0.1 — 2026-10-28

### Sửa khung mô tả trong `README.md`

🔴 **Lỗi của tôi khi dựng:** README đóng khung agent là *"kế hoạch nội dung tuần → order sản xuất"*, trong khi trọng tâm thật là **tối ưu quảng cáo Ads cho từng bác sĩ**. Bàn giao sang `Agent-OrderMedia` bị đẩy lên thành đích đến, còn chỉ số thì nằm chìm trong sổ.

| Cũ | Mới |
|---|---|
| *"Biến số liệu + hội thoại + hồ sơ bác sĩ → kế hoạch nội dung tuần"* | **"Tối ưu quảng cáo Ads cho từng bác sĩ Kangnam"** |
| Sơ đồ chảy thẳng xuống `Agent-OrderMedia` như đích | OrderMedia là nhánh phụ *"dòng nào cần quay"* |
| Chỉ số nằm trong `sp-D` | **Bảng `CPI`/`CPL`/`CPB`/`CTR`/`CPM` lên trang chủ**, kèm cột *agent có cải thiện được không* |
| — | Thêm **công thức phân rã CPL** và **bảng chấm nội dung + 4 đường cải tiến** vào README |
| — | Thêm dòng ⛔ *"Đây KHÔNG phải agent sản xuất video"* ngay đầu |

⚠️ **Bộ não và 11 sổ tri thức không đổi** — `sp-D` và `sp-F` vốn đã là tri thức tối ưu ads. Chỗ lệch chỉ ở lớp mô tả.

⚠️ **Còn tồn, chưa sửa:** `sp-G` vẫn đặt tên bảng ④ là *"ORDER SẢN XUẤT"* ngang hàng bảng kế hoạch, và `sp-K` §4 xếp nhịp tuần theo lịch quay thay vì theo chu kỳ lên/tắt ad.

### Thêm trang hướng dẫn

`tools/trang-huong-dan.py` + `tools/huong-dan.json` → **https://claude.ai/artifact/7vzxFRWdcCg2vQpK5SSEWv**

- Generator **dùng chung** với `Agent-QC-Telesale` · `Agent-Order-SoLieu` · `Agent-Media` · `Agent-PBP` · `Agent-KN-GEO-Plant`. Lấy bản đã vá `<meta name="viewport">` từ `Agent-OrderMedia-Kangnam`.
- Nội dung: 3 thẻ copy · **17 file tri thức** · **35 prompt** theo 7 nhóm · 12 câu smoke test · 5 điều phải biết · 6 việc đang chặn.
- Trang đóng khung theo **tối ưu ads**: Điều 1 là *phân rã CPL trước, kết luận sau*; smoke test câu 1 là *"CPL tăng 40%, làm hook mới nhé?"* → ⛔ chưa.
- ⛔ `tools/huong-dan.html` không commit — artifact sinh ra, không phải nguồn.

**Lỗi gặp khi dựng:** generator báo `KeyError: 'goi'` — thẻ nào không phải `brain`/`ngan` thì bắt buộc có khoá `"file"` trỏ tới file nguồn. Đã ghi cảnh báo vào `doc/02-cau-lenh.md`.

---

## v1.0 — 2026-10-28

Bản đầu tiên.

### Phạm vi

Agent lên **kế hoạch seeding & nội dung quảng cáo tuần cho từng bác sĩ**. Đứng giữa `Agent-AdsReport` *(chẩn đoán số)* và `Agent-OrderMedia` *(biến order thành phiếu quay)*.

### Quyết định thiết kế

| # | Quyết định | Vì sao |
|---|---|---|
| ① | **Hội thoại là nguồn chính, không phải số liệu** | Số liệu chỉ cho biết *cái gì đã chạy*. Chỉ nhìn số thì tuần nào cũng nhân bản winner tuần trước, tới khi winner chết thì không có gì thay. Hội thoại cho biết *cái gì còn thiếu* |
| ② | **12 mã phản đối `O-01`…`O-12` là danh sách ĐÓNG** | Mã mở thì mỗi tuần một cách phân loại, không đếm chuỗi được. `O-00` vượt 10% mẫu mới là tín hiệu danh sách cần bổ sung |
| ③ | **Hai module đơn vị, không phải một** | `sp-I` = con người *(bác sĩ)*, `sp-J` = tổ chức. Nhân hiệu bác sĩ là chủ đề của agent này nên dữ kiện về người đủ lớn để đứng riêng |
| ④ | **Cột `TRUY NGƯỢC` là cột bắt buộc** | Hook không truy ngược được về `HT-nnn` hoặc một con số là hook bịa. Cột này cũng là cột trả lời thay khi ai đó hỏi *"sao tuần này làm clip này?"* |
| ⑤ | **Agent phải dám nói "không phải vấn đề nội dung"** | CPL tăng vì CPM thì đổi hook là tốn một tuần sản xuất để chữa nhầm bệnh. Một agent nội dung luôn kết luận *"cần làm thêm content"* là một agent vô dụng |
| ⑥ | **Ô CHALLENGER bắt buộc mỗi tuần, kể cả tuần số đẹp** | Đây là luật khó bán nhất — nó tiêu tiền vào thứ chưa chắc thắng. Nhưng không có challenger thì khi winner chết mới làm nội dung mới là đã chậm 7–10 ngày |
| ⑦ | **"Tự học" được nói thẳng là một FILE** | Model không nhớ gì giữa hai phiên. Nói rõ điều đó trong `sp-K` §1 tốt hơn để người dùng tưởng agent tự giỏi lên |
| ⑧ | **Phần ④ nhật ký: ghi dự đoán TRƯỚC, đối chiếu SAU** | Không ghi dự đoán trước thì mọi kết quả đều giải thích được sau khi đã biết — và không ai học được gì |
| ⑨ | **Giữ nguyên mã `L01`–`L16`, `CD1`–`CD6`, `A1`–`A5`, 12 điểm `L`** | Dùng chung với `Agent-OrderMedia` và `Agent-AdsReport` để so hiệu suất chéo và nối order giữa hai agent |
| ⑩ | **Agent dừng ở bảng ④ (order)** | Tự viết kịch bản chi tiết là bỏ qua cả thư viện khuôn kịch bản của `Agent-OrderMedia` |

### Phát hiện từ dữ liệu — đã mã hoá thành chặn, không lấp liếm

| 🔴 Phát hiện | Mã hoá ở |
|---|---|
| **Ba bác sĩ vướng chứng chỉ hành nghề**: một người *không tra ra thông tin*, một người *tra ra tên bác sĩ khác*, một người *trạng thái nghỉ việc từ năm trước*. Hai trong ba **đang chạy quảng cáo** với chức danh Trưởng/Phó khoa | `sp-I` §2 · `sp-H` §3a |
| **Ba mức bảo hành cùng lưu hành** trên ads thật: *3 năm* / *10 năm* / *trọn đời* — không thể cùng đúng cho cùng một dịch vụ | `sp-J` §4b · `sp-C` §2 `O-07` |
| **Website công bố 15 bác sĩ, hồ sơ nội bộ chỉ có 8.** Ít nhất 3 người trên trang đội ngũ không có trong hồ sơ | `sp-I` §1 |
| **4/8 bác sĩ không có dữ liệu tính cách/đời sống** — hai trong số đó **đang chạy** → không làm được nội dung `LIVESTYLE` | `sp-I` §3 · §6 ② |
| **Số ca của một bác sĩ mâu thuẫn trong chính hồ sơ**: cột ghi `~3.000`, mô tả ghi `6.000` | `sp-I` §4 |
| **Một bác sĩ mang khẩu hiệu có tên bác sĩ khác** — nhiều khả năng lỗi chép trong sheet | `sp-I` §3 · `sp-F` §4 |
| **4/10 chuyên khoa không có bác sĩ nào trong hồ sơ seeding** | `sp-J` §3 |
| **Sheet hồ sơ bác sĩ chứa email và mật khẩu đăng nhập** | `sp-I` §0 · `.gitignore` · `sp-H` §3c |
| **Chưa có khung case chuẩn hoá** — thiếu đúng hai trường bắt buộc cho nhân hiệu: *ai mổ* và *cơ sở nào* | `sp-J` §5 |
| **Chưa có báo chí, LinkedIn, site riêng, Google Maps cho bác sĩ** → `O-05`/`O-06` không đóng được bằng Facebook một mình | `sp-I` §6 ④⑤⑥ |
| `L13`–`L15` **đang được dùng trong kế hoạch Ads nhưng chưa được định nghĩa** ở thư viện format | `sp-F` §1 |

### Ranh giới riêng được thêm so với các agent khác trong hệ

- **Ranh giới nhân hiệu** (`sp-H` §3): *bác sĩ được nói về NGHỀ, chưa được nói về MÌNH*
- **Ranh giới riêng tư của chính bác sĩ** (`sp-H` §3c): một bác sĩ ghi rõ *"không thích quay, lên hình"* → đó là ranh giới của người đó, ⛔ không phải khó khăn cần thuyết phục vượt qua
- **Bác sĩ nghỉ việc** (`sp-H` §3d): phải GỠ/DỪNG PHÂN PHỐI nội dung cũ — vi phạm `L01`+`L02`+`L08` cùng lúc
- **Bốn tầng seeding** (`sp-E` §3): tầng ④ *giả review bằng nick ảo* ⛔ cấm tuyệt đối
- **Đọc hội thoại ⛔ không phải căn cứ đánh giá nhân viên trực page** (`sp-C` §7) — chấm người là việc của `Agent-QC-Telesale`

### Đã kiểm

```
python tools/sp.py hoi-thoai template/MAU_hoi-thoai.csv   → 25 hội thoại, O-00 4%
python tools/sp.py so-lieu  template/MAU_so-lieu-tuan.csv → 15 dòng, 🟢7 🟡3 🔴2 + 3 chưa đủ mẫu
python tools/gop-tham-khao.py                             → 11 sổ
python tools/dem-ngan.py                                  → 7.970 / 8.000
```

### Lỗi đã sửa trong lúc dựng

| Lỗi | Sửa |
|---|---|
| `dem-ngan.py` đếm ra **54 ký tự** | Khối ``` đặt trong blockquote ở header làm hàng rào ghép lệch → bỏ khối đó, chuyển thành câu lệnh inline. Đã ghi cảnh báo vào `doc/02-cau-lenh.md` |
| `sp.py` để **36% hội thoại rơi `O-00`** | Bảng từ khoá quá hẹp — bổ sung `O-04` `O-05` `O-08`; còn **4%** |
| `sp.py` áp **ngưỡng tuyệt đối lên mẫu 25** | Ngưỡng của `sp-C` §5 là **/100 hội thoại**. Chuyển sang tính theo tỷ lệ và **ẩn cột việc khi mẫu < 50** |
| Nấc `A2` và `A4` ra **0%** trên mẫu thật | Bảng từ khoá nấc quá hẹp — bổ sung; còn `A2` 8% · `A4` 4% |

---

## Dự định v1.1

- [ ] Mở chặn ① — đối chiếu chứng chỉ `BS01` `BS02`, cập nhật `sp-I` §2
- [ ] Mở chặn ② — chính sách bảo hành bằng văn bản, cập nhật `sp-J` §4b
- [ ] Phỏng vấn 30 phút lấy dữ liệu tính cách `BS04` `BS05` theo khung của `BS01`/`BS03`
- [ ] `tools/ke-hoach.py` — sinh khung bảng ③ 18 cột sẵn ngày/giờ/bác sĩ để agent chỉ điền phần sáng tạo
- [ ] `tools/trang-huong-dan.py` + `tools/huong-dan.json` — trang hướng dẫn dùng chung với các agent khác
- [ ] Thay ngưỡng giả định trong `sp-D` bằng **3 tháng số thật**
- [ ] Đo khung giờ tối ưu **riêng cho từng page bác sĩ** (`sp-E` §4 đang dùng khung chung)
- [ ] Nối ngược: đưa lỗ hổng E-E-A-T sang `Agent-KN-GEO-Plant` dưới dạng file bàn giao
