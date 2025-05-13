# O assert sempre verifica se o retorno da condição é TRUE.
assert True, "Assert falhou"

# assert numbers
# numero_esperado = 1
# numero_atual = 2
# assert numero_esperado == numero_atual, f"Esperado {numero_esperado} Atual {numero_atual}."
# assert numero_esperado < numero_atual, f"Esperado {numero_esperado} é maior que o número Atual {numero_atual}."

# assert text
# texto_esperado = "Selenium Webdriver"
# texto_obtido = "Selenium Webdriver"
# assert texto_esperado == texto_obtido, f"Esperado {texto_esperado}, obtido {texto_obtido}"


# assert text in string
# texto_esperado = "Selenium"
# texto_obtido = "Selenium Webdriver"
# assert texto_esperado in texto_obtido, f"Esperado '{texto_esperado}' dentro da string '{texto_obtido}'"
# assert texto_esperado not in texto_obtido, f"Esperado '{texto_esperado}' dentro da string '{texto_obtido}'"


# assert is_displayed/is_enabled/is_selected
# img_backpack = browser.find_element(By.XPATH,"(//img[@class='inventory_item_img'])[1]")
# assert img_backpack.get_attribute("alt") == "Sauce Labs Backpack", "A descrição do primeiro produto não é a esperada"
# assert img_backpack.is_displayed()
# assert img_backpack.is_enabled()
# assert img_backpack.is_selected()
