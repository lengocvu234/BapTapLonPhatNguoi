from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from apscheduler.schedulers.blocking import BlockingScheduler
import pytesseract
from PIL import Image
import time
import io
import base64

# Cấu hình pytesseract (đường dẫn đến tesseract.exe nếu cần)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def check_violation():
    # ----------------- MỞ TRÌNH DUYỆT -----------------
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        print("Bắt đầu kiểm tra phạt nguội...")

        # ----------------- VÀO TRANG WEB -----------------
        driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.htm")
        print("Đã vào trang csgt.vn")

        # ----------------- NHẬP BIỂN SỐ -----------------
        try:
            id_bien_so = "bienSo"
            bien_so = "38A23216"  # Biển số cần kiểm tra
            input_bien_so = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, id_bien_so))
            )
            input_bien_so.clear()
            input_bien_so.send_keys(bien_so)
            print(f"Đã nhập biển số xe: {bien_so}")
        except Exception as e:
            print(f"Lỗi khi nhập biển số: {e}")

        # ----------------- CHỌN LOẠI PHƯƠNG TIỆN (Ô TÔ) -----------------
        try:
            option_selector = "//*[@id='loaiPhuongTien']/option[@value='1']"  # Giá trị '1' là ô tô
            option_o_to = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, option_selector))
            )
            option_o_to.click()
            print("Đã chọn phương tiện Ô Tô")
        except Exception as e:
            print(f"Lỗi khi chọn loại phương tiện: {e}")

        # ----------------- TRÍCH XUẤT MÃ BẢO MẬT -----------------
        try:
            captcha_img = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "captchaImage"))
            )
            captcha_src = captcha_img.get_attribute("src")
            captcha_data = base64.b64decode(captcha_src.split(",")[1])
            captcha_image = Image.open(io.BytesIO(captcha_data))
            captcha_text = pytesseract.image_to_string(captcha_image, config='--psm 6').strip()
            print(f"Mã bảo mật trích xuất: {captcha_text}")

            # Nhập mã bảo mật
            captcha_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "captchaInput"))
            )
            captcha_input.clear()
            captcha_input.send_keys(captcha_text)
        except Exception as e:
            print(f"Lỗi khi xử lý mã bảo mật: {e}")

        # ----------------- CLICK NÚT TÌM KIẾM -----------------
        try:
            xpath_btn = '//*[@id="btnTraCuu"]'
            element_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath_btn))
            )
            element_btn.click()
            print("Đang kiểm tra vi phạm...")
        except Exception as e:
            print(f"Lỗi khi nhấn nút tìm kiếm: {e}")

        # ----------------- CHỜ KẾT QUẢ HIỂN THỊ -----------------
        try:
            result_selector = "#resultContainer"
            element_result = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, result_selector))
            )
            text_result = element_result.text

            # ----------------- HIỂN THỊ KẾT QUẢ -----------------
            print("\n Kết quả kiểm tra biển số:", bien_so)
            print("---------------------------------------------------")
            print(text_result)

            if "Không tìm thấy kết quả" in text_result:
                print("Không có vi phạm phạt nguội.")
            else:
                print("Đã tìm thấy vi phạm phạt nguội!")
        except Exception as e:
            print(f"Lỗi khi lấy kết quả: {e}")

    except Exception as e:
        print(f"Lỗi không xác định: {e}")

    finally:
        driver.quit()
        print("Đã đóng trình duyệt.")

# ----------------- LẬP LỊCH CHẠY -----------------
scheduler = BlockingScheduler()
scheduler.add_job(check_violation, 'cron', hour=6, minute=0)  # Chạy lúc 6h sáng
scheduler.add_job(check_violation, 'cron', hour=12, minute=0)  # Chạy lúc 12h trưa

print("Đang chạy lịch trình kiểm tra phạt nguội...")
scheduler.start()