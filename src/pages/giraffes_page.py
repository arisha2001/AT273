from pages.base_page import BasePage


class GiraffesPage(BasePage):

    def find_first_art_giraffe(self):
        return self.wait_for_element_to_be_clickable_css(
            "div.post .ssize"
        ).text.split('\n')[1]