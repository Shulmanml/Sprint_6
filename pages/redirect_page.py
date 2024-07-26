import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.redirect_page_locators import RedirectPageLocators

class RedirectPage(BasePage):
    @allure.step('Клик на лого яндекса')
    def clik_on_logo_yandex(self):
        self.click_on_item(MainPageLocators.COOKIES_BUTTON)
        self.click_on_item(MainPageLocators.LOGO_YANDEX)
        self.switch_window(RedirectPageLocators.NEWS_BLOCK_HEADER)
        result = self.get_current_url()
        return result
