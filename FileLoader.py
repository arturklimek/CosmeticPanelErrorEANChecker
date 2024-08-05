import logging
import pandas as pd

class ExcelLoader:
    def __init__(self, file_path):
        """
        Initialize the ExcelLoader with a file path.

        Args:
            file_path (str): The path to the Excel file to be loaded.
        """
        self.logger = logging.getLogger('EANCheckerLogger')
        self.file_path = file_path
        self.data = None
        self.logger.info(f"ExcelLoader initialized with file path: {file_path}")

    def load_data(self):
        """
        Load data from the Excel file considering the correct sheet and row.

        Returns:
            pd.DataFrame: The loaded data with whitespace stripped from string columns.
        """
        self.logger.info(f'Loading data from {self.file_path}')
        try:
            excel_data = pd.read_excel(self.file_path, sheet_name=None)
            sheet_name = list(excel_data.keys())[0]
            self.logger.info(f'Found sheet: {sheet_name}')
            temp_data = pd.read_excel(self.file_path, sheet_name=sheet_name, skiprows=7)
            self.data = temp_data.apply(lambda col: col.str.strip() if col.dtypes == object else col)
            self.logger.info('Data loaded and cleaned successfully')
            self.logger.debug(f'Loaded data: \n{self.data}')
        except Exception as e:
            self.logger.error(f'Failed to load data from {self.file_path}: {e}')
            raise
        return self.data

    def validate_data(self):
        """
        Validate the necessary columns in the data.

        Raises:
            ValueError: If required columns are missing from the data.
        """
        self.logger.info('Validating data for required columns')
        required_columns = ['scanned_id', 'Liczba zdarzeń']
        for col in required_columns:
            if col not in self.data.columns:
                self.logger.error(f'Missing required column: {col}')
                raise ValueError(f"Missing required column: {col}")
        self.logger.info('Data validation successful')
