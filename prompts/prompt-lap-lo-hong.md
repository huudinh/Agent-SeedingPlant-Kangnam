# PROMPT · LẤP LỖ HỔNG & NHẬT KÝ

> Hai prompt hay dùng nhất **ngoài** chu trình tuần.

---

## 1. Lấp lỗ hổng phễu

```
Từ ma trận 5A × chân dung dưới đây, liệt kê MỌI Ô TRỐNG.

Với mỗi ô trống, trả lời ba câu:
  ① Mã O nào tương ứng, đang bao nhiêu lần/100 hội thoại?
  ② Đây là CHỦ Ý BỎ TRỐNG hay là BỎ SÓT?
  ③ Nếu là bỏ sót: viết một hook cho đúng ô đó, kèm format và bác sĩ phù hợp.

Xếp ưu tiên theo: mã O cao × ô trống × ⛔ không bị chặn pháp chế.

★ Ưu tiên tuyệt đối cho ô trống nào mà nội dung lấp được nó là QUYỀN LỢI DỊCH VỤ
chứ không phải claim y khoa — loại đó sạch pháp chế, viết được ngay, không phải
chờ ai duyệt. Ví dụ: bốn quyền lợi cho tệp Việt kiều (sp-J §6).
```

### Biến thể — lỗ hổng E-E-A-T

```
Từ sp-I §6, xếp 8 lỗ hổng E-E-A-T theo ĐÒN BẨY: việc nào mở được nhiều chặn nhất
với ít công nhất.

Mỗi việc ghi: ai làm · cần gì · mở được chặn nào · mất bao lâu.
Tách rõ: việc nào của agent này, việc nào của Agent-GEO-Plant, việc nào của PR.
```

---

## 2. Nhật ký tuần — khi chỉ muốn cập nhật bộ nhớ

```
Đây là nhật ký tuần [44]. Cập nhật thành nhật ký tuần [45] với số liệu mới.

[dán nhật ký cũ]
[dán số liệu/kết quả tuần này]

Giữ nguyên 5 phần:
① SỔ HOOK — hook · chấm · các tuần đã chạy · việc tuần này
② LUẬT MỚI RÚT RA — đánh dấu [lần 1] / [lần 2] / [lần 3]
   ★ Đủ 3 lần → VIẾT THÀNH LUẬT vào sổ tương ứng, ghi rõ sổ nào §nào, rồi BỎ KHỎI
     nhật ký. Nhật ký ngắn dần là dấu hiệu tốt.
③ ĐANG THEO DÕI — chưa đủ 3 lần
④ ★ DỰ ĐOÁN
   - đối chiếu từng dự đoán tuần trước: ✅ ĐÚNG / ❌ SAI, kèm số thật
   - ⛔ KHÔNG được lặng lẽ bỏ dự đoán SAI
   - ⛔ KHÔNG sửa dự đoán cũ cho khớp kết quả — sai thì ghi thêm dòng đính chính
   - rồi ghi dự đoán mới cho tuần này
   - tính tỷ lệ dự đoán đúng luỹ kế. Dưới 50% nghĩa là TRI THỨC TRONG CÁC SỔ ĐANG SAI,
     không phải thị trường khó.
⑤ VIỆC CHẶN CÒN TỒN — kèm TỒN TỪ TUẦN NÀO và CHẶN MẤY DÒNG
   Việc tồn >4 tuần → đẩy lên thành dòng riêng ở ĐẦU kế hoạch, không để trong nhật ký.
```

### Biến thể — chuyển nhật ký thành luật

```
Mục này trong nhật ký đã lặp lần thứ 3:
  "[dán mục]"

① Nó thuộc sổ nào, §nào?
② Viết đoạn chính xác cần chèn vào sổ đó — đúng giọng và định dạng của sổ.
③ Có luật nào đang có trong sổ MÂU THUẪN với luật mới này không? Nếu có thì sửa cái nào.
④ Nhắc chạy lại: python tools/gop-tham-khao.py
```
