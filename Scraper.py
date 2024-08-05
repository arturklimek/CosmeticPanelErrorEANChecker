import logging
import requests
from bs4 import BeautifulSoup

class RossmannScraper:
    def __init__(self):
        """
        Initialize the RossmannScraper with base URL and headers for web scraping.
        """
        self.logger = logging.getLogger('EANCheckerLogger')
        self.base_url = "https://www.rossmann.pl/szukaj?Search="
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        self.logger.info("RossmannScraper initialized")

    def check_product(self, ean):
        """
        Check if a product with the given EAN is available on Rossmann.pl.

        Args:
            ean (str): The EAN code of the product to be checked.

        Returns:
            bool: True if the product is found, False otherwise.
        """
        search_url = f"{self.base_url}{ean}"
        self.logger.info(f'Checking product for EAN: {ean} with URL: {search_url}')
        try:
            response = requests.get(search_url, headers=self.headers)
            self.logger.debug(f'HTTP GET request sent to URL: {search_url}')
            if response.status_code == 200:
                self.logger.info(f'Successful response received for EAN: {ean}')
                soup = BeautifulSoup(response.text, 'html.parser')
                toast_div = soup.find('div', class_='Toastify')
                if toast_div:
                    self.logger.debug(f'Toastify div found for EAN: {ean}')
                    result_div = toast_div.find_next_sibling('div')
                    if result_div:
                        header = result_div.find('h1')
                        if header:
                            header_text = header.get_text()
                            if 'Brak wyników dla:' in header_text:
                                self.logger.info(f'Product not found for EAN: {ean}')
                                return False
                            elif 'Wyniki wyszukiwania:' in header_text:
                                self.logger.info(f'Product found for EAN: {ean}')
                                return True
            else:
                self.logger.warning(
                    f'Failed to retrieve product info for EAN: {ean}, status code: {response.status_code}')
        except Exception as e:
            self.logger.error(f'Error occurred while checking product for EAN: {ean}: {e}', exc_info=True)
        return False
