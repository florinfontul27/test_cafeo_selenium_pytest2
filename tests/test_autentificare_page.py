from time import sleep

from pages.autentificare_page import AutentificarePage
from pages.home_page import HomePage


def test_login_with_invalid_credentials_no_username_no_password(browser):
    home_page = HomePage(browser)
    customer_page = AutentificarePage(browser)
    home_page.load_page()
    home_page.click_contul_meu_button()
    sleep(4)
    customer_page.click_intra_in_cont()
    sleep(5)
    assert "Adresa de e-mail este obligatorie" in customer_page.get_error_message_text()

def test_login_with_invalid_credentials(browser):
    home_page = HomePage(browser)
    customer_page = AutentificarePage(browser)
    home_page.load_page()
    home_page.click_contul_meu_button()
    customer_page.type_email("ion@ion.com")
    customer_page.type_password("start123")
    customer_page.click_intra_in_cont()
    sleep(5)
    assert "Adresa de email sau parola sunt greșite. Încearcă din nou." in customer_page.get_error_message_text()
