

from selenium.webdriver.common.by import By





#self.driver.find_elements_by_xpath("//div[@class='card h-100']")
#product.find_element_by_xpath('div/h4/a').text
#driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
#self.driver.find_element_by_css_selector("button[class='btn btn-success']").click()
from pageObjects.ConfirmPage import confirmPage


class checkoutPage:
    productname = (By.XPATH,"//div[@class='card h-100']")
    product = (By.XPATH,"//div[@class='card h-100']/div/h4/a")
    button = (By.CSS_SELECTOR,"a[class='nav-link btn btn-primary']")
    button2 = (By.CSS_SELECTOR,"button[class='btn btn-success']")


    def __init__(self,driver):
        self.driver = driver



    def getproductname(self):
        return self.driver.find_elements(*checkoutPage.productname)

    def getproduct(self):
        return self.driver.find_element(*checkoutPage.product)

    def getClick(self):
        return  self.driver.find_element(*checkoutPage.button)

    def getClick1(self):
          self.driver.find_element(*checkoutPage.button2).click()
          confirmPage1 = confirmPage(self.driver)

          return confirmPage1
