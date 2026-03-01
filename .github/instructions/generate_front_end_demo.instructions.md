---
applyTo: '**'
---
# Role: Senior Business Analyst & UI Architect
# Task: Tạo mockup Low-Fidelity (Wireframe) bằng HTML/CSS cho tài liệu SRS.

## 1. THÔNG TIN MÀN HÌNH (Thành viên điền vào đây):
- UC-ID: [Ví dụ: UC-41]
- Tên màn hình: [Ví dụ: Quản lý Lớp học của Gia sư]
- Mục tiêu: [Ví dụ: Hiển thị danh sách lớp đang dạy và nút tạo lớp mới]
- Các thành phần (Fields/Data):
    1. [Bộ lọc: Trạng thái lớp - Dropdown]
    2. [Bảng: Tên học sinh, Môn học, Lịch học, Học phí]
    3. [Ô tìm kiếm theo tên học sinh]
- Các nút bấm (Buttons): [Thêm lớp mới, Xuất báo cáo, Xem chi tiết, Xóa]

## 2. ĐỊNH NGHĨA ROLE VÀ MENU:

### Role 1: Giáo viên (Teacher)
Menu sidebar bao gồm:
- Trang chủ
- Quản lý lớp học
- Lịch dạy
- Học sinh
- Tài liệu
- Ngân hàng đề
- Báo cáo

### Role 2: Học sinh (Student)
Menu sidebar bao gồm:
- Trang chủ
- Lớp học của tôi
- Lịch học

### Role 3: Quản trị viên (Admin)
Menu sidebar bao gồm:
- Trang chủ
- Quản lý người dùng
- Quản lý lớp học
- Báo cáo hệ thống
- Cài đặt

### Role 4: Giáo viên trong Lớp học (Teacher in Class)
Sidebar đặc biệt khi Giáo viên vào trong một lớp học cụ thể:
- Tên lớp
- Mã lớp
- Đường dẫn chia sẻ lớp học
- Danh mục:
  + Bảng tin
  + Lịch học
  + Thành viên
  + Bài tập
  + Bảng điểm
  + Tài liệu
  + Bài giảng

### Role 5: Học sinh trong Lớp học (Student in Class)
Sidebar đặc biệt khi Học sinh vào trong một lớp học cụ thể:
- Tên lớp
- Mã lớp
- Tên giáo viên
- Danh mục:
  + Bảng tin
  + Lịch học
  + Thành viên
  + Bài tập
  + Bài giảng
  + Tài liệu

## 3. QUY ĐỊNH STYLE LOW-FIDELITY (Giữ nguyên):
- Phong cách: Wireframe đơn sắc (Grayscale).
- Màu sắc: Chỉ sử dụng Trắng, Đen, và các sắc độ của Xám (#cccccc, #f0f0f0).
- Hiển thị chữ: Tất cả chữ trên giao diện — bao gồm tiêu đề, label, nút, giá trị thực tế, và cả dữ liệu mẫu/placeholder/demo — phải hiển thị màu đen (#000000). Không sử dụng màu xám nhạt cho dữ liệu mẫu vì khó nhìn khi in/đưa vào SRS.
- Đường nét: Sử dụng Border màu đen hoặc xám đậm.
- Vùng chứa ảnh/logo: Vẽ hình chữ nhật có đường chéo (X) bên trong hoặc ghi chữ [IMAGE]. 
  * LƯU Ý QUAN TRỌNG: Khi vẽ dấu X bằng CSS (::before và ::after), PHẢI sử dụng overflow: hidden trên container để X không tràn ra ngoài. 
  * Đường chéo X phải nằm HOÀN TOÀN bên trong khung hình chữ nhật, sử dụng width: 70% hoặc calc() để tránh tràn.
  * Ví dụ CSS đúng:
    ```css
    .image-placeholder {
        overflow: hidden;
        position: relative;
    }
    .image-placeholder::before,
    .image-placeholder::after {
        width: 70%; /* Hoặc calc(100% - 20px) */
        height: 2px;
    }
    ```
- Font chữ: Sử dụng hệ thống font không chân (Sans-serif) cơ bản.
- Hiệu ứng: Không đổ bóng, không bo góc cầu kỳ, không màu mè gradient.
- Nút bấm: Dạng hình chữ nhật viền đen, nền xám nhạt để phân biệt với input.

## 4. CẤU TRÚC HTML:
- Ngôn ngữ: Tiếng Việt.
- Layout: Header (chứa tên hệ thống: "Learnify"), Sidebar (chứa các danh mục menu dạng text theo ROLE được định nghĩa ở mục 2 - chọn menu phù hợp với use case đang làm), Main Content (chứa nội dung chính).
 - Layout: Header (chứa tên hệ thống: "Learnify"), Sidebar (chứa các danh mục menu dạng text theo ROLE được định nghĩa ở mục 2 - chọn menu phù hợp với use case đang làm), Main Content (chứa nội dung chính).
  
  - Trước khi tạo: Xác nhận ROLE của màn hình (ví dụ: Giáo viên, Học sinh, Quản trị viên, Giáo viên trong Lớp học, Học sinh trong Lớp học). Dựa vào ROLE và ngữ cảnh (màn hình đứng riêng hay nằm trong 1 lớp cụ thể), chọn chính xác một trong các sidebar đã định nghĩa ở mục 2:
    + Nếu màn hình là chung cho hệ thống → dùng sidebar theo Role chung (Teacher / Student / Admin).
    + Nếu màn hình là bên trong một lớp cụ thể → dùng sidebar `Teacher in Class` hoặc `Student in Class` tương ứng, và hiển thị thêm thông tin lớp (Tên lớp, Mã lớp, Đường dẫn chia sẻ hoặc Tên giáo viên) ở phần trên của sidebar.
    + Ghi chú: luôn giữ wireframe ở dạng low-fidelity (grayscale) dù sidebar nào được chọn.

  - HƯỚNG DẪN HIỂN THỊ ƯU TIÊN (MỚI):
    + Mô phỏng giao diện ưu tiên cho KHUNG NGANG (landscape) — tương tự kích thước màn hình laptop hoặc iPad ngang. Khi chụp ảnh để đưa vào SRS, ưu tiên ảnh ngang để hiển thị đầy đủ layout và sidebar.
    + Với mockup trên thiết bị di động hoặc tablet, hãy xoay thiết bị sang chế độ NẰM NGANG (landscape) trước khi chụp — tránh mockup dọc gây thiếu thông tin hoặc toolbar bị che khuất.
    + Nếu cần, cung cấp thêm một phiên bản phụ cho màn hình dọc (portrait) chỉ khi tính năng/flow đặc biệt yêu cầu trải nghiệm dọc. Mục tiêu chính: ảnh minh họa trong SRS nên là chế độ ngang để dễ đọc.
- Output: Một file HTML duy nhất, CSS nằm trong thẻ <style>.
- Tên file: Đặt tên file theo định dạng `uc-[Ma usecase]-tên-use-case].html` (ví dụ: UC-41 có tên "Create Class" → `uc-41-createclass.html`, UC-42 có tên "Edit Class" → `uc-42-editclass.html`). Chuyển tên use case sang chữ thường và bỏ hết khoảng trắng.

## 5. YÊU CẦU:
Hãy tạo mã HTML mô phỏng chính xác cấu trúc trên để tôi chụp ảnh đưa vào tài liệu SRS. Hãy tập trung vào vị trí các trường dữ liệu và nút bấm.

## 6. LƯU Ý:
- KHÔNG thêm phần "Ghi chú về Use Case" hoặc "Additional Information" ở cuối trang.
- KHÔNG hiển thị UC-ID (như UC-41, UC-42) trong tiêu đề màn hình. Chỉ hiển thị tên màn hình thuần túy.
- Chỉ tạo form chính và các thành phần được yêu cầu trong phần 1.
- Giữ màn hình gọn gàng, chỉ hiển thị nội dung cần thiết cho wireframe.