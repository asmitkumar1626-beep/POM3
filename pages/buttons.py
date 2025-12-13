from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
from selenium.webdriver.common.action_chains import ActionChains
class Buttons(Basepage):
    BUTTONS=(By.XPATH,"//span[normalize-space()='Buttons']")
    double_click=(By.XPATH,"//button[@id='doubleClickBtn']")
    CONTEXT_click=(By.XPATH,"//button[@id='rightClickBtn']")
    click_me=(By.XPATH,"//div[@class='col-12 mt-4 col-md-6']//div//div[3]//button")

    def clicks(self):
        self.jsclick(self.BUTTONS)
        ele=self.wait.until(EC.visibility_of_element_located(self.double_click))
        actions=ActionChains(self.driver)
        actions.double_click(ele).perform()
        ele2=self.wait.until(EC.visibility_of_element_located(self.CONTEXT_click))
        actions.context_click(ele2).perform()
        self.click(self.click_me)