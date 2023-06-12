from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
        return self.driver.find_element(*HomePage.shop)
