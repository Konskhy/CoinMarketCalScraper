from locators.event_locator import EventLocator


class EventParser:
    def __init__(self, parent):
        self.parent = parent

    @property
    def coin(self):
        locator = EventLocator.COIN
        return self.parent.select_one(locator).string

    @property
    def name(self):
        locator = EventLocator.NAME
        return self.parent.select_one(locator).string

    @property
    def event_date(self):
        locator = EventLocator.DATE
        return self.parent.select_one(locator).string

    @property
    def description(self):
        locator = EventLocator.DESC
        return self.parent.select_one(locator).string
