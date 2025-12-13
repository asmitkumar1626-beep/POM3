from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
from selenium.webdriver.common.action_chains import ActionChains
class Dynamic(Basepage):
    DYNAMIC=(By.XPATH,"//span[normalize-space()='Dynamic Properties']")
    invisible_link=(By.XPATH,"//button[@id='visibleAfter']")
    not_enabled_butt=(By.XPATH,"//button[@id='enableAfter']")
    def dynamic(self):
        self.jsclick(self.DYNAMIC)
        self.wait.until(EC.visibility_of_element_located(self.invisible_link))
        self.click(self.invisible_link)
        self.click(self.not_enabled_butt)
