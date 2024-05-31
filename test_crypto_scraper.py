import unittest
from crypto_scraper import CryptoScraper

class TestCryptoScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = CryptoScraper()

    def test_fetch_data(self):
        data = self.scraper.fetch_data()
        self.assertIsInstance(data, dict)
        self.assertTrue("Biggest Volume Increase" in data)
        self.assertIsInstance(data["Biggest Volume Increase"], list)

    def test_fetch_section(self):
        section_title = "Biggest Volume Increase"
        data = self.scraper.fetch_section(section_title)
        self.assertIsInstance(data, list)
        if data:
            item = data[0]
            self.assertIn("Rank", item)
            self.assertIn("Name", item)
            self.assertIn("Symbol", item)
            self.assertIn("Price", item)
            self.assertIn("Change", item)

    def test_set_proxy(self):
        proxy = "http://your_proxy_here"
        self.scraper.set_proxy(proxy)
        self.assertEqual(self.scraper.proxy, proxy)

if __name__ == "__main__":
    unittest.main()
