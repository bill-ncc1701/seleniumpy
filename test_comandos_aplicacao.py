from selenium import webdriver

browser = webdriver.Chrome()

# get() - Navega para uma URL
browser.get("https://www.saucedemo.com/")

# title() - Retorna o título da página
print("O titulo da página é: ", browser.title)

# current_url() - Retorna a URL atual
print("A URL atual é: ", browser.current_url)

# page_source() - Retorna o código-fonte da página
print("O código-fonte da página é: ", browser.page_source)
