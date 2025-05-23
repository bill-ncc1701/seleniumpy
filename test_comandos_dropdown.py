import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("http://192.168.56.103:8484/pratice-dropdowns.html")

dropdown_products = Select (browser.find_element(By.XPATH,"//select[@id='first']"))
dropdown_products.select_by_visible_text("Microsoft")
time.sleep(3)

dropdown_animals = Select (browser.find_element(By.XPATH,"//select[@id='animals']"))
dropdown_animals.select_by_value("babycat")
time.sleep(3)
dropdown_animals.select_by_index(3) #Seleciona o item Avatar

dropdown_food = Select (browser.find_element(By.XPATH,"//select[@id='second']"))
dropdown_food.select_by_visible_text("Pasta")
time.sleep(3)
dropdown_food.select_by_visible_text("Sushi")
time.sleep(3)



