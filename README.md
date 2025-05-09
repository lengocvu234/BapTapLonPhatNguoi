
# Kiểm Tra Phạt Nguội Phương Tiện Giao Thông

## Mô Tả
Đây là một ứng dụng Python tự động kiểm tra phạt nguội phương tiện giao thông trên trang web của Cục Cảnh sát Giao thông Việt Nam. Ứng dụng sử dụng **Selenium** để điều khiển trình duyệt, **Tesseract OCR** để giải mã captcha, và **APScheduler** để lập lịch chạy tự động.

## Tính Năng
- Tự động truy cập trang web kiểm tra phạt nguội.
- Nhập biển số xe và chọn loại phương tiện (ô tô).
- Giải mã captcha bằng Tesseract OCR.
- Tự động nhấn nút tìm kiếm và hiển thị kết quả.
- Lập lịch chạy vào 6h sáng và 12h trưa hàng ngày.

## Yêu Cầu Hệ Thống
- **Hệ điều hành**: Windows, macOS hoặc Linux.
- **Python**: Phiên bản 3.7 trở lên.
- **Google Chrome**: Phiên bản mới nhất.
- **ChromeDriver**: Tương thích với phiên bản Google Chrome.
- **Tesseract OCR**: Cài đặt và cấu hình đường dẫn chính xác.

---

## Cài Đặt

### 1. Cài Đặt Python và Thư Viện
```bash
pip install selenium apscheduler pytesseract pillow
```

### 2. Cài Đặt Google Chrome và ChromeDriver
- Tải [Google Chrome](https://www.google.com/chrome).
- Tải ChromeDriver tương thích tại: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).
- Giải nén `chromedriver.exe` và đặt vào thư mục PATH hoặc cùng thư mục với mã nguồn.

### 3. Cài Đặt Tesseract OCR
- Tải và cài đặt: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
- Cấu hình đường dẫn trong mã Python:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

##  Sử Dụng

### 1. Chạy chương trình
```bash
python baiphatnguoi.py
```

### 2. Theo dõi kết quả
Kết quả kiểm tra phạt nguội sẽ được hiển thị trên terminal.

### 3. Lập lịch tự động
Chương trình sẽ tự động chạy vào:
- 6:00 sáng hàng ngày
- 12:00 trưa hàng ngày

---

## Hướng Dẫn Đẩy Code Lên GitHub

### 1. Cài Đặt Git
- Tải tại: [https://git-scm.com](https://git-scm.com)

### 2. Cấu Hình Git
```bash
git config --global user.name "Tên Của Bạn"
git config --global user.email "email@example.com"
```

### 3. Tạo SSH Key và Kết Nối GitHub

#### Bước 1: Kiểm Tra SSH Key
```bash
ls -al ~/.ssh
```

#### Bước 2: Tạo SSH Key (nếu chưa có)
```bash
ssh-keygen -t rsa -b 4096 -C "email@example.com"
```

#### Bước 3: Kích hoạt ssh-agent
```bash
eval "$(ssh-agent -s)"
```

#### Bước 4: Thêm SSH key vào ssh-agent
```bash
ssh-add ~/.ssh/id_rsa
```

#### Bước 5: Sao chép SSH key và thêm vào GitHub
```bash
clip < ~/.ssh/id_rsa.pub  # Trên Windows
```
- Truy cập GitHub → Settings → SSH and GPG keys → New SSH Key

### 4. Đẩy Code Lên GitHub
```bash
git init
git remote add origin git@github.com:username/tên-repo.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

---

## Lưu Ý
- Đảm bảo kết nối internet ổn định khi chạy chương trình.
- Đảm bảo ChromeDriver tương thích với phiên bản Google Chrome.
- Nếu có lỗi, hãy kiểm tra lại các bước cài đặt và cấu hình.

## Tác Giả: LÊ NGỌC VŨ
Ứng dụng được phát triển nhằm hỗ trợ người dân dễ dàng tra cứu vi phạm giao thông một cách nhanh chóng và tự động.
