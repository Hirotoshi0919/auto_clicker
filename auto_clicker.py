from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(10)

while True:
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()

