import time

from selenium import webdriver

browser = webdriver.Chrome()

# get() - Navega para uma URL
browser.get("https://google.com")

# maximize_window() - Maximiza a janela do navegador
browser.maximize_window()

# refresh() - Atualiza a página atual
browser.refresh()

browser.get("https://terra.com.br")
time.sleep(2)

# back() - Volta para a página anterior (google.com)
browser.back()

browser.get("https://uol.com.br")
time.sleep(2)
# forward() - Avança para a próxima página
browser.forward()

# close() - Fecha a aba atual do navegador
#browser.close()
time.sleep(2)

# quit() - Fecha o navegador
browser.quit()



