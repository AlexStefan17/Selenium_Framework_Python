import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True)
    service_obj = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()










