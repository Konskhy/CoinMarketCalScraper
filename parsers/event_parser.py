from selenium.webdriver.common.by import By
from locators.event_locator import EventLocator



class EventParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'{self.event_date} - {self.coin} - {self.name} '

    @property
    def coin(self):
        locator = EventLocator.COIN
        # return self.parent.find_element(locator).string
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def name(self):
        locator = EventLocator.NAME
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def event_date(self):
        locator = EventLocator.DATE
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def description(self):
        locator = EventLocator.DESC
        return self.parent.find_element(By.CSS_SELECTOR, locator).text
