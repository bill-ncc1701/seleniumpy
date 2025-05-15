import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.maximize_window()
browser.get("http://192.168.56.103:8484/frames.html")
#time.sleep(5)

iframe1 = browser.find_element(By.ID, "iframe1")
browser.switch_to.frame("iframe1") # Switch to the first iframe

textbox = browser.find_element(By.XPATH, "//*[@id='textbox_iframe1']").send_keys("Iframe 1")
time.sleep(3)

iframe3 = browser.find_element(By.ID, "iframe3")
browser.switch_to.frame("iframe3") # Switch to the first iframe
textarea = browser.find_element(By.XPATH, "//*[@id='observacao']").send_keys("Este é o texto do Iframe 3")
time.sleep(3)

browser.switch_to.default_content()
iframe2 = browser.find_element(By.ID, "iframe2")
browser.switch_to.frame("iframe2") # Switch to the first iframe

dropdown_animals = Select (browser.find_element(By.XPATH,"//select[@id='animals']"))
dropdown_animals.select_by_visible_text("Lion")
time.sleep(3)
dropdown_animals.select_by_index(1)
time.sleep(3)
dropdown_animals.select_by_value("babycat")
time.sleep(3)

browser.quit()
