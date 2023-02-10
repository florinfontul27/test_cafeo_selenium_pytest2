from selenium.webdriver.common.by import By


class AutentificarePage:

    INTRA_IN_CONT_BUTTON = (By.ID, 'SubmitLogin')
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "passwd")
    ERROR_MESSAGE_TEXT = (By.CSS_SELECTOR, "ol>li")

    def __init__(self, browser):
        self.browser = browser

    def click_intra_in_cont(self):
        self.browser.find_element(*self.INTRA_IN_CONT_BUTTON).click()

    def type_email(self, email):
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(email)

    def type_password(self, password):
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def get_error_message_text(self):
        return self.browser.find_element(*self.ERROR_MESSAGE_TEXT).text







