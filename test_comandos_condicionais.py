import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from typing_extensions import assert_type

browser = webdriver.Chrome()

browser.get("https://demo.applitools.com")

username = browser.find_element(By.ID, "username")
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@type='checkbox']")

#is_displayed() - Verifica se o elemento está visível na página
print("O Elemento username está visível:",username.is_displayed())
print("O Elemento 'remember me' está visível:",checkbox_remember_me.is_displayed())

#is_enabled() - Verifica se o elemento está habilitado
print("O Elemento username está habilitado:",username.is_enabled())
print("O Elemento 'remember me' está habilitado:",checkbox_remember_me.is_enabled())

#is_selected() - Verifica se o elemento está selecionado
print("O Elemento 'remember me' está selecionado:",checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected()

# Seleciona o checkbox
checkbox_remember_me.click()
assert checkbox_remember_me.is_selected()
print("O Elemento 'remember me' está selecionado:",checkbox_remember_me.is_selected())
time.sleep(5)

browser.quit()