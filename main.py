from CSVWriter import CSVWriter
from EANChecker import EANChecker
from FileLoader import ExcelLoader
import logging
from logging.handlers import RotatingFileHandler

file_path = './skaner bledy.xlsx'

def setup_logging():
    """
    Setup global logging configuration.

    Returns:
        logger (logging.Logger): Configured logger instance.
    """
    logger = logging.getLogger('EANCheckerLogger')
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler('ean_checker.log', maxBytes=20000000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

if __name__ == "__main__":
    logger = setup_logging()
    logger.info("Starting EANChecker process")

    try:
        excel_loader = ExcelLoader(file_path)
        logger.info(f"Excel file loader initialized with file path: {file_path}")

        csv_writer = CSVWriter('output_results.csv')
        logger.info("CSVWriter initialized with output file: 'output_results.csv'")

        checker = EANChecker(excel_loader, csv_writer)
        logger.info("EANChecker initialized")

        results = checker.check_codes()
        logger.info("EAN codes checking completed")

        for (code, changed_code, original_type, is_numeric, length,
             original_available, changed_available, original_search_url,
             changed_search_url, errors_count) in results:
            print(
                f"Code: {code}, Changed Code: {changed_code}, Original Type: {original_type}, Is Numeric: {is_numeric}, Length: {length}, Original Available: {original_available}, Changed Available: {changed_available}, Original Search URL: {original_search_url}, Changed Search URL: {changed_search_url}, Number of Errors: {errors_count}")
            logger.info(
                f"Processed code: {code}, Changed code: {changed_code}, Original type: {original_type}, Is numeric: {is_numeric}, Length: {length}, Original available: {original_available}, Changed available: {changed_available}, Original search URL: {original_search_url}, Changed search URL: {changed_search_url}, Number of errors: {errors_count}")

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
