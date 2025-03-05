from bl.test_manager import TestManager
from data_access.config import Config
import allure


@allure.step("Проверка что выбранный товар находится в корзине и стоимость не изменилась")
def test_basket(driver):
    driver.get(Config.BASE_URL)
    test_manager = TestManager(driver)

    with allure.step("Проверка что выбранный товар находится в корзине и стоимость не изменилась"):
        assert "1160174" == test_manager.jewelry_basket()[0]
        assert "2 500 руб." == test_manager.jewelry_basket()[1]
