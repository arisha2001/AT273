from pages.base_page import BasePage


class BatikPage(BasePage):
    def first_to_fav(self):

        self.wait_for_element_to_be_clickable(
            "(//div[contains(@class, 'post')])[1]//div[contains(@class, 'heart')]"
        ).click()

        self.wait_for_element_to_be_clickable(
            "//span[@class='fvtico']"
        ).click()

        return self.find_element_by_xpath("//div[@class='heart']").get_attribute("data-id")
