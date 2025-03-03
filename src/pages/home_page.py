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
