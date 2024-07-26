
import pytest
import data
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators



class TestOrderPage:
    @pytest.mark.parametrize(
        "order_locator, name, surname, address, station_locator, phone_number, date, rental_period, colour_scooter, comments",
        [
            (MainPageLocators.TOP_ORDER_BUTTON, data.name[0], data.surname[0], data.address[0],
             OrderPageLocators.LUBYANKA_STATION, data.phone_number,
             data.date[0], OrderPageLocators.RENTAL_PERIOD_1_DAY, OrderPageLocators.BLACK_SCOOTER,
             data.comments[0]),
            (MainPageLocators.BOTTOM_ORDER_BUTTON, data.name[1], data.surname[1], data.address[1],
             OrderPageLocators.Cherciz_STATION, data.phone_number,
             data.date[1], OrderPageLocators.RENTAL_PERIOD_2_DAY, OrderPageLocators.GREY_SCOOTER, data.comments[1])
        ])
    def test_order_success(self, order_page, order_locator, name, surname, address, station_locator, phone_number,
                           date, rental_period, colour_scooter, comments):
        order_page.do_order(order_locator, name, surname, address, station_locator, phone_number, date,
                            rental_period, colour_scooter, comments)
        result = order_page.get_text_from_item(OrderPageLocators.SUCCESS_ORDER_MESSAGE)
        assert "Заказ оформлен" in result





















