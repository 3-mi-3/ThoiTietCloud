# WEB THÔNG TIN THỜI TIẾT CƠ BẢN
## Giới thiệu
Project bao gồm 2 ứng dụng web:
* App 1: Thêm, sửa, xóa, hiển thị danh sách, tìm kiếm thông tin thời tiết, lưu thông tin lên Cloud
* App 2: Lấy thông tin từ Cloud để hiển thị danh sách thời tiết, có tính năng lọc theo thời gian
## Công nghệ và thuật toán sử dụng
* Python Flask – Backend xử lý server
* HTML + Bootstrap – Giao diện người dùng
* Firebase: lưu trữ CSDL
## Giao diện minh họa
**Giao diện App 1**
<img width="1361" height="622" alt="image" src="https://github.com/user-attachments/assets/5de7ff6e-a7d5-496b-bb70-095d7da14929" />

**Giao diện App 2**
<img width="1351" height="623" alt="image" src="https://github.com/user-attachments/assets/02b14b2a-38c4-4009-819f-0f82070f0e54" />

## Hướng dẫn cài đặt
**Yêu cầu:**
* Python 3.10 trở lên
* Các thư viện: flask, firebase-admin, requests, datetime
* File cấu hình Firebase: thoi-tiet-debe0-firebase-adminsdk-fbsvc-f4358b344f.json hoặc file tương ứng từ Firebase project của bạn

**Cài đặt:**
1. Clone repo: git clone https://github.com/your-username/ThoiTietCloud.git
2. Tạo Firebase Project của bạn và tải về file Firebase .json, thay thế đường dẫn file vào dòng `cred = credentials.Certificate("./thoi-tiet-debe0-firebase-adminsdk-fbsvc-f4358b344f.json")` trong file app1.py và app2.py
3. Cài thư viện: `pip install flask firebase-admin requests datetime`
4. Chạy server: python app1.py và app2.py
5. Mở trình duyệt và truy cập: http://localhost:5000 cho App 1 và http://localhost:5001 cho App 2
