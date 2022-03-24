from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# webdriverをブラウザのバージョンにあわせて更新
driver = webdriver.Chrome(ChromeDriverManager().install())
# ブラウザ最大化
driver.maximize_window()
# サイトを開く
driver.get("https://orteil.dashnet.org/cookieclicker/")
# 要素が読み込まれるまで最大10秒待機
driver.implicitly_wait(10)
# 無限クリック
while True:
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()

