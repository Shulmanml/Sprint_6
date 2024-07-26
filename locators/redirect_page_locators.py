from selenium.webdriver.common.by import By

class RedirectPageLocators:
    # заголовок блока новостей
    NEWS_BLOCK_HEADER = (By.XPATH, '//*[@class = "floor-title__title-2v" and text() = "Новости"]')
