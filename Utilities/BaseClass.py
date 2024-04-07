import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class BaseClass:
    def __init__(self,driver):
        self.driver=driver

    def EnterText(self, xpath, value):
        xpath.send_keys(value)

    def ClickElement(self,Obj):
        Obj.click()

    def getText(self, xpath):
        msg=xpath.text
        return msg


    def BottomScroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
