from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium browser drivers\\chromedriver.exe")

driver.get("https://google.com")
driver.find_element(By.XPATH, "//*[@class='gLFyf gsfi']").send_keys("hi")
driver.find_element(By.XPATH, "//*[@class='gLFyf gsfi']").send_keys(Keys.ENTER)

driver.quit()

driver.find_element(By.XPATH, "//img[@title='Faded Short Sleeve T-shirts']").click()
driver.find_element(By.XPATH, "(//span[text()='Add to cart'])[2]").click()
driver.find_element(By.XPATH, "//a[@title='Proceed to checkout']").click()
