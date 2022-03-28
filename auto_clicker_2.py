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

    #施設の要素を検索
    product = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

    # NGパターン
    # product = driver.find_elements(By.CLASS_NAME, "product unlocked enabled")


    if len(product) > 0:
        # for each文にて要素がある間繰り返す
        for product_element in product:
            count_cookie = int(driver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",", ""))
            product_cost = int(product_element.text.split("\n")[1].replace(",", ""))
            # 施設を買える枚数クッキーがある場合は購入
            if count_cookie >= product_cost:
                product_element.click()
                # ログ表示
                print("所持しているクッキー：" + str(count_cookie) + "枚")
                print(product_element.text.split("\n")[0] + "（コスト：" + str(product_cost) + ")をクリックしました")
                print("-" * 40)

    else:
        # クッキーを連打する
        cookie = driver.find_element(By.ID, "bigCookie")
        cookie.click()
