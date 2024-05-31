import requests
from bs4 import BeautifulSoup

class CryptoScraper:
    """
    A scraper for fetching cryptocurrency data from BitDegree's top crypto gainers page.
    """

    # Constant URL for the BitDegree top crypto gainers page
    URL = "https://www.bitdegree.org/cryptocurrency-prices/top-crypto-gainers-today"

    def __init__(self):
        """
        Initializes the CryptoScraper with default headers and no proxy.
        """
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.proxy = None

    def set_proxy(self, proxy):
        """
        Sets the proxy for the scraper.

        Args:
            proxy (str): The proxy URL.
        """
        self.proxy = proxy

    def fetch_data(self):
        """
        Fetches all cryptocurrency data from the BitDegree page.

        Returns:
            dict: A dictionary containing data for each section by title.
        """
        # Setting up the proxies if any
        proxies = {
            "http": self.proxy,
            "https": self.proxy,
        } if self.proxy else None

        # Sending a GET request to the page
        response = requests.get(self.URL, headers=self.headers, proxies=proxies)

        # Parsing the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Finding all stats-card sections
        stats_cards = soup.find_all("div", class_="stats-card")

        # Dictionary to hold data for each section by title
        data_by_section = {}

        for card in stats_cards:
            # Finding the title of the section
            title_element = card.find("span", class_="title ml-2")
            if title_element:
                title = title_element.text.strip()

                # Extracting data from each section within the card
                data = []
                sections = card.select("div.section")
                for section in sections:
                    coin_rank_element = section.find("div", class_="coin-rank")
                    coin_rank = coin_rank_element.text.strip() if coin_rank_element else "N/A"

                    coin_name_element = section.find("span", class_="name")
                    coin_name = coin_name_element.text.strip() if coin_name_element else "N/A"

                    coin_symbol_element = section.find("span", class_="coin-item-symbol")
                    coin_symbol = coin_symbol_element.text.strip() if coin_symbol_element else "N/A"

                    coin_price_element = section.find("span", class_="stat")
                    coin_price = coin_price_element.text.strip() if coin_price_element else "N/A"

                    # Check if the coin_change element exists before extracting text
                    coin_change_element_up = section.find("span", class_="stats-value-up")
                    coin_change_element_down = section.find("span", class_="stats-value-down")

                    if coin_change_element_up:
                        coin_change = coin_change_element_up.text.strip()
                    elif coin_change_element_down:
                        coin_change = "-" + coin_change_element_down.text.strip()
                    else:
                        coin_change = "N/A"

                    data.append({
                        "Rank": coin_rank,
                        "Name": coin_name,
                        "Symbol": coin_symbol,
                        "Price": coin_price,
                        "Change": coin_change
                    })

                # Storing the data in the dictionary by title
                data_by_section[title] = data

        return data_by_section

    def fetch_section(self, section_title):
        """
        Fetches data for a specific section by title.

        Args:
            section_title (str): The title of the section to fetch data for.

        Returns:
            list: A list of dictionaries containing data for the specified section.
        """
        # Setting up the proxies if any
        proxies = {
            "http": self.proxy,
            "https": self.proxy,
        } if self.proxy else None

        # Sending a GET request to the page
        response = requests.get(self.URL, headers=self.headers, proxies=proxies)

        # Parsing the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Finding the specific section with the given title
        section_data = []
        card = soup.find("span", class_="title ml-2", string=section_title)
        if card:
            card = card.find_parent("div", class_="stats-card")
            sections = card.select("div.section")
            for section in sections:
                coin_rank_element = section.find("div", class_="coin-rank")
                coin_rank = coin_rank_element.text.strip() if coin_rank_element else "N/A"

                coin_name_element = section.find("span", class_="name")
                coin_name = coin_name_element.text.strip() if coin_name_element else "N/A"

                coin_symbol_element = section.find("span", class_="coin-item-symbol")
                coin_symbol = coin_symbol_element.text.strip() if coin_symbol_element else "N/A"

                coin_price_element = section.find("span", class_="stat")
                coin_price = coin_price_element.text.strip() if coin_price_element else "N/A"

                # Check if the coin_change element exists before extracting text
                coin_change_element_up = section.find("span", class_="stats-value-up")
                coin_change_element_down = section.find("span", class_="stats-value-down")

                if coin_change_element_up:
                    coin_change = coin_change_element_up.text.strip()
                elif coin_change_element_down:
                    coin_change = "-" + coin_change_element_down.text.strip()
                else:
                    coin_change = "N/A"

                section_data.append({
                    "Rank": coin_rank,
                    "Name": coin_name,
                    "Symbol": coin_symbol,
                    "Price": coin_price,
                    "Change": coin_change
                })

        return section_data

