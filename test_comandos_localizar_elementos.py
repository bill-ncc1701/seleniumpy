import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
# get() - Navega para uma URL
browser.get("https://www.saucedemo.com/")

# find_element() - Localiza um elemento na página
# username = browser.find_element(By.ID, "user-name")
# password = browser.find_element(By.ID, "password")

# send_keys() - Envia texto para o elemento
# username.send_keys("standard_user")
# password.send_keys("secret_sauce")


# find_elements() - Localiza vários elementos na página
auth_fields = browser.find_elements(By.XPATH, "//*[@class='input_error form_input']")

print(auth_fields)

assert len(auth_fields) == 2, "Número de campos de autenticação é diferente do esperado."

print("Elementos encontrados:" , len(auth_fields)) #Tamanho da varíavel (numero de campos encontrados)

time.sleep(2)
browser.quit()