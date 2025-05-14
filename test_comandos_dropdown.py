import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://checher.tech/practice/practice-dropdowns-selenium-webdriver")

dropdown_products = Select (browser.find_element(By.XPATH,"//select[@id='first']"))
dropdown_products.select_by_visible_text("Google")
time.sleep(3)

dropdown_animals = Select (browser.find_element(By.XPATH,"//select[@id='animals']"))
dropdown_animals.select_by_value("babycat")
time.sleep(3)
dropdown_animals.select_by_index(3) #Seleciona o item Avatar

dropdown_food = Select (browser.find_element(By.XPATH,"//select[@id='second']"))
dropdown_food.select_by_visible_text("Pizza")
time.sleep(3)
dropdown_food.select_by_visible_text("Bonda")
time.sleep(3)



