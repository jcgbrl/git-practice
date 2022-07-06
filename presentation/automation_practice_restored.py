from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:\\selenium browser drivers\\chromedriver.exe')

driver.implicitly_wait(40)

# github practice pull practice

# HOME PAGE practice practice
driver.get("http://automationpractice.com/index.php")
driver.find_element(By.XPATH, "(//a[text()='T-shirts'])[2]").click()
# T-SHIRTS PAGE
driver.find_element(By.XPATH, "//img[@title='Faded Short Sleeve T-shirts']").click()
driver.find_element(By.XPATH, "//span[text()='Add to cart']").click()
driver.find_element(By.XPATH, "//a[@title='Proceed to checkout']").click()
# SUMMARY PAGE
driver.find_element(By.XPATH, "//span[text()='Proceed to checkout']").click()
# SIGN IN PAGE
driver.find_element(By.ID, "email_create").send_keys("cambridgetest478@gmail.com")
driver.find_element(By.XPATH, "//i[@class='icon-user left']").click()
# ACCOUNT CREATION
driver.find_element(By.ID, "id_gender1").click()
driver.find_element(By.ID, "customer_firstname").send_keys("Test First")
driver.find_element(By.ID, "customer_lastname").send_keys("Test Last")
driver.find_element(By.ID, "passwd").send_keys("Cambridge123")
driver.find_element(By.ID, "address1").send_keys("Test Address 123")
driver.find_element(By.ID, "city").send_keys("Houston")
state = driver.find_element(By.ID, "id_state")
stateDD = Select(state)
stateDD.select_by_visible_text("Texas")
driver.find_element(By.ID, "postcode").send_keys("12345")
driver.find_element(By.ID, "phone_mobile").send_keys("1234567890")
driver.find_element(By.ID, "submitAccount").click()
# ADDRESS PAGE
driver.find_element(By.XPATH, "//span[text()='Proceed to checkout']").click()
# SHIPPING
driver.find_element(By.ID, "cgv").click()
driver.find_element(By.NAME, "processCarrier").click()
# PAYMENT
driver.find_element(By.CLASS_NAME, "bankwire").click()
driver.find_element(By.XPATH, "//span[text()='I confirm my order']").click()

driver.quit()

print("\n100% Passed")
