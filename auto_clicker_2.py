import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# webdriverをブラウザのバージョンにあわせて更新
driver = webdriver.Chrome(ChromeDriverManager().install())
# ブラウザ最大化
driver.maximize_window()
# サイトを開く
driver.get("https://orteil.dashnet.org/cookieclicker/")
# 3秒待機
time.sleep(3)

# 無限クリック
while True:

    product = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    upgrade = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")

    if len(product) > 0:

        for product_element in product:
            count_cookie = int(driver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",", ""))
            product_cost = int(product_element.text.split("\n")[1].replace(",", ""))

            if count_cookie >= product_cost:
                product_element.click()

                print("所持しているクッキー：" + str(count_cookie) + "枚")
                print(product_element.text.split("\n")[0] + "（コスト：" + str(product_cost) + ")をクリックしました")
                print("-" * 40)

    else:
        cookie = driver.find_element(By.ID, "bigCookie")
        cookie.click()
