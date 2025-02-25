from bl.test_manager import TestManager
from data_access.config import Config
import allure


@allure.feature("Тестирование раздела 'Вышитые картины'")
def test_search_embroidery(driver):
    driver.get(Config.BASE_URL)
    test_manager = TestManager(driver)
    result = test_manager.search_artwork()
    with allure.step("Поиск картины 'Трамвайный путь'"):
        print(f"Результат поиска: {result}")
        assert result == "В наличии!"

