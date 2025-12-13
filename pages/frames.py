from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
from selenium.webdriver.common.action_chains import ActionChains
class Frames(Basepage):
    FRAMES=(By.XPATH,"//span[normalize-space()='Frames']")
    iframe=(By.XPATH,"//iframe[@id='frame1']")
    iframe2=(By.XPATH,"//div[@id='frame2Wrapper']//iframe")
    outside_frame=(By.XPATH,"//div[contains(text(),'Sample Iframe page There are 2 Iframes in this pag')]")
    def frames(self):
        self.jsclick(self.FRAMES)
        frame1=self.wait.until(EC.presence_of_element_located(self.iframe))
        self.driver.switch_to.frame(frame1)
        self.driver.switch_to.default_content()
        frame2=self.wait.until(EC.presence_of_element_located(self.iframe2))
        self.driver.switch_to.frame(frame2)
        self.driver.switch_to.default_content()
        self.wait.until(EC.presence_of_element_located(self.outside_frame))
        print("outside frames")