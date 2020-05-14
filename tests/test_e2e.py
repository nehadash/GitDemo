import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#@pytest.mark.usefixtures("setup")
from pageObjects.ConfirmPage import confirmPage
from pageObjects.HomePage import HomePage
from pageObjects.checkoutPage import checkoutPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):

        log = self.getloggingDemo()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("getting all the card titles")




        products = checkoutpage.getproductname()
        for product in products:

         productname = checkoutpage.getproduct()
         log.info(productname)

        if productname == "Blackberry":
            print("yes")
            product.find_element_by_xpath("div/button").click()

        checkoutpage.getClick().click()

        confirmPage1 =  checkoutpage.getClick1()
        log.info("Entering country name as ind")


        confirmPage1.countryerror().send_keys("ind")



        #self.driver.find_element_by_id("country").send_keys("ind")

        self.verifyLinkPresence("India")


        #self.driver.find_element_by_link_text("India").click()
        confirmPage1.getCountry1().click()
        #self.driver.find_element_by_css_selector("div[class='checkbox checkbox-primary']").click()
        confirmPage1.getAgree().click()
        #self.driver.find_element_by_css_selector("input[type='submit']").click()
        confirmPage1.getPurchase().click()
        # print(driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text)

        #success = self.driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text
        success = confirmPage1.getAlert().text
        log.info("Text received from application is " + success)

        assert "Success! Thank you!" in success