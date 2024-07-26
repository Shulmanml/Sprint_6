
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    def click_on_item(self, locator):
        item = self.find_element_with_wait(locator)
        item.click()


    def get_text_from_item(self, locator):
        item = self.find_element_with_wait(locator)
        return item.text

    def scroll_to_item(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def edit_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return (method, locator)

    def get_url(self, URL):
        self.driver.get(URL)

    def get_current_url(self):
        return self.driver.current_url

    def switch_window(self, locator):
        all_windows = self.driver.window_handles
        new_window = all_windows[-1]
        self.driver.switch_to.window(new_window)
        self.find_element_with_wait(locator)


