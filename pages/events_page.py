from bs4 import BeautifulSoup

from locators.event_cal_locator import EventCalLocator
from parsers.event_parser import EventParser


class EventsPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def events(self):
        return [EventParser(e) for e in self.soup.select(EventCalLocator.EVENTS)]
