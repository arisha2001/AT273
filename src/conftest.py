from datetime import datetime

import pytest
from selenium import webdriver
import os

@pytest.fixture(params=["chrome", "safari"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Safari()
    # safari не хочет открываться в полноэкранном режиме
    driver.maximize_window()
    yield driver

    driver.quit()


def pytest_runtest_makereport(item, call):
    # Проверка, завершился ли тест неудачно
    if call.when == "call" and call.excinfo is not None:
        # Получаем экземпляр драйвера из фикстуры
        driver = item.funcargs['driver']
        # Делаем скриншот
        screenshot_path = f"src/Screenshots/{datetime.now()}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        driver.save_screenshot(screenshot_path)
        print(f"Скриншот сохранен: {screenshot_path}")