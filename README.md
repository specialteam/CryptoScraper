
# CryptoScraper

CryptoScraper is a Python script for fetching cryptocurrency data from BitDegree's top crypto gainers page. It can retrieve data for all sections or a specific section based on the title.

## Features

- Fetch all cryptocurrency data from BitDegree.
- Fetch data for a specific section by title.
- Support for setting a proxy.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/specialteam/CryptoScraper.git
   cd cryptoscraper
   ```

2. Install the required packages:

   ```sh
   pip install requests beautifulsoup4
   ```

## Usage

### Fetch All Data

You can fetch all cryptocurrency data with the following script:

```python
from crypto_scraper import CryptoScraper

# Create an instance of the scraper
scraper = CryptoScraper()

# Fetch all data
all_data = scraper.fetch_data()
for title, data in all_data.items():
    print(f"Section: {title}")
    for item in data:
        print(item)
    print("\n" + "-"*50 + "\n")
```

### Fetch Specific Section

To fetch data for a specific section by title:

```python
from crypto_scraper import CryptoScraper

# Create an instance of the scraper
scraper = CryptoScraper()

# Fetch a specific section
section_title = "Biggest Volume Increase"
section_data = scraper.fetch_section(section_title)
print(f"Section: {section_title}")
for item in section_data:
    print(item)
print("\n" + "-"*50 + "\n")
```

### Set Proxy

If you need to use a proxy, you can set it before fetching data:

```python
from crypto_scraper import CryptoScraper

# Create an instance of the scraper
scraper = CryptoScraper()

# Set proxy
scraper.set_proxy("http://your_proxy_here")

# Fetch all data
all_data = scraper.fetch_data()
for title, data in all_data.items():
    print(f"Section: {title}")
    for item in data:
        print(item)
    print("\n" + "-"*50 + "\n")
```

## Running Tests

You can run the provided tests using `unittest`:

```sh
python -m unittest discover
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or comments, please reach out to https://t.me/amirspecial
