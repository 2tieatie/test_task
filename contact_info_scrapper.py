from selenium import webdriver
from selenium.webdriver.common.by import By
from vars import *
from selenium.common.exceptions import NoSuchElementException


class LIInfoScrapper:

    def __init__(self):
        options: webdriver.EdgeOptions = webdriver.EdgeOptions()
        for option in driver_options:
            options.add_argument(option)
        for key, value in custom_headers.items():
            options.add_argument(f"--header={key}:{value}")
        self.driver: webdriver.Edge = webdriver.Edge(options=options)
        self.DEBUG: bool = True
        self.info: str
        self.name: str
        self.location: str

    def get_info(self, link: str):
        # collecting data from html by xpath
        self.driver.get(link)

        try:
            self.name = self.driver.find_element(By.XPATH, "//h1[@id='pv-contact-info']").text.strip()
        except Exception as ex:
            self.name = None

        try:
            self.location = self.driver.find_element(By.XPATH,
                                                     '//span[@class="text-body-small inline t-black--light break-words"]').text.strip()
        except NoSuchElementException:
            self.location = None

        try:
            info_raw = self.driver.find_element(By.XPATH,
                                                "//div[@class='pv-profile-section__section-info section-info']")
            self.info = info_raw.text.strip().replace(f'{self.name.split()[0]}’s Profile\n', '')
        except NoSuchElementException:
            self.info = None


