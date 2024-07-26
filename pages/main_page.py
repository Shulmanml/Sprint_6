import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Клик на вопрос')
    def click_on_question(self, num):
        edited_question_locator = self.edit_locator(MainPageLocators.QUESTION_LOCATOR, num)
        self.click_on_item(edited_question_locator)


    @allure.step('Получение текста ответа на вопрос')
    def get_text_from_answer(self, num):
        edited_answer_locator = self.edit_locator(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_item(edited_answer_locator)


    def click_to_question_and_get_answer_text(self, num):
        self.click_on_item(MainPageLocators.COOKIES_BUTTON)
        self.scroll_to_item(MainPageLocators.LAST_QUESTION)
        self.click_on_question(num)
        return  self.get_text_from_answer(num)

    @allure.step('Клик по лого самоката')
    def click_on_logo_samokat(self):
        self.click_on_item(MainPageLocators.COOKIES_BUTTON)
        self.click_on_item(MainPageLocators.TOP_ORDER_BUTTON)
        self.click_on_item(MainPageLocators.LOGO_SAMOKAT)

