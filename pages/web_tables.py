from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_page import Basepage
class Webtable(Basepage):
    WEBTABLE=(By.XPATH,"//span[normalize-space()='Web Tables']")
    add=(By.XPATH,"//button[@id='addNewRecordButton']")
    f_name=(By.XPATH,"//input[@id='firstName']")
    l_name=(By.XPATH,"//input[@id='lastName']")
    email=(By.XPATH,"//input[@id='userEmail']")
    age=(By.XPATH,"//input[@id='age']")
    salary=(By.XPATH,"//input[@id='salary']")
    Department=(By.XPATH,"//input[@id='department']")
    submit=(By.XPATH,"//button[@id='submit']")

    def web_tables(self):
        self.jsclick(self.WEBTABLE)
        self.jsclick(self.add)
        self.type(self.f_name,"asmit")
        self.type(self.l_name,"kanar")
        self.type(self.email,"asmitkumar7750@gmail.com")
        self.type(self.age,"33")
        self.type(self.salary,"50000000")
        self.type(self.Department,"QA automation tester")
        self.click(self.submit)
        ele=self.driver.find_elements(By.XPATH,"//div[@class='rt-tbody']//div[@class='rt-tr-group']")
        for i in ele:
            gg=i.find_elements(By.XPATH,".//div[@class='rt-td']")
            for j in gg:
                print(j.text,end="|")
            print()