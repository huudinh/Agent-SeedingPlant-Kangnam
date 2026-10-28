# PROMPT · ★ BÓC HỘI THOẠI → INSIGHT

> Bước B3 — **bước làm nên giá trị của agent này.** Chạy riêng được, không cần số liệu ads.

```
Bóc [100] hội thoại inbox dưới đây thành insight.

① ĐẾM ĐỦ 12 MÃ O-01..O-12, kể cả mã bằng 0:
   mã | tên | số lần | % mẫu | nấc 5A hay gặp | chân dung hay gặp

② BẢNG GIAO — 4 cột, kết luận theo 4 ô:
   mã O | số lần hỏi/100 | số nội dung ĐÃ CÓ | kết luận
   · hỏi NHIỀU + nội dung ÍT   → ① LỖ HỔNG, ƯU TIÊN 1
   · hỏi NHIỀU + nội dung NHIỀU → ② đang đúng hướng — nhưng kiểm xem nội dung
                                   có đang TRẢ LỜI SAI không
   · hỏi ÍT + nội dung NHIỀU   → ③ ĐANG PHÍ, cắt bớt
   · hỏi ÍT + nội dung ÍT      → ④ để yên

③ TOP 10 CÂU CHÉP
   Câu hỏi ĐẦU TIÊN của khách, NGUYÊN VĂN, đã bỏ hết tên/SĐT/địa chỉ, kèm HT-nnn.
   Đây là hook thị trường đã viết sẵn — chép, đừng viết lại cho hay.

④ PHÂN BỐ NẤC 5A
   % hội thoại ở A1..A5. Nếu >60% rơi A3 thì nói thẳng: phễu đang thiếu A1–A2.

⑤ BA Ô TRỐNG NẶNG NHẤT
   Ô 5A × chân dung đang trống trong ma trận MÀ có mã O cao.

⑥ GHI CHÚ TẦNG HAI — đọc nửa TRỰC PAGE TRẢ LỜI
   · đoạn nào trực page phải gõ tay lặp lại nhiều hội thoại → thiếu hẳn một clip
   · chỗ nào khách hỏi xong, được trả lời, rồi IM LUÔN → câu trả lời không đóng
     được nỗi sợ, đây là ô ② chứ không phải ô ①
   Kèm câu: "Đây là đầu vào để làm nội dung, không phải căn cứ đánh giá nhân sự."

⑦ CỠ MẪU — đọc bao nhiêu, bỏ bao nhiêu, vì sao bỏ

⛔ Không đưa tên/SĐT/ảnh/link profile khách vào bất kỳ dòng nào.
⛔ Không tự trả lời O-07 (bảo hành) và O-12 (bệnh nền).
⛔ O-00 vượt 10% mẫu thì báo lại, đừng tự thêm mã mới.
```

---

## Biến thể — chỉ muốn hook

```
Từ [n] hội thoại dưới đây, rút 10 hook theo ba cách của sp-C §6:
  ① CHÉP NGUYÊN câu hỏi đầu tiên của khách  (ưu tiên — cho 6 câu)
  ② GỘP TẦN SUẤT nhiều người hỏi cùng một ý  (cho 3 câu)
  ③ LẬT Ô TRỐNG trong ma trận chân dung      (cho 1 câu)

Mỗi hook kèm: HT-nnn truy ngược · mã O đóng · nấc · chân dung ·
chấm theo công thức 4 thành phần (① là cổng) · có trúng H1–H7 không.

⛔ Không viết hook có tính từ mà không có tình trạng cụ thể.
```

## Biến thể — một mã O

```
Mã O-05 (nghi tay nghề bác sĩ) đang [n] lần/100. Trả lời ba câu:
  ① Khách nghi cụ thể cái gì? Trích 5 câu nguyên văn.
  ② Nội dung nào đang có đáng lẽ phải đóng được mã này mà không đóng được? Vì sao?
  ③ Facebook một mình có đóng nổi mã này không? Nếu không thì cần gì ngoài Facebook?
```
