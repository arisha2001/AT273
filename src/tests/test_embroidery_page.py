from bl.test_manager import TestManager
from data_access.config import Config
import allure


@allure.step("Проверка наличия картины 'Трамвайный путь'")
def test_art_presence(driver):
    driver.get(Config.BASE_URL)
    test_manager = TestManager(driver)
    with allure.step("Поиск картины 'Трамвайный путь'"):
        assert test_manager.search_art_tram_track() == "В наличии!"


@allure.step("Проверка стиля картины 'Трамвайный путь'")
def test_art_style(driver):
    driver.get(Config.BASE_URL)
    test_manager = TestManager(driver)
    with allure.step("Стиль картины 'Трамвайный путь'"):
        assert test_manager.tram_track_style() == "Реализм"
