import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

wait = WebDriverWait(browser, 30)

#Busca o alert javascript na tela.
browser.find_element(By.ID, "alert")
# Esperar até que o alert esteja presente.
wait.until(EC.alert_is_present())

#Buscar o texto modificado de Site para Selenium Webdriver.
browser.find_element(By.ID, "populate-text")
wait.until(EC.text_to_be_present_in_element((By.XPATH,"//*[@class='target-text']"), "Selenium Webdriver"))
target_text = browser.find_element(By.XPATH,"//*[@class='target-text']").text
assert target_text == "Selenium Webdriver", "Texto esperado: Selenium Webdriver, mas encontrado: {target_text}"

#Testa se o primeiro botão ficou visivel.
browser.find_element(By.ID, "display-other-button")
wait.until(EC.element_to_be_clickable((By.ID, "hidden")))

#Testa se o segundo botão foi habilitado.
browser.find_element(By.ID, "display-other-button")
wait.until(EC.element_to_be_clickable((By.ID, "disable")))

#Testa se o checkbox foi clicado.
checkbox = browser.find_element(By.ID, "ch")
browser.find_element(By.ID, "checkbox").click()
wait.until(EC.element_located_to_be_selected(ch)



time.sleep(5)
browser.quit()