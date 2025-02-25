import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class EmbroideryPage(BasePage):

    def search_by_genre(self):
        # нажимаем галочку около жанра "Городской пейзаж"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "genre257")
            )
        ).click()

        time.sleep(1)

        # Нажимаем кнопку применить фильтр по жанру "Городской пейзаж"
        self.wait_for_element_to_be_clickable(
            "//button[@type='submit' and @class='a_button' and contains(text(), 'Применить')]"
        ).click()

        time.sleep(1)

        # в отфильтрованном окне ищем картину с названием "Трамвайный путь"
        tramway_path_element = self.wait_for_element_to_be_clickable(
            "//div[@data-id='870972']/parent::*/div[@class='price']/following-sibling::div[@class='small']"
        )

        return tramway_path_element.text
