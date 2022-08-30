# import requests
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from pages.events_page import EventsPage


SOURCE = 'https://coinmarketcal.com'
edgeService = Service('C:/Program Files/msedgedriver.exe', verbose=True)
edge = webdriver.Edge(service=edgeService)
edge.get(SOURCE)


# page_content = requests.get(SOURCE)
# print(page_content.status_code)

page = EventsPage(edge)

events = page.events

for ev in events:
    print(ev)

time.sleep(5)
edge.quit()
