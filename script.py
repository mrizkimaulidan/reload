from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = input('URL (http/https) : ')

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get(url)

while True:
    browser.refresh()
