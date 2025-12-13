from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
class Checkbox(Basepage):
    CHECKBOX=(By.XPATH,"//span[normalize-space()='Check Box']")
    checkbox=(By.XPATH,"//span[@class='rct-checkbox']")
    plus=(By.XPATH,"//button[@title='Expand all']")
    Workspase=(By.XPATH,"//label[@for='tree-node-workspace']")

    def check_box(self):
        self.jsclick(self.CHECKBOX)
        self.jsclick(self.checkbox)
        self.jsclick(self.plus)
        self.jsclick(self.Workspase)

