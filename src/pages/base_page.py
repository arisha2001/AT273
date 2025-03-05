from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def find_element_by_css(self, css):
        return self.driver.find_element(By.CSS_SELECTOR, css)

    def wait_for_element_to_be_clickable(self, xpath, timeout=10):
        """Ожидание, пока элемент станет кликабельным."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(
                (By.XPATH, xpath)
            )
        )

    def wait_for_element_to_be_clickable_css(self, css, timeout=10):
        """Ожидание, пока элемент станет кликабельным."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, css)
            )
        )