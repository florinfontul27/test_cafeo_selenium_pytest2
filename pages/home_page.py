from selenium.webdriver.common.by import By


class HomePage:
    URL = "https://cafeo.ro/"
    CONTUL_MEU_BUTTON = (By.CSS_SELECTOR, '[class="li_login last"]')
    def __int__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_contul_meu_button(self):
        self.browser.find_element(*self.CONTUL_MEU_BUTTON).click()

