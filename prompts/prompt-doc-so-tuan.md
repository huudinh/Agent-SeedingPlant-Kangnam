# PROMPT · ĐỌC SỐ TUẦN TRƯỚC — "YẾU GÌ"

> Bước B2. ⚠️ Prompt này **không** thay `Agent-AdsReport` — nó chỉ đọc số đủ để biết **tuần này nên làm nội dung gì**.

```
Đọc số liệu kỳ [07–13/10] dưới đây. Lead đếm theo [Meta / CRM].

① KIỂM CỔNG A TRƯỚC — thiếu một là dừng phần kết luận hiệu suất:
   · kỳ có ghi rõ ngày không
   · có ghi lead đếm theo Meta hay CRM không
   · có tracking chết / lệch Meta↔CRM ≥30% không
   · có ad bị từ chối/hạn chế chưa xử trong kỳ không

② PHÂN RÃ CPL — bắt buộc, trước mọi kết luận:
   CPL = (CPM/1000) ÷ (CTR × click→inbox% × inbox→lead%)
   Ghi rõ từng thành phần lệch bao nhiêu % so median 7 ngày.

   RỒI TRẢ LỜI DỨT KHOÁT MỘT CÂU:
   "Tuần này CÓ / KHÔNG phải vấn đề nội dung."
   · xấu ở CTR          → CÓ, việc của kế hoạch nội dung
   · xấu ở CPM          → KHÔNG, việc của Adnet (tệp/bid/lịch)
   · xấu ở click→inbox  → KHÔNG, việc của Kỹ thuật (điểm đến)
   · xấu ở inbox→lead   → KHÔNG, việc của Trực page (ca trực, thời gian phản hồi)

③ TẦNG RÒ — chỉ kết luận ở tầng NHỎ NHẤT, các tầng sau ghi "hệ quả kéo theo"

④ CHẤM NỘI DUNG theo cột HOOK (không chấm theo tên ad nếu có cột hook):
   🟢 CTR≥median VÀ CPL≤median · 🟡 một trong hai · 🔴 CTR≤−30% median VÀ CPM trong ±15%
   Mỗi dòng kèm CỠ MẪU. Dưới ngưỡng mẫu thì ghi CHƯA ĐỦ MẪU, đừng chấm.

⑤ BÃO HOÀ & CHALLENGER
   · frequency ≥2,5 kèm CTR giảm ≥20%
   · 1 ad chiếm ≥60% chi ad set
   · ★ ad set nào ≥14 ngày không có creative mới

⑥ CHẶN KẾT LUẬN — kiểm bốn thứ trước khi kết luận bất cứ điều gì:
   · đang so cuối tuần với ngày thường → HUỶ kết luận
   · ngày đầu sau khi ưu đãi kết thúc → GIẢI THÍCH, không quy trách nhiệm
   · CPM tăng ≥30% ở ≥70% ad set → đó là THỊ TRƯỜNG, không ai sửa bằng đổi creative
   · ad vừa bị từ chối → số của ad đó không dùng để chấm nội dung

⑦ BỐN ĐƯỜNG CẢI TIẾN — xếp từng nội dung vào đúng một đường:
   nhân bản (🟢, giữ nguyên hook, đổi chân dung/khu vực/bác sĩ)
   biến thể (🟡, đổi ĐÚNG MỘT biến)
   giữ ý bỏ hook (🔴 nhưng mã O vẫn cao trong hội thoại)
   bỏ hẳn (🔴 và mã O thấp)
   ⛔ Không đổi ≥3 biến cùng lúc.

Số ghi theo quy ước: 412k · 18,2tr · 1,8% · lệch ghi cả % và tuyệt đối.
```

---

## Biến thể — so một bác sĩ với team

```
Bác sĩ [BS03 Huyên] tuần [45]: CPL/CPB/CTR của người này so với MEDIAN TEAM
cùng khu vực, cùng chuyên khoa.

⚠️ Chỉ kết luận khi có ≥2 tuần liên tiếp cùng chiều. Dưới đó ghi CHƯA ĐỦ KỲ.
⚠️ Kèm câu: "Đây là đầu vào để chọn nội dung, không phải căn cứ đánh giá bác sĩ."
```

## Biến thể — thiếu cột hook

```
File số liệu này không có cột HOOK. Chấm theo tên ad được bao nhiêu thì chấm,
và ghi rõ ở đầu: độ tin thấp, cần khối Ads bổ sung cột HOOK vào báo cáo tuần.
```
