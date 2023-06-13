import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        checkOutPage = CheckOutPage(self.driver)
        cards = checkOutPage.getCardTitles().click()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkOutPage.checkOutItems().click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "India")))
        # TODO POM
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()

        success_test = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you" in success_test
