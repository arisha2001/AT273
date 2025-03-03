from pages.home_page import HomePage
from pages.embroidery_page import EmbroideryPage


class TestManager:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.embroidery_page = EmbroideryPage(driver)

    def search_artwork(self):
        self.home_page.go_to_embroidery()
        return self.embroidery_page.get_art_tram_track()

    def artwork_style(self):
        self.home_page.go_to_embroidery()
        return self.embroidery_page.art_tram_track_style()