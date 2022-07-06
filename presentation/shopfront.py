from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service("C:/selenium browser drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(10)

# SHOPFRONT HOME PAGE
driver.get("https://qa-shopfront.cambridgedev.org/")
print(driver.current_url)

# STORE BOOK 1 TITLE
booktitle1 = driver.find_element(By.XPATH, "//h2[text()='Test & Train Self-Study B2 First']").text
print(booktitle1)

# STORE BOOK 1 PRICE
bookprice1 = driver.find_element(By.XPATH, "//p[text()=' £ 20.00 ']").text
print(bookprice1)

# verify text
assert booktitle1 == driver.find_element(By.XPATH, "//h2[text()='Test & Train Self-Study B2 First']").text

time.sleep(10)

driver.find_element(By.XPATH, "(//button[text()=' Add to cart '])[1]").click()

time.sleep(10)

driver.find_element(By.XPATH, "//*[@id='app']/div[1]/header/div/div[1]/button").click()

time.sleep(10)

assert booktitle1 == driver.find_element(By.XPATH, "//*[@id='quantity-container']/div[2]/strong").text

driver.quit()
