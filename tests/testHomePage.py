import pytest
from Utilities.BaseClass import BaseClass
from pageObject import HomePage
import time


@pytest.mark.usefixtures("setup")
class Test_Homepage:

    def test_VerifyFormSubmission(self):
        base = BaseClass(self.driver)
        homepage = HomePage.HomePageObject(self.driver)
        # path=homepage.getEmailObject()
        base.EnterText(homepage.getEmailObject(),'xyz@gmail.com')
        base.EnterText(homepage.getPasswordObject(),'pqr')
        time.sleep(5)
        base.ClickElement(homepage.getCheckboxObject())
        time.sleep(5)
        base.BottomScroll()
        base.ClickElement(homepage.SubmitButton())
        time.sleep(2)
        msg=base.getText(homepage.SuccessMsgHomePage())
        assert 'Success' in msg





