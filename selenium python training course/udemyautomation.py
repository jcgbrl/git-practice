import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/selenium browser drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)  # 5 seconds is the max time out

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "email").send_keys("gab@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text  # store text
print(message)
assert "submitted" in message  # verify text

# static dropdown
dropdown = Select(driver.find_element(By.NAME, ""))
dropdown.select_by_visible_text("")  # or
dropdown.select_by_index(0)

# dynamic dropdown
driver.find_element(By.ID, "").send_keys("ind")
time.sleep(2)

alert = driver.switch_to.alert  # alert modal
alert.accept()  # yes
alert.dismiss()  # no

action = ActionChains(driver)  # hover mouse
action.move_to_element(driver.find_element(By.ID, "")).perform()

driver.switch_to.frame("frame id")  # for frames

driver.get_screenshot_as_png()  # screenshot

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")

#  service_obj = Service("C:/selenium browser drivers/chromedriver.exe")
#  driver = webdriver.Chrome(service=service_obj,options=chrome_options)
