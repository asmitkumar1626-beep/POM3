from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
class Radio(Basepage):
    RADIO=(By.XPATH,"//span[normalize-space()='Radio Button']")
    Yes=(By.XPATH,"//label[normalize-space()='Yes']")
    impressive=(By.XPATH,"//label[normalize-space()='Impressive']")

    def radio(self):
        self.jsclick(self.RADIO)
        self.click(self.Yes)
        self.click(self.impressive)

