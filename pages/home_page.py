from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class HomePage:
    CONTUL_MEU_BUTTON = (By.CSS_SELECTOR, '[class="login ga-track"]')
    SEARCH_INPUT = (By.ID, "search_query_top")
    PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, "a.product-name")
    ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, "div > button#onetrust-accept-btn-handler")
    SEARCH_ERROR_MESSAGE_TEXT = (By.CSS_SELECTOR, "p.alert-warning")

    NU_ACUM_BUTTON = (By.CSS_SELECTOR, '[class="v-btn v-btn--flat v-btn--text theme--light v-size--default"]')
    URL = "https://cafeo.ro/"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        sleep(5)
        self.browser.switch_to.frame(self.browser.find_element(By.ID, "movalio-push-popup"))
        self.browser.find_element(*self.NU_ACUM_BUTTON).click()
        self.browser.switch_to.default_content()
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def click_contul_meu_button(self):
        self.browser.find_element(*self.CONTUL_MEU_BUTTON).click()

    def type_in_search_input(self, product):
        self.browser.find_element(*self.SEARCH_INPUT).send_keys(product)

    def make_a_search(self, product):
        self.type_in_search_input(product)
        self.browser.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
        sleep(5)

    def list_of_products_name(self):
        products_list = []
        web_element_list = self.browser.find_elements(*self.PRODUCT_NAME_TEXT)
        for web_element in web_element_list:
            products_list.append(web_element.text)
        return products_list

    def get_search_error_message(self):
        return self.browser.find_element(*self.SEARCH_ERROR_MESSAGE_TEXT).text


