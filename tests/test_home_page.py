from pages.home_page import HomePage

def test_search_functionality(browser):
    search_text = "capsule lavazza"
    home_page = HomePage(browser)
    home_page.load_page()
    home_page.make_a_search(search_text)
    for text in home_page.list_of_products_name():
        assert search_text in text.lower(), f'{search_text} nu se gaseste in resultatul cautarii {text}'

def test_search_functionality_error_message(browser):
    search_text = "tdhgcb"
    home_page = HomePage(browser)
    home_page.load_page()
    home_page.make_a_search(search_text)
    assert "Nu am găsit niciun produs care să se potrivească cu termenul căutat:" in home_page.get_search_error_message()
    assert search_text in home_page.get_search_error_message(), f'{search_text} text nu se afla in mesajul de eroare'