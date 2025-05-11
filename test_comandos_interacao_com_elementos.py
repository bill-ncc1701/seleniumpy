import time
from zipimport import alt_path_sep

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/")

# find_element
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")

# send_keys
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# click
btn_login.click()

# text
products_title = browser.find_element(By.XPATH,"//span[@class='title']")
print("O Título da página é",products_title.text)
assert products_title.text == "Products", "O título da página não é o esperado"

# get_attribute
img_backpack = browser.find_element(By.XPATH,"(//img[@class='inventory_item_img'])[1]")
assert img_backpack.get_attribute("alt") == "Sauce Labs Backpack", "A descrição do primeiro produto não é a esperada"
print("A descrição do primeiro produto é ",img_backpack.get_attribute("alt"))

time.sleep(5)
browser.quit()