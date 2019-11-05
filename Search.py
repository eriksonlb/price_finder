from selenium import webdriver

class Google:
  def __init__(self, driver):    
    self.driver = driver
    self.url = 'https://www.google.com.br/shopping'
    self.search_bar = 'lst-ib' #id
    self.btn_search = 'btnG' #name
    self.btn_lucky = 'btnI' #name

  def navigate(self):
    self.driver.get(self.url)

  def search(self, word='Python3'):
    self.driver.find_element_by_id(self.search_bar).send_keys(word)
    self.driver.find_element_by_name(self.btn_search).click()


# #Using Selenoid (falling)
# capabilities = {"browserName": "chrome", "version": "78.0", "enableVNC": True, "enableVideo": False}
# driver = webdriver.Remote(command_executor="http://selenoid:4444/wd/hub", desired_capabilities=capabilities)

ff = webdriver.Firefox()
g = Google(ff)
g.navigate()
g.search('Mi Band 4')
