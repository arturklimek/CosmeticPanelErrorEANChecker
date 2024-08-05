import logging
import barcodenumber
import re

class EANValidator:
    def __init__(self, code):
        """
        Initialize the EANValidator with a given code.

        Args:
            code (str): The barcode to be validated and analyzed.
        """
        self.logger = logging.getLogger('EANCheckerLogger')
        self.original_code = code
        self.code = code
        self.is_numeric = self.check_if_numeric()
        self.length = len(self.code)
        self.original_type = self.detect_original_type()
        self.changed_code = self.pad_code_to_ean13() if self.length < 13 and self.is_numeric else ''
        self.changed_type = 'EAN-13' if self.changed_code and self.is_valid_ean13(self.changed_code) else 'Invalid Changed EAN-13'
        self.logger.info(f'Initialized EANValidator with code: {code}')
        self.logger.info(f'Validated code: {self.code}, Original type: {self.original_type}, Changed code: {self.changed_code}, Changed type: {self.changed_type}')

    def check_if_numeric(self):
        """
        Check if the code is numeric.

        Returns:
            bool: True if the code is numeric, False otherwise.
        """
        is_numeric = self.code.isdigit()
        self.logger.debug(f'Code {self.code} is numeric: {is_numeric}')
        return is_numeric

    def pad_code_to_ean13(self):
        """
        Pad the code with zeros to the left to make it EAN-13.

        Returns:
            str: The Changed EAN-13 code.
        """
        changed_code = self.code.zfill(13)
        self.logger.debug(f'Changed code {self.code} to EAN-13: {changed_code}')
        return changed_code

    def detect_original_type(self):
        """
        Detect the original type of the barcode.

        Returns:
            str: The type of the original barcode (e.g., 'EAN-13', 'EAN-8', 'UPC-A', 'Numeric', 'Non-numeric or Unsupported Type').
        """
        if self.is_numeric:
            if self.length == 13:
                if self.is_valid_ean13(self.code):
                    return 'EAN-13'
                else:
                    return 'Invalid EAN-13'
            elif self.length == 8:
                if self.is_valid_ean8(self.code):
                    return 'EAN-8'
                else:
                    return 'Invalid EAN-8'
            elif self.length == 12:
                if self.is_valid_upca(self.code):
                    return 'UPC-A'
                else:
                    return 'Invalid UPC-A'
            else:
                return 'Numeric'
        else:
            return 'Non-numeric or Unsupported Type'

    def is_valid_ean13(self, code):
        """
        Check if the code is a valid EAN-13.

        Args:
            code (str): The code to be checked.

        Returns:
            bool: True if the code is a valid EAN-13, False otherwise.
        """
        is_valid = barcodenumber.check_code('ean13', code)
        self.logger.debug(f'Code {code} is valid EAN-13: {is_valid}')
        return is_valid

    def is_valid_ean8(self, code):
        """
        Check if the code is a valid EAN-8.

        Args:
            code (str): The code to be checked.

        Returns:
            bool: True if the code is a valid EAN-8, False otherwise.
        """
        is_valid = barcodenumber.check_code('ean8', code)
        self.logger.debug(f'Code {code} is valid EAN-8: {is_valid}')
        return is_valid

    def is_valid_upca(self, code):
        """
        Check if the code is a valid UPC-A.

        Args:
            code (str): The code to be checked.

        Returns:
            bool: True if the code is a valid UPC-A, False otherwise.
        """
        is_valid = barcodenumber.check_code('upca', code)
        self.logger.debug(f'Code {code} is valid UPC-A: {is_valid}')
        return is_valid
