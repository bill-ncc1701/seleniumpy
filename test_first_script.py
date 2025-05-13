import time

from selenium import webdriver


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://google.com")
time.sleep(5)
browser.quit()