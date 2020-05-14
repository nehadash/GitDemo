import pytest
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Testtwo(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getloggingDemo()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])

        homepage.getEmail().send_keys(getData["gender"])
        homepage.getClickCheck().click()
        homepage.getClickCheck().click()
        self.selectoptionBytext(homepage.getDropdown(),getData["gender"])

        homepage.submittForm().click()
        alertText =homepage.getsuccessmessage().text

        self.driver.refresh()


    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self,request):
        return  request.param




