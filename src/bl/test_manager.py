from pages.batik_page import BatikPage
from pages.giraffes_page import GiraffesPage
from pages.home_page import HomePage
from pages.embroidery_page import EmbroideryPage
from pages.jewelry_page import JewelryPage


class TestManager:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.embroidery_page = EmbroideryPage(driver)
        self.batik_page = BatikPage(driver)
        self.giraffes_page = GiraffesPage(driver)
        self.jewelry_page = JewelryPage(driver)

    def search_art_tram_track(self):
        self.home_page.go_to_embroidery()
        return self.embroidery_page.get_art_tram_track()

    def tram_track_style(self):
        self.home_page.go_to_embroidery()
        return self.embroidery_page.art_tram_track_style()

    def batik_first_fav(self):
        self.home_page.go_to_batik()
        return self.batik_page.first_to_fav()

    def word_giraffes_exists(self):
        self.home_page.go_to_giraffes()
        return self.giraffes_page.find_first_art_giraffe()

    def jewelry_basket(self):
        # перед началом теста убедимся что в корзине ничего нет
        self.home_page.clear_basket()
        self.home_page.go_to_jewelry()
        return self.jewelry_page.to_basket()