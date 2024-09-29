from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()

user_data_dir  = 'C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\'
option.add_argument(f"user-data-dir={user_data_dir}")
option.add_argument("--profile-directory=Profile 2")

# Inisialisasi WebDriver dengan opsi
driver = webdriver.Chrome(options=option)

# Tunggu sejenak hingga browser siap
driver.implicitly_wait(5)

# Akses URL
driver.get("https://x.com")

# Tunggu input sebelum menutup
input('Tekan Enter untuk keluar...')

# Tutup browser
driver.quit()
