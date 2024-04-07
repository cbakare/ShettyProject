from selenium.webdriver.common.by import By


class HomePageObject:
    def __init__(self,driver):
        self.driver=driver

    def getEmailObject(self):
        return self.driver.find_element(By.NAME,'email')

    def getPasswordObject(self):
        return self.driver.find_element(By.ID,'exampleInputPassword1')

    def getCheckboxObject(self):
        return self.driver.find_element(By.ID,'exampleCheck1')

    def SubmitButton(self):
        return self.driver.find_element(By.XPATH,"//input[@class='btn btn-success']")

    def SuccessMsgHomePage(self):
        return self.driver.find_element(By.XPATH,'//./strong')


