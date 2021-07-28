from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests

print('1. Reload using webdriver browser\n2. Reload with request get')

options = int(input('Choose your options : '))

if options == 1:
    print('Option %s selected' % options)
    url = input('URL (http/https) : ')

    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.get(url)

    while True:
        browser.refresh()

else:
    print('Option %s selected' % options)
    url = input('URL (http/https) : ')

    while True:
        requests.get(url)
