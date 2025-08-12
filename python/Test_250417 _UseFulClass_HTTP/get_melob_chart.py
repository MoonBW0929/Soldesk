# https://www.melon.com/chart/index.htm

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.melon.com/chart/index.htm")

data = driver.find_elements(By.CSS_SELECTOR, ".ellipsis a")

for n in data:
    print(n.text)

# 만약 스크롤이 필요한 사이트의 경우
# body = driver.find_element(By.CSS_SELECTOR, "body")

# for i in range(5):
#     body.send_keys(Keys.END)
#     sleep(1)