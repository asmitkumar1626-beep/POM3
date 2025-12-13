from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
from selenium.webdriver.common.action_chains import ActionChains
class Alert(Basepage):
    ALERT=(By.XPATH,"//div[normalize-space()='Alerts, Frame & Windows']")
    alerts=(By.XPATH,"//span[normalize-space()='Alerts']")
    alert_butt=(By.XPATH,"//button[@id='alertButton']")
    delayed_alert=(By.XPATH,"//button[@id='timerAlertButton']")
    confirm_butt=(By.XPATH,"//button[@id='confirmButton']")
    def alert(self):
        ele=self.wait.until(EC.presence_of_element_located(self.ALERT))
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        self.jsclick(self.ALERT)
        self.jsclick(self.alerts)
        self.jsclick(self.alert_butt)
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        self.jsclick(self.delayed_alert)
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        self.jsclick(self.confirm_butt)
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.dismiss()
