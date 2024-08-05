# CosmeticPanelErrorEANChecker

## Overview

The CosmeticPanelErrorEANChecker is a Python-based tool designed to read a list of EAN codes (from input file) that were incorrectly scanned on a cosmetic panel and subsequently search for these products on the Rossmann online store. The program validates the codes, checks their availability on the store, and logs the results in a CSV file.

## Features

- **Read Excel File**: Load a list of EAN codes and their associated error counts from an Excel file.
- **Validate EAN Codes**: Validate the EAN codes to identify their type (EAN-13, EAN-8, UPC-A, etc.).
- **Search Products**: Check the availability of these products on the Rossmann online store.
- **Logging**: Log the process and results, including invalid codes and errors encountered during the search.
- **Output Results**: Save the results to a CSV file, including the original and modified EAN codes, their types, and availability status.

## Requirements

- Python 3.x
- pandas
- requests
- beautifulsoup4
- barcodenumber

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/arturklimek/CosmeticPanelErrorEANChecker.git
    cd CosmeticPanelErrorEANChecker
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare your Excel file**: Ensure your Excel file follows the expected format with a header row containing 'scanned_id' and 'Liczba zdarzeń'.

2. **Configure logging**: The program uses a rotating file handler for logging. By default, logs are written to `ean_checker.log`.

3. **Run the program:**
    ```bash
    python main.py
    ```

4. **Check results**: The results will be saved to `output_results.csv`.


## Example

An example of how to use the CosmeticPanelErrorEANChecker:
1. Place your Excel file in the project directory.
2. Run the program and wait for it to process the EAN codes.
3. Open `output_results.csv` to view the results.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [pandas](https://pandas.pydata.org/)
- [requests](https://requests.readthedocs.io/en/latest/)
- [barcodenumber](https://pypi.org/project/barcodenumber/)

