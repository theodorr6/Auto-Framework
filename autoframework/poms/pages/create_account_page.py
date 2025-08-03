from autoframework.poms.pages.base_page import BasePage

class CreateAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    ACC_INFO_TITLE = "//b[text()='Enter Account Information']"
    TITLE = "//label[@for='id_gender1']"
    PASSWORD_FIELD = "//input[@type='password']"

    def verify_acc_info_title(self):
        """Verify the presence of Account Info Title."""
        return self.get_presence_of_element(self.ACC_INFO_TITLE)


    def select_title(self):
        """ Select title"""
        self.click_element(self.TITLE)

    def type_password(self, password):
        """ Type password"""
        self.fill_text(self.PASSWORD_FIELD, password)