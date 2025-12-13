from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
from selenium.webdriver.common.action_chains import ActionChains
class Upload(Basepage):
    UPLOAD=(By.XPATH,"//span[normalize-space()='Upload and Download']")
    upload=(By.XPATH,"//input[@id='uploadFile']")
    def upload_download(self):
        self.jsclick(self.UPLOAD)
        self.type(self.upload,"C:/Users/asmit/OneDrive/Pictures/Screenshots/Screenshot (2).png")