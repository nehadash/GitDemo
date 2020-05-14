from selenium.webdriver.common.by import By


class confirmPage:
    # self.driver.find_element_by_id("country").send_keys("ind")
    countrry = (By.ID,"country")
    #self.driver.find_element_by_link_text("India").click()
    country1 = (By.LINK_TEXT,"India")
    #self.driver.find_element_by_css_selector("div[class='checkbox checkbox-primary']").click()
    agree = (By.CSS_SELECTOR,"div[class='checkbox checkbox-primary']")
    #self.driver.find_element_by_css_selector("input[type='submit']").click()
    purcahse = (By.CSS_SELECTOR,"input[type='submit']")
    #elf.driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text
    alert = (By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']")

    def __init__(self,driver):
        self.driver = driver

    def countryerror(self):
        return  self.driver.find_element(*confirmPage.countrry)



    def getCountry1(self):
        return self.driver.find_element(*confirmPage.country1)

    def getAgree(self):
        return self.driver.find_element(*confirmPage.agree)

    def getPurchase(self):
        return self.driver.find_element(*confirmPage.purcahse)

    def getAlert(self):
        return self.driver.find_element(*confirmPage.alert)






