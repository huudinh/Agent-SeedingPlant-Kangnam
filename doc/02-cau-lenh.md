# ② DÒNG LỆNH

> Bốn script. Tất cả chỉ cần **Python 3.9+**; đọc `.xlsx` cần thêm `pip install openpyxl`.

---

## `tools/sp.py` — tiền xử lý đầu vào

Hai việc con. Script làm phần **đếm** và phần **tính**; phần **hiểu ngữ cảnh** vẫn là việc của agent.

### `hoi-thoai` — bước B3

```bash
python tools/sp.py hoi-thoai <file>              [--sheet TÊN] [--out ĐƯỜNG_DẪN]
python tools/sp.py hoi-thoai --sheet-id <ID> --gid <GID>
```

Nhận `.csv` · `.xlsx` · **`.txt`** *(dạng dán thô `KH: …` / `Khách: …`)*.

Lấy **tin nhắn đầu tiên của mỗi hội thoại**, gán `O-01`…`O-12`, nấc 5A, chân dung, rồi đếm.

```
  DOC DUOC : 25 hoi thoai
  GHI RA   : out\insight-hoi-thoai.csv

  DEM MA PHAN DOI — nguong ra viec: >=15 tuyen rieng, 8-14 mot hook
    O-05    3   12.0%  Nghi tay nghe bac si         MOT HOOK <<
    O-08    7   28.0%  Khong biet minh can gi       TUYEN RIENG <<
```
→ Cột việc **chỉ hiện khi mẫu ≥ 50**. Dưới đó chỉ xếp hạng tương đối.

```
  ! O-00 = 36% (>10%) — danh sach 12 ma can bo sung. BAO LAI, dung tu them ma.
```
→ Danh sách 12 mã là **danh sách đóng**. `O-00` cao nghĩa là nó cần bổ sung — ⛔ đừng để agent tự thêm mã.

```
  PHAN BO NAC 5A
    A3    7   28.0%
    ! >60% roi vao A3 — pheu dang THIEU NOI DUNG A1-A2
```
→ Kết luận này **không nhìn ra được từ số liệu ads**. Inbox toàn người sắp chốt = tệp mới không vào.

```
  TANG HAI: 4 hoi thoai co truc page go TRA LOI DAI (>=300 ky tu)
```
→ Việc này đáng lẽ **clip làm**, không phải người gõ. Xem `sp-C` §7.

### `so-lieu` — bước B2

```bash
python tools/sp.py so-lieu <file> --ky "20-26/10" --lead-tu CRM  [--out ĐƯỜNG_DẪN]
python tools/sp.py so-lieu --sheet-id <ID> --gid <GID> --ky "20-26/10" --lead-tu Meta
```

| Tham số | Nghĩa |
|---|---|
| `--ky` | Kỳ số liệu — ⚠️ **cổng A đòi**, không ghi thì agent phải chặn |
| `--lead-tu` | `Meta` · `CRM` · `CHUA GHI` — ⚠️ **cổng A đòi** |

```
  TONG KY
    Chi      204,4tr
    CPI      47k      (4360 inbox)
    CPL      436k      (469 lead / 204,4tr)
    CPB      1,8tr      (111 booking)

  CHAM NOI DUNG : TOT 7  ·  TB 3  ·  KEM 2  ·  chua du mau 3
      [KEM] MUI-CD2-A4-006   Hội thảo lột xác 18/10 cắt mí giá sốc
```

```
  ! FILE KHONG CO COT 'HOOK' — chi cham duoc theo TEN AD, do tin THAP.
```
→ **Cột `HOOK` là cột quan trọng nhất của file số liệu.** Không có nó thì chấm được *ad*, ⛔ không chấm được *nội dung*.

### ⚠️ Giới hạn của script

| Script làm được | Script KHÔNG làm được |
|---|---|
| Gán mã `O`, nấc, chân dung theo **từ khoá** | Hiểu ngữ cảnh một câu hỏi |
| Đếm tần suất, tính %, phát hiện mẫu nhỏ | **Bảng giao** — cần biết nội dung ĐÃ CÓ những gì |
| Tính CPM/CTR/CPI/CPL/CPB | **Phân rã CPL với median 7 ngày** — script chỉ có median trong kỳ |
| Chấm 🟢🟡🔴, bắt bão hoà, bắt phụ thuộc 1 creative | Kết luận *"có phải vấn đề nội dung không"* |
| Nhắc 4 thứ chặn kết luận | Viết hook, viết CTA |

Ví dụ: script bắt được *"bảo hành"* → `O-07`, **không** bắt được *"lỡ nó không như ý thì sao ạ"* cũng là `O-07`.
→ **Agent vẫn phải đọc lại toàn bộ.** Script chỉ để khỏi bỏ sót và khỏi đếm tay.

---

## `tools/gop-tham-khao.py` — gộp tri thức

```bash
python tools/gop-tham-khao.py
```

Gộp **11 sổ `knowledge/`** theo thứ tự `sp-A` → `sp-K` thành [`goi/GOP-tri-thuc.md`](../goi/GOP-tri-thuc.md), kèm mục lục và neo liên kết.

**Chạy lại mỗi lần sửa `knowledge/`.** File gộp sinh tự động — ⛔ đừng sửa trực tiếp trong đó.

---

## `tools/dem-ngan.py` — đếm ký tự bản ngắn

```bash
python tools/dem-ngan.py
```

```
  Khoi COPY : 7,970 ky tu
  Gioi han  : 8,000
  Con lai   : 30  (gan day — them dong nao thi phai cat dong khac)
```

🔴 **`SYSTEM-PROMPT-NGAN.md` đang gần đầy.** Chạy script này **sau mỗi lần sửa** file đó — ChatGPT Custom GPT cắt phần vượt **không báo lỗi**, nên vượt mà không biết là mất luật chặn ở cuối prompt.

Script trả **exit code 1** khi vượt → dùng được trong hook hoặc CI.

⚠️ Script lấy khối ``` **lớn nhất** trong file. ⛔ Đừng đặt khối ``` nào khác trong blockquote của file đó — hàng rào sẽ ghép lệch và số đếm sai.

---

## `tools/trang-huong-dan.py` — sinh trang hướng dẫn

```bash
python tools/trang-huong-dan.py              # ghi ra tools/huong-dan.html
python tools/trang-huong-dan.py <đường_dẫn>  # ghi ra chỗ khác
```

```
tools\huong-dan.html — 398 KB
  3 thẻ · 17 file tri thức · 35 prompt · 12 câu smoke test
```

Đọc câu chữ từ [`tools/huong-dan.json`](../tools/huong-dan.json) + **đọc thẳng các file nguồn** *(bộ não, 11 sổ, 6 prompt)* để nhúng vào nút Copy → **nút Copy luôn khớp file nguồn**, không bao giờ lệch.

| Việc | Ở đâu |
|---|---|
| Sửa **nội dung** trang *(câu chữ, smoke test, prompt, mục chặn)* | `tools/huong-dan.json` |
| Sửa **style/layout** | `tools/trang-huong-dan.py` — ⚠️ generator **dùng chung** với các agent khác |
| Sửa tri thức | `knowledge/` → nút Copy tự cập nhật, ⛔ không phải sửa JSON |

**Quy trình đăng lại sau khi sửa:**
```bash
python tools/gop-tham-khao.py      # gộp lại tri thức trước
python tools/dem-ngan.py           # canh giới hạn bản ngắn
python tools/trang-huong-dan.py    # rồi mới sinh trang
```
Xong thì publish lại `tools/huong-dan.html` vào **đúng URL artifact cũ** để link trong README không đổi:
`https://claude.ai/artifact/7vzxFRWdcCg2vQpK5SSEWv`

⛔ `tools/huong-dan.html` **không commit** — nó là artifact sinh ra, không phải nguồn.

> ⚠️ **Generator này dùng chung với `Agent-QC-Telesale`, `Agent-Order-SoLieu`, `Agent-Media`, `Agent-PBP`…** Bản trong repo này đã thêm `<meta name="viewport">` *(bản gốc thiếu, làm trang bị thu nhỏ trên điện thoại)*. Nếu sửa style, cân nhắc đồng bộ sang các agent kia.
>
> ⚠️ Thẻ nào trong `the[]` **không phải `brain`/`ngan`** thì bắt buộc có khoá `"file"`, nếu không generator báo `KeyError`.

---

## Quy trình đầy đủ — một tuần

```bash
# 1. bóc hội thoại
python tools/sp.py hoi-thoai inbox-t45.csv

# 2. đọc số tuần trước
python tools/sp.py so-lieu ads-t44.csv --ky "20-26/10" --lead-tu CRM

# 3. đưa hai file out/ cho agent, kèm nhật ký tuần trước
```

Rồi trong agent:
```
AUTO — kế hoạch nội dung tuần 45, kỳ số liệu 20–26/10.
Đính kèm: out/insight-hoi-thoai.csv · out/cham-noi-dung.csv · nhật ký tuần 44.

Xuất đủ 4 bảng + 2 khối + nhật ký tuần 45.
Cuối bảng in khối GIẢ ĐỊNH và khối [CHỜ XÁC NHẬN] kèm ai cấp, chặn mấy dòng.
```

---

## ⛔ Lưu ý bảo mật

`out/`, file hội thoại gốc, hồ sơ bác sĩ gốc, ảnh khách **không commit** — xem [`.gitignore`](../.gitignore).

```
⛔ Sheet hồ sơ bác sĩ nguồn CÓ CHỨA email và MẬT KHẨU đăng nhập.
   Không tải về repo. Không in ra. Không gửi ra ngoài khối.
   sp-I đã cố ý loại hai trường đó — ⛔ đừng chép lại vào.
```

Trước khi gửi bất cứ file nào ra ngoài khối:
- ⛔ Không gửi hội thoại gốc — chỉ gửi bản đã bóc, đã ẩn danh
- ⛔ Không gửi kèm ảnh khách gửi trong inbox
- ⛔ Không upload file hội thoại lên công cụ bên thứ ba chưa được duyệt

---

## Lỗi thường gặp

| Lỗi | Nguyên nhân | Sửa |
|---|---|---|
| `Khong tim duoc cot noi dung tin nhan` | File không có cột nhận ra được | Xem `sp-B` §3; đổi tên cột hoặc thêm từ khoá vào `COT_HT` trong `sp.py` |
| `Thieu cot bat buoc: chi, imp, click` | File số liệu thiếu cột | Xem `sp-B` §4 |
| `Thieu openpyxl` | Đọc `.xlsx` mà chưa cài | `pip install openpyxl` |
| `HTTP 401/403` khi tải Google Sheet | Tab chưa mở quyền xem bằng link | Đổi quyền, hoặc tải CSV về rồi chạy trên file |
| `O-00` chiếm phần lớn | Từ khoá chưa phủ giọng khách của ngành/vùng này | Bổ sung từ khoá vào `MA_O` trong `sp.py` **và** vào `sp-C` §2 |
| Chữ hiện thành `?` trên màn hình | Console Windows cp1252 | Script đã tự xử; còn lỗi thì chạy `chcp 65001` trước |
