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
