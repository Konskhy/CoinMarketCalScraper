# from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from locators.event_cal_locator import EventCalLocator
from parsers.event_parser import EventParser


class EventsPage:
    # def __init__(self, page_content):
    #     self.soup = BeautifulSoup(page_content, 'html.parser')
    def __init__(self, browser):
        self.browser = browser

    @property
    def events(self):
        # return [EventParser(e) for e in self.soup.select(EventCalLocator.EVENTS)]
        return [EventParser(e) for e in self.browser.find_elements(By.CSS_SELECTOR, EventCalLocator.EVENTS)]

