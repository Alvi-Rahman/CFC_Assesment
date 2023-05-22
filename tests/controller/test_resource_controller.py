import pytest
from controllers.resource_controller import ResourceScrapeController


class TestResourceScrapeController:
    @pytest.fixture
    def resource_scrape_controller(self):
        """
        Fixture for creating an instance of ResourceScrapeController for testing.
        """
        return ResourceScrapeController()

    def test_scrape_resources(self, resource_scrape_controller):
        """
        Test case for the __scrape_resources method of ResourceScrapeController.

        Tests the behavior of scraping external resources from a webpage and returning a dictionary.

        Args:
            resource_scrape_controller (ResourceScrapeController): Instance of ResourceScrapeController.
        """
        flag, external_resources = resource_scrape_controller._ResourceScrapeController__scrape_resources()
        assert flag is True
        assert isinstance(external_resources, dict)

    def test_write_resources(self, resource_scrape_controller):
        """
        Test case for the __write_resources method of ResourceScrapeController.

        Tests the behavior of writing the scraped external resources to a JSON file and returning a message.

        Args:
            resource_scrape_controller (ResourceScrapeController): Instance of ResourceScrapeController.
        """
        message = resource_scrape_controller._ResourceScrapeController__write_resources()
        assert isinstance(message, str)

    def test_main(self, resource_scrape_controller):
        """
        Test case for the main method of ResourceScrapeController.

        Tests the behavior of the main entry point that orchestrates the scraping and writing process.

        Args:
            resource_scrape_controller (ResourceScrapeController): Instance of ResourceScrapeController.
        """
        message = resource_scrape_controller.main()
        assert isinstance(message, str)
