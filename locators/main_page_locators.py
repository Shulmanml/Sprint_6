
from selenium.webdriver.common.by import By
class MainPageLocators:
    # лого сайта
    LOGO_SAMOKAT = (By.XPATH, '//*[@class="Header_LogoScooter__3lsAR"]')
    # лого яндекса на сайте самоката
    LOGO_YANDEX = (By.XPATH, '//*[@class = "Header_LogoYandex__3TSOI"]')
    # кнопка куков
    COOKIES_BUTTON = (By.XPATH, '//*[@class = "App_CookieButton__3cvqF"]')
    # общий локатор для вопросов о важном
    QUESTION_LOCATOR = (By.ID, 'accordion__heading-{}')
    # общий локатор для ответов на вопросы о важном
    ANSWER_LOCATOR = (By.ID, 'accordion__panel-{}')
    # локатор последнего вопроса о важном
    LAST_QUESTION = (By.CLASS_NAME, 'Home_SubHeader__zwi_E')
    # кнопка заказа расположенная сверху
    TOP_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    # кнопка заказа расположенная в центре страницы
    BOTTOM_ORDER_BUTTON = (By.XPATH, '//*[@class = "Home_FinishButton__1_cWm"]/button[text() = "Заказать"]')

    NEWS_BLOCK_HEADER = (By.XPATH, '//*[@class = "floor-title__title-2v" and text() = "Новости"]')





