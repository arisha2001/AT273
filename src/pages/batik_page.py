from pages.base_page import BasePage


class BatikPage(BasePage):
    def first_to_fav(self):

        first_el = self.find_element_by_css("div.post")

        heart = first_el.find_element_by_css("div.heart")

        heart.click()

        first_el_id = heart.get_attribute("data-id")

        self.wait_for_element_to_be_clickable(
            "//span[@class='fvtico']"
        ).click()

        return first_el_id
