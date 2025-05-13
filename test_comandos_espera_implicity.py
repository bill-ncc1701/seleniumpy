import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()

#A cada comando deve esperar "ATÉ" 12 segundos. Se antes dos 12 segundos o conteudo da págia for exebibido
# o script continua.
browser.implicitly_wait(12)
browser.get("https://chercher.tech/practice/implicit-wait")

checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
assert checkbox.is_displayed()

print("O Checkbox está na tela.")


browser.quit()