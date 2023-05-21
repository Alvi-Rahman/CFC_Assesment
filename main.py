from utilities.beautiful_soup_scrapper import BeautifulSoupContentScrapper
from utilities.writer import FileWriter


class CFCWebScrapper:
    def scrape_cfc_index_page(self):
        bs_scrapper = BeautifulSoupContentScrapper()
        external_resources = bs_scrapper.scrape_index_page()
        file_writer = FileWriter()
        file_name = "output.json"
        file_writer.write_to_json_file(external_resources, file_name)
        return f"File was written to {file_name}"


if __name__ == "__main__":
    scraper_instance = CFCWebScrapper()
    print(scraper_instance.scrape_cfc_index_page())

