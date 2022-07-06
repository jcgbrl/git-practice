from selenium.webdriver.common.by import By
from utilities.baseclass import baseclass

class shopfront(baseclass):

    def test_shopfront(self):

        # SHOPFRONT HOME PAGE
        self.driver.get("https://qa-shopfront.cambridgedev.org/")
        print(self.driver.current_url)

        # STORE BOOK 1 TITLE
        booktitle1 = self.driver.find_element(By.XPATH, "//h2[text()='Test & Train Self-Study B2 First']").text
        print(booktitle1)

        # STORE BOOK 1 PRICE
        bookprice1 = self.driver.find_element(By.XPATH, "//p[text()=' £ 20.00 ']").text
        print(bookprice1)

        # verify text
        assert booktitle1 == self.driver.find_element(By.XPATH, "//h2[text()='Test & Train Self-Study B2 First']").text

        self.driver.find_element(By.XPATH, "(//button[@class='btn product-card__buy-now'])[1]").click()
