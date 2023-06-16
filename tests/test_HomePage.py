import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import pytest


class TestHomePage(BaseClass):

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param


    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info(f"first name is {getData['firstname']}")
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByTest(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

