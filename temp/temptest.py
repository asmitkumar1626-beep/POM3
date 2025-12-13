import time
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demoqa.com/nestedframes")
driver.maximize_window()
iframe=driver.find_element(By.XPATH,"//iframe[@id='frame1']")
driver.switch_to.frame(iframe)
print("we inside the parent")
iframe2=driver.find_element(By.XPATH,"//iframe[contains(@srcdoc,'Child Iframe')]")
driver.switch_to.frame(iframe2)
print("we inside the child")
driver.switch_to.parent_frame()
print("we out side the child")
driver.switch_to.default_content()
print("we outside the parent too!")

# driver.find_element(By.XPATH,"//button[@id='promtButton']").click()

time.sleep(2)