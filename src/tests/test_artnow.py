from bl.test_manager import TestManager
from data_access.config import Config
import allure


@allure.step("Проверка наличия картины 'Трамвайный путь'")
def test_art_presence(driver):
    driver.get(Config.BASE_URL)
    test_manager = TestManager(driver)
    art_presence = test_manager.search_artwork()
    with allure.step("Поиск картины 'Трамвайный путь'"):
        assert art_presence == "В наличии!"


@allure.step("Проверка стиля картины 'Трамвайный путь'")
def test_art_style(driver):
    driver.get(Config.BASE_URL)
    test_manager = TestManager(driver)
    style_art = test_manager.artwork_style()
    with allure.step("Стиль картины 'Трамвайный путь'"):
        assert style_art == "Реализм"
