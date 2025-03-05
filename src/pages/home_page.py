from .base_page import BasePage

class HomePage(BasePage):

    def open_full_menu(self):
        self.wait_for_element_to_be_clickable(
            "//li[@class='menu-group gids' and @data-show='gids']"
        ).click()

    def clear_basket(self):
        self.wait_for_element_to_be_clickable("//span[@class='basketico']", 2).click()
        try:
            delete_buttons = self.wait_for_element_to_be_clickable(
                "//div[@class='c_del control']",
                2
            )

            for button in delete_buttons:
                button.click()
                # Ожидаем, пока элемент станет устаревшим
                self.wait_for_element_to_be_clickable_staleness(button)
        except:
            pass

    def go_to_embroidery(self):
        self.open_full_menu()

        # переходим в "Вышитые картины"
        self.wait_for_element_to_be_clickable(
            "//li[@class='menu-extra-item gids']/a[@href='//artnow.ru/vyshitye-kartiny-kupit.html']"
        ).click()

    def go_to_batik(self):
        self.open_full_menu()

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

    def go_to_jewelry(self):
        self.open_full_menu()

        # переходим в "Ювелирное искусство"
        self.wait_for_element_to_be_clickable(
            "//li[@class='menu-extra-item gids']/a[@href='//artnow.ru/juvelirnye-izdelija-ruchnoj-raboty.html']"
        ).click()
