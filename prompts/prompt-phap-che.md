# PROMPT · ⛔ SOÁT PHÁP CHẾ — CỔNG B

> Chạy **trước khi** kế hoạch rời khỏi agent. Chạy được riêng trên một kế hoạch đã có.

```
Soát pháp chế bảng kế hoạch dưới đây. Với MỖI DÒNG:

① 12 điểm L01–L12 — ghi điểm nào chạm
② Màu cờ: 🟢 đăng được · 🟡 sửa câu rồi đăng · 🔴 không đăng
③ ⛔ MỖI CỜ 🟡 VÀ 🔴 PHẢI KÈM MỘT CÂU THAY THẾ CỤ THỂ.
   Ghi "vi phạm L04" mà không đưa câu thay = chưa soát xong.
④ Dòng 🔴 đang chạy: ghi "giữ ngân sách hiện tại, KHÔNG tăng, dựng bản thay"

KIỂM RIÊNG CÁC Ô SAU:
  · tên bác sĩ nào → tra sp-I §2, người đó có được nêu chức danh/số năm/số ca không
  · có bác sĩ đang DỪNG hoặc đã nghỉ việc lọt vào không
  · bác sĩ có nói về kỹ thuật ngoài chuyên khoa của chính mình không
  · có con số nào trong danh sách ⛔ KHÔNG BỊA (sp-H §4) không
  · có mục seeding tầng ④ (giả review nick ảo) không
  · có hook nói với NGƯỜI XEM rằng họ đang có khiếm khuyết không
    (⛔ "Mắt bạn sụp mí…" → ✅ "Sụp mí làm gương mặt trông mệt — vì sao?")
  · có CTA chốt nào gắn vào nấc A1 không
  · format L06 / L11 / L12 có qua luật chặn riêng chưa
  · có email / SĐT / mật khẩu / đời tư ai lọt ra không

XUẤT:
  bảng cờ: MÃ DÒNG | cờ | điểm L | câu vi phạm | CÂU THAY THẾ | ai duyệt
  + khối [CHỜ XÁC NHẬN]: thứ còn thiếu | ai cấp | CHẶN MẤY DÒNG
  + câu mẫu trả lời bình luận cho quản trị kênh (sp-H §5)
```

---

## Biến thể — soát một hook

```
Soát hook này: "[dán hook]"

① Chấm theo công thức 4 thành phần, ① gọi tình trạng là CỔNG
② Có trúng H1–H7 không
③ Có vi phạm điểm L nào không — nếu có, viết lại giữ nguyên ý
④ Có vi phạm luật Facebook ngành thẩm mỹ (ám chỉ khiếm khuyết người xem) không
⑤ Kết: ✅ DÙNG ĐƯỢC / ⚠️ SỬA RỒI DÙNG / ✗ ĐỔI HOOK
```

## Biến thể — rà nội dung cũ của bác sĩ đã nghỉ

```
[BS07] đã nghỉ việc theo sp-I §2.

Liệt kê việc phải làm:
  · nội dung nào có tên/hình người đó cần GỠ hoặc DỪNG PHÂN PHỐI
  · khẩu hiệu nào của người đó đang lưu hành phải thu hồi
  · page/kênh nào của người đó cần xử lý (đổi tên? đóng? bàn giao?)
  · ai chịu trách nhiệm từng việc

⚠️ Để nội dung cũ chạy với tên người không còn hành nghề tại cơ sở là vi phạm
L01 + L02 + L08 cùng lúc — nặng hơn một ad bị từ chối.
```
