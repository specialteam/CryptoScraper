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
