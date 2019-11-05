from Search import GoogleShopping
from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "version": "78.0",
    "enableVNC": True,
    "enableVideo": False
}

chrome = webdriver.Remote(
    command_executor="http://selenoid:4444/wd/hub",
    desired_capabilities=capabilities)

g = GoogleShopping(chrome)

g.navigate()
bar = g.bar(chrome)
bar.send_keys('teste')