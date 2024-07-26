
from selenium.webdriver.common.by import By
class OrderPageLocators:
    # поле для ввода имени
    NAME_FIELD = (By.XPATH, '//input[@placeholder = "* Имя"]')
    # поле для ввода фамилии
    SURNAME_FIELD = (By.XPATH, '//input[@placeholder = "* Фамилия"]')
    # поле для ввода адреса
    Address_FIELD = (By.XPATH, '//input[@placeholder = "* Адрес: куда привезти заказ"]')
    # поле для ввода станции метро
    METRO_STATION_FIELD = (By.XPATH, '//input[@placeholder = "* Станция метро"]')
    # локатор станции Лубянка
    LUBYANKA_STATION = (By.XPATH, '//div[@class = "Order_Text__2broi" and text() = "Лубянка"]')
    # локатор станции Черкизовская
    Cherciz_STATION = (By.XPATH, '//div[@class = "Order_Text__2broi" and text() = "Черкизовская"]')
    # поле для ввода номера телефона
    PHONE_NUMBER_FIELD = (By.XPATH, '//input[@placeholder = "* Телефон: на него позвонит курьер"]')
    # кнопка далее
    NEXT_BUTTON = (By.XPATH, '//*[contains(@class, Button_Button__ra12g) and text()="Далее"]')
    # поле для ввода даты заказа
    DATE_FIELD = (By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]')
    # локатор для выбора определенной даты
    ORDER_DATE_FIELD = (By.XPATH, '//*[@class = "react-datepicker__day react-datepicker__day--0{}"]')
    # поле для ввода срока заказа
    RENTAL_PERIOD_FIELD = (By.XPATH, '//*[@class = "Dropdown-placeholder" and text() = "* Срок аренды"]')
    # локатор для выбора одних суток аренды самоката
    RENTAL_PERIOD_1_DAY = (By.XPATH, '//*[@class = "Dropdown-option" and text() = "сутки"]')
    # локатор для выбора одних двух суток аренды самоката
    RENTAL_PERIOD_2_DAY = (By.XPATH, '//*[@class = "Dropdown-option" and text() = "двое суток"]')
    # локатор для выбора черного самоката
    BLACK_SCOOTER = (By.XPATH, '//*[@class = "Checkbox_Label__3wxSf" and text() = "чёрный жемчуг"]')
    # локатор для выбора серого самоката
    GREY_SCOOTER = (By.XPATH, '//*[@class = "Checkbox_Label__3wxSf" and text() = "серая безысходность"]')
    # поле для ввода комментария для  курьера
    COMMENTS = (By.XPATH, '//*[@placeholder = "Комментарий для курьера"]')
    # кнопка подтверждения заказа
    CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(),"Да")]')
    # кнопка заказать после подтверждения заказа
    ORDER_BUTTON = (By.XPATH, '//*[@class = "Order_Buttons__1xGrp"]/button[text() = "Заказать"]')
    # сообщение об успешном заказе
    SUCCESS_ORDER_MESSAGE = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ" and contains(text(), "Заказ оформлен")]')



