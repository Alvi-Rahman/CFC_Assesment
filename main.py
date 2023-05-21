from utilities.beautiful_soup_scrapper import BeautifulSoupContentScrapper


class CFCWebScrapper:
    def scrape_cfc_index_page(self):
        bs_scrapper = BeautifulSoupContentScrapper()
        external_resources = bs_scrapper.scrape_index_page()
        return external_resources


if __name__ == "__main__":
    scraper_instance = CFCWebScrapper()
    print(scraper_instance.scrape_cfc_index_page())

