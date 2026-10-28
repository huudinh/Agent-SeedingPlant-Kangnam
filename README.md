# 🌱 Agent-SeedingPlant-Kangnam

> **Tối ưu quảng cáo Ads cho từng bác sĩ Kangnam.**
>
> Đọc số liệu tuần trước, chẩn đoán **CPI · CPL · CPB** đang hỏng ở đâu, đọc hội thoại khách thật để biết khách đang cần gì mà quảng cáo chưa trả lời, rồi **đưa ra cải tiến nội dung** và **format nội dung chạy ads tuần tới** cho từng bác sĩ.

`v1.0` · Claude / ChatGPT / Gemini / Claude Code

### 📘 [**Hướng dẫn cài đặt & prompt mẫu →**](https://claude.ai/artifact/7vzxFRWdcCg2vQpK5SSEWv)

> Trang web có **nút Copy từng file**: 3 thẻ copy bộ não · 17 file tri thức · **35 prompt mẫu** lọc theo 7 nhóm · **12 câu smoke test** · năm điều phải biết · sáu việc đang chặn.
>
> Người mới vào khối thì **mở trang này trước**, đừng đọc README.

---

## Agent này làm gì

| Việc | Nghĩa |
|---|---|
| ① **Đánh giá hiệu quả tuần trước** | Phân rã `CPL`, chấm từng nội dung 🟢🟡🔴, trả lời *"tuần trước yếu gì"* |
| ② **Thấu hiểu khách qua hội thoại** | Bóc inbox thành **12 mã phản đối** `O-01…O-12`, đếm tần suất |
| ③ ★ **Đưa ra cải tiến nội dung** | 4 đường: nhân bản · biến thể · giữ ý bỏ hook · bỏ hẳn |
| ④ **Lên format nội dung chạy ads tuần** | Hook · CTA · format · nấc 5A · chân dung — **cho từng bác sĩ** |
| ⑤ **Soát pháp chế trước khi lên ads** | 12 điểm `L`, cờ 🔴🟡🟢, **kèm câu thay thế** |
| ⑥ **Tự học theo tuần** | Nhật ký: hook nào sống/chết, luật mới, dự đoán & đối chiếu |

⛔ **Đây KHÔNG phải agent sản xuất video.** Agent không viết lời thoại theo mốc giây, không làm shot list, không làm call sheet. Dòng nào cần quay thì bàn giao sang `Agent-OrderMedia`.

---

## Đầu vào → Đầu ra

```
① Chân dung khách 5A + Hook/CTA template  ─┐
② Hội thoại inbox với khách (≈100 cuộc)   ─┤      ┌─► ③ ĐÁNH GIÁ HIỆU QUẢ TUẦN TRƯỚC
③ Số liệu Performance ads tuần trước      ─┼─►AGENT┼─► ④ INSIGHT + "YẾU GÌ"
④ Hồ sơ bác sĩ · USP · thế mạnh (sp-I)    ─┘      ├─► ⑤ CẢI TIẾN TỪNG NỘI DUNG
                                                   ├─► ⑥ FORMAT NỘI DUNG CHẠY ADS TUẦN TỚI
                                                   ├─► ⑦ CỜ PHÁP CHẾ + câu thay thế
                                                   ├─► ⑧ [CHỜ XÁC NHẬN] + ai cấp + chặn mấy dòng
                                                   └─► ⑨ NHẬT KÝ TUẦN ← bộ nhớ của hệ
```

Quy trình gốc từ vận hành: **Đọc insight → Nhóm/Đối tượng (Giai đoạn) → Hook → CTA → Format**, mở thành 7 bước có hai cổng chặn.

---

## Chỉ số agent chịu trách nhiệm

| Chỉ số | Công thức | Agent có cải thiện được không |
|---|---|---|
| **CTR** | click ÷ impression | ✅ **Có** — hook & creative là việc của agent này |
| **CPI** | chi ÷ hội thoại tin nhắn bắt đầu | ✅ Có, qua CTR và độ khớp thông điệp |
| **CPL** | chi ÷ lead hợp lệ | 🟡 Một phần — phải phân rã trước |
| **CPB** | chi ÷ booking | 🟡 Một phần |
| **CPM** | chi ÷ impression × 1.000 | ⛔ **Không** — đấu giá/tệp, việc của Adnet |

### ★ Luật quan trọng nhất của agent

```
CPL = (CPM/1000) ÷ ( CTR × click→inbox% × inbox→lead% )

⛔ KHÔNG ĐỀ XUẤT ĐỔI NỘI DUNG KHI THÀNH PHẦN XẤU ĐI KHÔNG PHẢI CTR.
```

| Thành phần xấu đi | Thật ra là việc của | Agent phải nói |
|---|---|---|
| **CTR** giảm | ✅ Nội dung | *"Đây là vấn đề nội dung — tuần này làm gì"* |
| **CPM** tăng | Adnet (tệp, bid, lịch) | *"Tuần này KHÔNG phải vấn đề nội dung"* |
| **click→inbox** giảm | Kỹ thuật (điểm đến, lời chào tự động) | *"Không phải nội dung"* |
| **inbox→lead** giảm | Trực page (ca trực, thời gian phản hồi) | *"Không phải nội dung"* |

⚠️ Một agent quảng cáo luôn kết luận *"cần làm thêm content"* là một agent vô dụng. **Dám nói "không phải lỗi nội dung" là giá trị, không phải né việc.**

---

## Vị trí trong hệ agent

```
   Agent-PBP (định vị, big idea, kế hoạch quý)
            │ trụ cột nội dung
            ▼
số liệu ads ──► Agent-AdsReport ──► chẩn đoán sâu: 30 mã cảnh báo, ai xử
            │
            ▼ "yếu tầng nào"
hội thoại  ─┐
chân dung  ─┼──► ★ Agent-SeedingPlant ──► TỐI ƯU NỘI DUNG ADS THEO BÁC SĨ
hồ sơ BS   ─┘         (repo này)                 │
                                                 │ dòng nào cần quay
                                                 ▼
                                   Agent-OrderMedia ──► phiếu quay chi tiết

      lỗ hổng E-E-A-T bác sĩ ──────► Agent-KN-GEO-Plant
```

| Việc này | ⛔ KHÔNG phải của agent này | Của ai |
|---|---|---|
| Chẩn đoán số liệu chi tiết, bắn cảnh báo theo mã, phân bổ ngân sách | | `Agent-AdsReport-Kangnam` |
| Viết lời thoại theo mốc giây, shot list, đạo cụ, call sheet | | `Agent-OrderMedia-Kangnam` |
| Định vị thương hiệu, big idea, kế hoạch quý | | `Agent-PBP` |
| Trồng dấu chân bác sĩ cho AI trích dẫn (báo, LinkedIn, site riêng) | | `Agent-KN-GEO-Plant` |
| Chấm chất lượng cuộc gọi telesales | | `Agent-QC-Telesale` |

---

## Cài đặt nhanh

| Nền tảng | Dán vào | File |
|---|---|---|
| **Claude Project** | Custom instructions | [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) |
| **ChatGPT Custom GPT** | Instructions *(giới hạn 8.000 ký tự)* | [`SYSTEM-PROMPT-NGAN.md`](SYSTEM-PROMPT-NGAN.md) |
| **Gemini Gem** | Chỉ dẫn | [`SYSTEM-PROMPT.md`](SYSTEM-PROMPT.md) |

Rồi nạp **11 file [`knowledge/`](knowledge/)** + **6 file [`prompts/`](prompts/)** vào phần *Knowledge / Tri thức*.
Nền tảng chỉ cho nạp ít file → dùng [`goi/GOP-tri-thuc.md`](goi/GOP-tri-thuc.md).

📘 **Bản có nút Copy từng file:** [trang hướng dẫn](https://claude.ai/artifact/7vzxFRWdcCg2vQpK5SSEWv) · Chi tiết văn bản: [`doc/01-cai-dat.md`](doc/01-cai-dat.md)

> Nút Copy trên trang **đọc thẳng file nguồn trong repo** — sửa `knowledge/` rồi chạy lại `python tools/trang-huong-dan.py` là nút Copy tự khớp, không bao giờ lệch với repo.

---

## 11 sổ tri thức

| Sổ | Nội dung |
|---|---|
| [`sp-A`](knowledge/sp-A-vai-tro-quy-trinh.md) | Vai trò · 7 bước · hai cổng · AUTO · ranh giới với các agent khác |
| [`sp-B`](knowledge/sp-B-doc-dau-vao.md) | Ba dòng đầu vào · cột bắt buộc · 10 ô tự suy ra · quy ước mã |
| ★ [`sp-C`](knowledge/sp-C-khai-thac-hoi-thoai.md) | **Thấu hiểu khách qua hội thoại** — 12 mã `O` · bảng giao 4 ô · chép hook từ miệng khách |
| ★ [`sp-D`](knowledge/sp-D-doc-so-danh-gia.md) | **CPI/CPL/CPB · phân rã CPL · chấm nội dung · 4 đường cải tiến** |
| [`sp-E`](knowledge/sp-E-nen-tang-facebook.md) | Luật nền tảng với ads y tế · page bác sĩ · 4 tầng seeding · khung giờ · live |
| [`sp-F`](knowledge/sp-F-ngan-hang-format-hook.md) | **Ngân hàng format** `L01`–`L16` · format chuẩn từng bác sĩ · công thức hook · CTA theo nấc |
| [`sp-G`](knowledge/sp-G-ke-hoach-tuan.md) | Đầu ra: bảng đánh giá · bảng kế hoạch ads 18 cột · luật cân đối tuần |
| [`sp-H`](knowledge/sp-H-phap-che-ranh-gioi.md) | 12 điểm `L` · cờ 🔴🟡🟢 · **ranh giới nhân hiệu bác sĩ** · câu mẫu trả lời bình luận |
| ★ [`sp-I`](knowledge/sp-I-module-bac-si.md) | **Module đơn vị — BÁC SĨ.** 8 người · USP · thế mạnh · 🔴 xác minh chứng chỉ · lỗ hổng E-E-A-T |
| [`sp-J`](knowledge/sp-J-module-he-thong.md) | Module đơn vị — **HỆ THỐNG.** Chi nhánh · giấy phép · dịch vụ · giá · 🔴 bảo hành |
| [`sp-K`](knowledge/sp-K-tu-hoc-nhat-ky.md) | **Tự học** — nhật ký tuần · luật "ba lần thành luật" · nhịp vận hành tuần |

★ **Đổi đơn vị → thay `sp-I` + `sp-J`, không sửa bộ não.**

---

## Dòng lệnh

```bash
# đọc số ads tuần trước — CPI/CPL/CPB, chấm nội dung 🟢🟡🔴
python tools/sp.py so-lieu template/MAU_so-lieu-tuan.csv --ky "20-26/10" --lead-tu CRM

# bóc hội thoại khách thành 12 mã phản đối, đếm tần suất
python tools/sp.py hoi-thoai template/MAU_hoi-thoai.csv

# gộp tri thức sau mỗi lần sửa knowledge/
python tools/gop-tham-khao.py

# canh giới hạn 8.000 ký tự của bản ngắn
python tools/dem-ngan.py
```

Chi tiết: [`doc/02-cau-lenh.md`](doc/02-cau-lenh.md)

---

## 6 prompt mẫu

| Prompt | Dùng khi |
|---|---|
| [`prompt-auto.md`](prompts/prompt-auto.md) | Chạy cả tuần một phát |
| ★ [`prompt-doc-so-tuan.md`](prompts/prompt-doc-so-tuan.md) | *"Tuần trước yếu gì?"* — phân rã CPL, chấm nội dung |
| ★ [`prompt-boc-hoi-thoai.md`](prompts/prompt-boc-hoi-thoai.md) | Bóc hội thoại → insight → hook |
| [`prompt-ke-hoach-bac-si.md`](prompts/prompt-ke-hoach-bac-si.md) | Nội dung ads cho một bác sĩ |
| [`prompt-phap-che.md`](prompts/prompt-phap-che.md) | Soát cổng B trước khi lên ads |
| [`prompt-lap-lo-hong.md`](prompts/prompt-lap-lo-hong.md) | Lấp lỗ hổng phễu · cập nhật nhật ký |

---

## Năm luật khó nhất

| # | Luật | Vì sao |
|---|---|---|
| ① | **Phân rã CPL trước khi kết luận** | CPL tăng vì CPM thì đổi hook là chữa nhầm bệnh, tốn một tuần sản xuất vô ích |
| ② | **Hook phải truy ngược được** về `HT-nnn` hoặc một con số thật | Cột `TRUY NGƯỢC` trống = dòng bị loại khỏi kế hoạch. Không truy ngược được là hook bịa |
| ③ | **≥1 ô CHALLENGER mỗi tuần, kể cả tuần số đẹp** | Winner chết mà chưa có đồ thay là chậm 7–10 ngày |
| ④ | **Bác sĩ được nói về NGHỀ, chưa được nói về MÌNH** | Chức danh/số năm/số ca chỉ nói khi `sp-I` §2 ghi đã đối chiếu chứng chỉ |
| ⑤ | **Tự học nằm trong một FILE, không nằm trong model** | Không dán lại nhật ký thì tuần sau agent đề xuất lại đúng hook đã chết |

### Chấm nội dung & bốn đường cải tiến

| Chấm | Điều kiện | Cải tiến |
|---|---|---|
| 🟢 **TỐT** | CTR ≥ median **và** CPL ≤ median | **Nhân bản** — giữ nguyên hook, đổi chân dung/khu vực/bác sĩ |
| 🟡 **TB** | Một trong hai chỉ số đạt | **Biến thể** — đổi **đúng một** biến |
| 🔴 **KÉM** + mã `O` vẫn cao | CTR ≤ −30% median, CPM trong ±15% | **Giữ ý — bỏ hook** |
| 🔴 **KÉM** + mã `O` thấp | | **Bỏ hẳn** |

⛔ **Không đổi ≥3 biến cùng lúc** — đổi ba biến thì dù kết quả tốt lên cũng không học được gì.

---

## ⛔ Tuyệt đối không

- ⛔ **Seeding giả review bằng nick ảo** — vi phạm `L06`+`L08`, mất tài khoản, mất uy tín
- ⛔ Đề xuất đổi nội dung khi **thành phần xấu đi không phải CTR**
- ⛔ Chạy quảng cáo gắn chức danh/bằng cấp bác sĩ **chưa đối chiếu được chứng chỉ**
- ⛔ Chạy ads cho bác sĩ **đang dừng** hoặc **đã nghỉ việc**
- ⛔ Trả lời `O-07` *(bảo hành)* bằng con số — ba mức đang xung đột
- ⛔ Trả lời `O-12` *(bệnh nền)* — claim y khoa, phải bác sĩ khám
- ⛔ Hook nói với **người xem** rằng họ đang có khiếm khuyết *(Facebook từ chối)*
- ⛔ Để lọt tên/SĐT/ảnh/email/mật khẩu — của khách **hay của bác sĩ**
- ⛔ Dùng kết quả đọc hội thoại để **chấm điểm nhân viên trực page**
- ⛔ Bịa giá, số suất, bảo hành, mốc hồi phục, số ca, chức danh

---

## 🔴 Đang bị chặn — cần cấp để mở

| # | Thứ còn thiếu | Ai cấp | Chặn gì |
|---|---|---|---|
| ① | **Đối chiếu chứng chỉ hành nghề `BS01` `BS02`** + văn bản bổ nhiệm chức danh | Vận hành + pháp chế | 🔴 Mọi ad gắn chức danh/số năm/số ca của **hai bác sĩ đang chạy** |
| ② | **Chính sách bảo hành bằng văn bản** — ba mức *(3 năm / 10 năm / trọn đời)* đang cùng chạy trên ads thật | Vận hành | 🔴 Mọi nội dung chạm `O-07` |
| ③ | Xác nhận **`BS07` đã nghỉ việc** → rà soát & gỡ ad cũ còn tên người đó | Vận hành | 🔴 Ad cũ đang phân phối |
| ④ | **Dữ liệu tính cách/đời sống cho `BS04` `BS05`** | Biên tập cơ sở | 🟠 Không làm được `LIVESTYLE` → nhân hiệu đứng im |
| ⑤ | **Bảng giá hiện hành** dịch vụ ngoài mắt | Vận hành / sales | 🟠 Format `L11` + hook nấc `A4` có giá |
| ⑥ | Định nghĩa **format `L13`–`L16`** · số giấy phép đủ **7 cơ sở** | Content Lead · pháp chế | 🟡 Ad local ngoài 2 bệnh viện |

⚠️ **Mục ① là mục cấp bách nhất** — hai bác sĩ **đang chạy quảng cáo** với chức danh chưa đối chiếu được. Đây không phải bất tiện nội bộ mà là rủi ro pháp chế đang phát sinh.

---

## Cây thư mục

```
Agent-SeedingPlant-Kangnam/
├── SYSTEM-PROMPT.md          bộ não đầy đủ
├── SYSTEM-PROMPT-NGAN.md     bản ≤8.000 ký tự cho ChatGPT
├── knowledge/                11 sổ sp-A … sp-K
├── prompts/                  6 prompt mẫu
├── goi/GOP-tri-thuc.md       bản gộp (sinh tự động)
├── template/                 dữ liệu mẫu để chạy thử
├── tools/                    sp.py · gop-tham-khao.py · dem-ngan.py · trang-huong-dan.py
├── doc/                      cài đặt · dòng lệnh · changelog
└── out/                      kết quả — ⛔ KHÔNG commit
```

⛔ `out/`, file hội thoại gốc, hồ sơ bác sĩ gốc, ảnh khách — [`.gitignore`](.gitignore) đã chặn.
