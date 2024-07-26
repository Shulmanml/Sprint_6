import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('кликнуть по кукам и кнопке заказа')
    def click_cookies_and_order_button(self, locator):
        self.click_on_item(MainPageLocators.COOKIES_BUTTON)
        self.scroll_to_item(locator)
        self.click_on_item(locator)

    @allure.step('внести имя')
    def set_name(self, name):
        self.find_element_with_wait(OrderPageLocators.NAME_FIELD).send_keys(name)

    @allure.step('внести фамилию')
    def set_surname(self, surname):
        self.find_element_with_wait(OrderPageLocators.SURNAME_FIELD).send_keys(surname)

    @allure.step('внести адрес доставки')
    def set_address(self, address):
        self.find_element_with_wait(OrderPageLocators.Address_FIELD).send_keys(address)

    @allure.step('Выбор станции метро')
    def set_metro_station(self, stationLocator):
        self.click_on_item(OrderPageLocators.METRO_STATION_FIELD)
        self.click_on_item(stationLocator)

    @allure.step('внести номер телефона')
    def set_phonenumber(self, phonenumber):
        self.find_element_with_wait(OrderPageLocators.PHONE_NUMBER_FIELD).send_keys(phonenumber)

    @allure.step('Кликнуть по кнопке далее')
    def click_on_next_button(self):
        self.click_on_item(OrderPageLocators.NEXT_BUTTON)

    @allure.step('выбрать дату доставки')
    def set_delivery_date(self, num):
        self.click_on_item(OrderPageLocators.DATE_FIELD)
        edited_date_locator = self.edit_locator(OrderPageLocators.ORDER_DATE_FIELD, num)
        self.click_on_item(edited_date_locator)

    @allure.step('указать срок аренды')
    def set_rental_period(self, locator):
        self.click_on_item(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_on_item(locator)

    @allure.step('выбор цвета')
    def choose_colour_scooter(self, locator):
        self.click_on_item(locator)

    @allure.step('оставить комментарий курьеру')
    def set_comments(self, comments):
        self.find_element_with_wait(OrderPageLocators.COMMENTS).send_keys(comments)

    @allure.step('кликнуть по кнопке заказать')
    def click_on_order_button(self):
        self.click_on_item(OrderPageLocators.ORDER_BUTTON)

    @allure.step('подтвердить заказ')
    def click_on_confirm_button(self):
        self.click_on_item(OrderPageLocators.CONFIRM_BUTTON)


    def do_order(self, order_locator, name,surname,address,station_locator, phone_number,date, rental_period,
                 colour_scooter, comments):
        self.click_cookies_and_order_button(order_locator)
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_station(station_locator)
        self.set_phonenumber(phone_number)
        self.click_on_next_button()
        self.set_delivery_date(date)
        self.set_rental_period(rental_period)
        self.choose_colour_scooter(colour_scooter)
        self.set_comments(comments)
        self.click_on_order_button()
        self.click_on_confirm_button()






