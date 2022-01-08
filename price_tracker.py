
from aadi_config import(
    get_web_driver_options,
    get_chrome_web_driver,
    set_ignore_certificate_error,
    set_browser_as_incognito,
    NAME,
    CURRENCY,
    FILTERS,
    BASE_URL,
    DIRECTORY
    )
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class GenerateReport:
    def __init__(self):
        pass

class AadiAPI:
    def __init__(self, search_term, filters, base_url, currency):
            self.base_url = base_url
            self.search_term = search_term
            options = get_web_driver_options()
            set_ignore_certificate_error(options)
            set_browser_as_incognito(options)
            self.driver = get_chrome_web_driver(options)
            self.currency = currency
            self.price_filter = f"&price_0={filters['min']}&price_1={filters['max']}"

    def run(self):
        print("Starting script...")
        print(f"Looking for {self.search_term} products...")
        links = self.get_products_links()
        time.sleep(3)
        self.driver.quit()

    def get_products_links(self):
        self.driver.get(self.base_url)
        element = self.driver.find_element(By.XPATH, '//*[@id="search-form-close-btn"]')
        element.send_keys(self.search_term)
        element.send_keys(Keys.SEARCH)
        time.sleep(2)


if __name__ == '__main__':
    print("HEYYY!!!")
    aadi = AadiAPI(NAME, FILTERS, BASE_URL, CURRENCY)
    aadi.run()
