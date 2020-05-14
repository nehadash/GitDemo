



#  self.driver.find_element_by_css_selector("a[href*='shop']").click()
from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import checkoutPage


class HomePage:

    shop = (By.CSS_SELECTOR,"a[href*='shop']" )
    name = (By.CSS_SELECTOR,"[name ='name']")
    email = (By.CSS_SELECTOR,"[name ='email']")
    checkme = (By.CSS_SELECTOR,"[for ='exampleCheck1']")
    dropdown = (By.ID,"exampleFormControlSelect1")
    submitform = (By.CSS_SELECTOR,"[type='submit']")
    sucessmessage= (By.CSS_SELECTOR,"[class ='alert alert-success alert-dismissible']")

    def __init__(self,driver):
        self.driver = driver

    def shopItems(self):
       self.driver.find_element(*HomePage.shop).click()
       checkoutpage = checkoutPage(self.driver)
       return  checkoutpage

    def getName(self):
         return self.driver.find_element(*HomePage.name)

    def getEmail(self):
         return self.driver.find_element(*HomePage.email)
    def getClickCheck(self):
         return self.driver.find_element(*HomePage.checkme)
    def getDropdown(self):
         return self.driver.find_element(*HomePage.dropdown)
    def submittForm(self):
         return self.driver.find_element(*HomePage.submitform)
    def getsuccessmessage(self):
        return self.driver.find_element(*HomePage.sucessmessage)