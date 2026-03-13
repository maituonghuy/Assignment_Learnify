---
applyTo: '**'
---

# Hướng dẫn tạo mô tả màn hình

## Đầu vào
- File mockup HTML (wireframe low-fidelity)
- Mô tả use case và yêu cầu chức năng

## Định dạng đầu ra
Tạo tài liệu mô tả màn hình đơn giản, chỉ bao gồm phần Các thành phần màn hình theo định dạng bảng markdown:

```markdown
# UC-[ID]: [Tên Use Case] - Mô tả màn hình

## Các thành phần màn hình

| Tên trường | Mô tả |
|------------|-------|
| **[Tên trường/thành phần bằng tiếng Việt]** | [Loại]: [Kiểu dữ liệu, ràng buộc, hành vi, quy tắc validation, v.v.] |
```

|Tên trường |Mô tả|
|Form Title|Text / Heading: Main heading displaying "Đăng Ký Tài Khoản" (Register Account).|
|Vai trò (Role) |Toggle Group / Buttons: Mandatory selection for the user's role, providing options for "Giáo Viên" (Teacher) and "Học Sinh" (Student).|
|Họ và Tên (Full Name) |Text Input: Mandatory input field for the user's full name with the placeholder "Nhập họ và tên của bạn".|
|Email |Email Input: Mandatory input field for the user's email with the placeholder "example@email.com" and helper text explaining it will be used for login and notifications.|


