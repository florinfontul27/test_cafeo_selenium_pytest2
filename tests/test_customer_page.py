from time import sleep
from pages.customer_page import CustomerPage
from pages.home_page import HomePage


def test_login_with_invalid_credentials_no_username_no_password(browser):
    home_page=HomePage(browser)
    home_page.load_page()
    home_page.click_contul_meu_button()
    customer_page = CustomerPage(browser)
    customer_page.click_intra_in_cont()
    assert "Adresa de e-mail este obligatorie" in customer_page.get_error_message_text()



def test_login_with_invalid_credentials2(browser):
    homme_page = HomePage(browser)
    homme_page.load_page()
    homme_page.click_contul_meu_button()
    customer_page = CustomerPage(browser)
    customer_page.type_email("ion@ion.com")
    customer_page.type_password("Dffdf")
    sleep(5)
    assert "Adresa de email sau parola sunt greșite. Încearcă din nou." in customer_page.get_error_message_text()
