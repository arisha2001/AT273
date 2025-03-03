import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class EmbroideryPage(BasePage):
    # переход на страницу жанра "Городской пейзаж"
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

    def get_art_tram_track(self):
        self.search_by_genre()

        # в отфильтрованном окне ищем картину с названием "Трамвайный путь"
        return self.wait_for_element_to_be_clickable(
            "//div[@data-id='870972']/parent::*/div[@class='price']/following-sibling::div[@class='small']"
        ).text


    def art_tram_track_style(self):
        self.search_by_genre()

        self.driver.execute_script(
            "document.querySelectorAll('.popup-class').forEach(el => el.style.display='none');"
        )

        time.sleep(2)

        # в отфильтрованном окне открываем ссылку на картину "Трамвайный путь"
        art = self.wait_for_element_to_be_clickable(
            "//div[@class='heart' and @data-id='870972']/preceding-sibling::a"
        )
        # переходим по ссылке картины
        self.driver.execute_script("arguments[0].click();", art)

        # ищем стиль картины
        return self.wait_for_element_to_be_clickable(
            "//div[@class='txtline lft']//span[contains(text(), 'Стиль:')]/following-sibling::a"
        ).text