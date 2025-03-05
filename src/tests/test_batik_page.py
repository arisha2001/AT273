from bl.test_manager import TestManager
from data_access.config import Config
import allure


@allure.step("Проверка сохранения первой картины в разделе 'Избранное' ")
def test_art_presence(driver):
    driver.get(Config.BASE_URL)
    test_manager = TestManager(driver)
    with allure.step("Батик проверка добавления в 'Избранное'"):
        assert test_manager.batik_first_fav() == "1167739"
