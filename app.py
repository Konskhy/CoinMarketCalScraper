import requests
from pages.events_page import EventsPage
SOURCE = 'https://coinmarketcal.com'

page_content = requests.get(SOURCE)
print(page_content.status_code)
page = EventsPage(page_content)
events = page.events

for ev in events:
    print(ev.coin)
