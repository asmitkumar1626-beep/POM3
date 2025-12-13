from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
class Text(Basepage):
    ELEMENTS=(By.XPATH,"//div[@class='category-cards']//div[1]//div[1]//div[2]")
    TEXT=(By.XPATH,"//span[normalize-space()='Text Box']")
    Username=(By.XPATH,"//input[@id='userName']")
    Email=(By.XPATH,"//input[@id='userEmail']")
    Address=(By.XPATH,"//textarea[@id='currentAddress']")
    Permanentadress=(By.XPATH,"//textarea[@id='permanentAddress']")

    def text_box(self):
        self.jsclick(self.ELEMENTS)
        self.jsclick(self.TEXT)
        self.type(self.Username,"asmit")
        self.type(self.Email,"asmitkumar7750@gmail.com")
        self.type(self.Address,"MIG 1 15/9 BDA COLONY BBSR")
        self.type(self.Permanentadress,"MIG 1 15/9 BDA COLONY BBSR")