from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def wait_for_element_to_be_clickable(self, xpath, timeout=10):
        """Ожидание, пока элемент станет кликабельным."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(
                (By.XPATH, xpath)
            )
        )