from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/selenium browser drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://qa-shopfront.cambridgedev.org/")

print(driver.title)  # get the title
print(driver.current_url)  # get the current url

driver.back()  # go backward
driver.refresh()
driver.forward()  # go forward

message = driver.find_element(By.ID, "example").text  # store text

driver.close()
