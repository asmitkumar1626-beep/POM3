from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
from selenium.webdriver.common.action_chains import ActionChains
class Nested_Frames(Basepage):
    NESTED=(By.XPATH,"//span[normalize-space()='Nested Frames']")
    parent=(By.XPATH,"//iframe[@id='frame1']")
    child=(By.XPATH,"//iframe[contains(@srcdoc,'Child Iframe')]")
    def nested(self):
        self.jsclick(self.NESTED)
        frame1=self.wait.until(EC.presence_of_element_located(self.parent))
        self.driver.switch_to.frame(frame1)
        print("we inside the parent")
        frame2=self.wait.until(EC.presence_of_element_located(self.child))
        self.driver.switch_to.frame(frame2)
        print("we inside the child now")
        self.driver.switch_to.parent_frame()
        print("in parent frame")
        self.driver.switch_to.default_content()
        print("we outside!!")
