# https://news.naver.com/

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://news.naver.com/")

data = driver.find_elements(By.CSS_SELECTOR, ".cnf_news_title")

for n in data:
    print(n.text)