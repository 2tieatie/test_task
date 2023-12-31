from selenium import webdriver
from selenium.webdriver.common.by import By
from vars import *
from selenium.common.exceptions import NoSuchElementException


class LIProfilesScrapper:

    def __init__(self):
        options = webdriver.EdgeOptions()
        for option in driver_options:
            options.add_argument(option)
        for key, value in custom_headers.items():
            options.add_argument(f"--header={key}:{value}")
        self.driver = webdriver.Edge(options=options)
        self.DEBUG = False

    def get_links(self, page: int):
        self.driver.get(f'{pattern}&page={page}')
        # collecting data from html by xpath
        try:
            self.driver.find_element(By.XPATH, '//div[@class="search-reusable-search-no-results artdeco-card mb2"]')
            self.elements = None

        except NoSuchElementException:
            self.elements = self.driver.find_elements(By.XPATH,
                                                      '//span[contains(@class, "entity-result__title-text")]/a[@class="app-aware-link "]')
            self.links = self.parse_links()

            if self.DEBUG:
                print(self.links)

    def parse_links(self):
        links = []
        if self.DEBUG:
            print(self.elements)
        # getting href of profile contact info
        for element in self.elements:
            link_raw = element.get_attribute('href')
            print(link_raw)
            # deleting useless part of url
            if link_raw not in wrong_results:
                link = f'{link_raw[:link_raw.find("?"):]}{cont_inf_pattern}'
                links.append(link)

        return links
