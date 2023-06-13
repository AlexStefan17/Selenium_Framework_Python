import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = Options()
        # chrome_options.add_experimental_option("detach", True)
        # linux
        service_obj = Service("/usr/bin/chromedriver")
        # work
        # service_obj = Service("D:\ChromeDriver")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    elif browser_name == "firefox":
        service_obj = Service("/usr/bin/geckodriver")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "ie":
        #TODO IE invocation
        pass

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()










