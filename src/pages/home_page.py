from .base_page import BasePage

class HomePage(BasePage):

    def go_to_embroidery(self):
        self.wait_for_element_to_be_clickable(
            "//li[@class='menu-group gids' and @data-show='gids']"
        ).click()

        # переходим в "Вышитые картины"
        self.wait_for_element_to_be_clickable(
            "//li[@class='menu-extra-item gids']/a[@href='//artnow.ru/vyshitye-kartiny-kupit.html']"
        ).click()

    def go_to_batik(self):
        self.wait_for_element_to_be_clickable(
            "//li[@class='menu-group gids' and @data-show='gids']"
        ).click()

        # переходим в "Батик"
        self.wait_for_element_to_be_clickable(
            "//li[@class='menu-extra-item gids']/a[@href='//artnow.ru/batik-kartiny-kupit.html']"
        ).click()

    def go_to_giraffes(self):
        input_element = self.find_element_by_xpath("//input[@name='qs']")

        input_element.send_keys("Жираф")

        self.find_element_by_xpath(
            "//button[@type='submit' and @class='control scLarge' and contains(text(), 'Искать')]"
        ).click()