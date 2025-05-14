from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://checher.tech/practice/practice-dropdowns-selenium-webdriver")
