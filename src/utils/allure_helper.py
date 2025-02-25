import allure

@allure.step("Сделать скриншот")
def take_screenshot(driver):
    screenshot_path = "screenshot.png"
    driver.save_screenshot(screenshot_path)
    allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG)