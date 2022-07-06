import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def chromeinvocation(request):

    service_obj = Service("C:/selenium browser drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)

    driver.get("https://qa-shopfront.cambridgedev.org/")

    driver.maximize_window()

    driver.implicitly_wait(10)

    request.cls.driver = driver

    yield

    driver.close()
