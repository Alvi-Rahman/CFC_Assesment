"""
CFC Web Scraper

This module contains the CFCWebScrapper class that serves as the entry point for the web scraping process.

Classes:
- CFCWebScrapper

"""

from controllers.resource_controller import ResourceScrapeController
from controllers.privacy_policy_controller import PrivacyPolicyWordCountController


class CFCWebScrapper:
    """
    CFCWebScrapper serves as the entry point for the web scraping process.

    Methods:
        resource_scraper_entry_point():
            Executes the resource scraping process.
        privacy_policy_word_counter_entry_point():
            Executes the privacy policy word counting process.

    """

    @staticmethod
    def resource_scraper_entry_point():
        """
        Executes the resource scraping process.

        Returns:
            str: A message indicating the success of the resource scraping process.

        """
        resource_scraper = ResourceScrapeController()
        return resource_scraper.main()

    @staticmethod
    def privacy_policy_word_counter_entry_point():
        """
        Executes the privacy policy word counting process.

        Returns:
            str: A message indicating the success of the privacy policy word counting process.

        """
        privacy_policy_word_counter = PrivacyPolicyWordCountController()
        return privacy_policy_word_counter.main()


if __name__ == "__main__":
    """
    Entry point of the CFC Web Scraper.

    Create an instance of CFCWebScrapper and execute the resource scraper and privacy policy word counter.
    Print the results of both processes.

    """
    scraper_instance = CFCWebScrapper()
    print(scraper_instance.resource_scraper_entry_point())
    print(scraper_instance.privacy_policy_word_counter_entry_point())
