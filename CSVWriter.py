import logging
import pandas as pd

class CSVWriter:
    def __init__(self, filename):
        """
        Initialize the CSVWriter with a filename.

        Args:
            filename (str): The name of the file where the data will be saved.
        """
        self.logger = logging.getLogger('EANCheckerLogger')
        self.filename = filename
        self.logger.info(f"CSVWriter initialized with filename: {filename}")

    def write_data(self, data):
        """
        Write extended data to a CSV file including results for original and padded codes.

        Args:
            data (list): List of tuples containing the data to be written to the CSV file.
        """
        self.logger.info("Preparing to write data to CSV file")
        try:
            df = pd.DataFrame(data, columns=['Original EAN', 'Changed EAN', 'Original Type', 'Is Numeric', 'Length',
                                             'Original Availability', 'Changed Availability', 'Original Search URL',
                                             'Changed Search URL', 'Number of Events'])
            self.logger.debug(f'Data to be written to CSV: \n{df}')
            df.to_csv(self.filename, index=False)
            self.logger.info(f"Data successfully saved to {self.filename}")
        except Exception as e:
            self.logger.error(f"Failed to write data to CSV file: {e}")
            raise
