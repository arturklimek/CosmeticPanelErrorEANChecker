import logging
import pandas as pd
from EAN import EANValidator
from Scraper import RossmannScraper

class EANChecker:
    def __init__(self, excel_loader, csv_writer):
        """
        Initialize the EANChecker with an Excel loader and a CSV writer.

        Args:
            excel_loader (ExcelLoader): Instance to load and validate Excel data.
            csv_writer (CSVWriter): Instance to write results to a CSV file.
        """
        self.logger = logging.getLogger('EANCheckerLogger')
        self.scraper = RossmannScraper()
        self.excel_loader = excel_loader
        self.csv_writer = csv_writer
        self.logger.info("EANChecker initialized")

    def check_codes(self):
        """
        Process the EAN codes from the Excel file to verify availability on Rossmann.pl.

        Returns:
            list: Results of the EAN code checks.
        """
        self.logger.info("Starting to load data from Excel")
        self.excel_loader.load_data()
        self.logger.info("Data loaded successfully, starting validation")
        self.excel_loader.validate_data()
        self.logger.info("Data validation successful")

        results = []
        for index, row in self.excel_loader.data.iterrows():
            ean = row['scanned_id']
            if pd.isna(ean):
                self.logger.debug(f"Row {index} skipped: EAN is NaN")
                continue
            ean = str(ean).strip()
            if not ean:
                self.logger.debug(f"Row {index} skipped: EAN is empty after stripping")
                continue

            validator = EANValidator(ean)
            self.logger.debug(f"Validator initialized for EAN: {ean}, Type: {validator.original_type}")

            errors_count = row['Liczba zdarzeń']
            self.logger.debug(f"Processing EAN: {ean}, Number of errors: {errors_count}")

            original_available = self.scraper.check_product(validator.code)
            original_search_url = self.scraper.base_url + validator.code

            if validator.changed_code:
                changed_code = validator.changed_code
                changed_available = self.scraper.check_product(changed_code)
                changed_search_url = self.scraper.base_url + changed_code
                self.logger.debug(f"Changed EAN: {changed_code}, Availability: {changed_available}")
            else:
                changed_code = ''
                changed_available = ''
                changed_search_url = ''

            self.logger.info(
                f"Code: {ean}, Changed Code: {changed_code}, Original Type: {validator.original_type}, "
                f"Is Numeric: {validator.is_numeric}, Length: {validator.length}, Original Available: {original_available}, "
                f"Changed Available: {changed_available}, Original Search URL: {original_search_url}, "
                f"Changed Search URL: {changed_search_url}, Number of Events: {errors_count}"
            )
            results.append((ean, changed_code, validator.original_type, validator.is_numeric, validator.length,
                            original_available, changed_available, original_search_url, changed_search_url,
                            errors_count))


        self.csv_writer.write_data(results)
        self.logger.info("Results written to CSV file successfully")
        return results
