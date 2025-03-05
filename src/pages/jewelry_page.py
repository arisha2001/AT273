from pages.base_page import BasePage


class JewelryPage(BasePage):

    def to_basket(self):
        # добавляем первый элемент в корзину
        self.wait_for_element_to_be_clickable(
            "(//div[contains(@class, 'post')])[1]//div[contains(@class, 'oclick')]"
        ).click()

        # переход в корзину
        self.wait_for_element_to_be_clickable(
            "//button[@class='ok-button' and text()='Перейти в корзину']"
        ).click()

        el_in_basket = self.wait_for_element_to_be_clickable_css('.c_row')

        # возвращаем идентификатор продукта в корзине и его стоимость
        return [
            el_in_basket.find_element_by_xpath("//div[@class='c_del control']").get_attribute("data-id"),
            el_in_basket.find_element_by_xpath(".//div[@class='price']").text
        ]

