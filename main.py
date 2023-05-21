from utilities.beautiful_soup_scrapper import BeautifulSoupContentScrapper
from utilities.writer import FileWriter


class CFCWebScrapper:
    @staticmethod
    def scrape_cfc_index_page():
        bs_scrapper = BeautifulSoupContentScrapper()
        external_resources = bs_scrapper.scrape_index_page()
        file_writer = FileWriter()
        file_name = "output.json"
        file_writer.write_to_json_file(external_resources, file_name)

        word_count = bs_scrapper.privacy_policy_word_frequency_counter()
        file_name = "privacy_policy.json"
        file_writer.write_to_json_file(word_count, file_name)
        return f"Privacy Policy File was written to {file_name}"


if __name__ == "__main__":
    scraper_instance = CFCWebScrapper()
    print(scraper_instance.scrape_cfc_index_page())

