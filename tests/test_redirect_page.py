

class TestRedirectPage:
    def test_click_on_logo_yandex_redirect_yandex_page(self, redirect_page):
        new_page = redirect_page.clik_on_logo_yandex()
        assert new_page == 'https://dzen.ru/?yredirect=true'


