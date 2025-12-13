from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
from selenium.webdriver.common.action_chains import ActionChains
class Links(Basepage):
    LINKS=(By.XPATH,"//span[normalize-space()='Links']")
    home_window=(By.XPATH,"//a[@id='simpleLink']")
    def links(self):
        self.jsclick(self.LINKS)
        current=self.driver.current_window_handle
        self.click(self.home_window)
        windows=self.driver.window_handles
        for win in windows:
            if win != current:
                self.driver.switch_to.window(win)
            break
