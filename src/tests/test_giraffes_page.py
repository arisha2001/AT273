from bl.test_manager import TestManager
from data_access.config import Config
import allure


@allure.step("Проверка содержания слова 'Жираф' в названии первой картины")
def test_word_presence(driver):
    driver.get(Config.BASE_URL)
    test_manager = TestManager(driver)
    name_art = test_manager.word_giraffes_exists()
    with allure.step("Проверка содержания слова 'Жираф' в названии первой картины"):
        assert "Жираф" in name_art
