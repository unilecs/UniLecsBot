import requests
from config import *
from models import *
from datetime import datetime
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["X-ACCESS-KEY"] = DATA_ACCESS_KEY

class EventService:
    def __init__(self, data=None, version=None):
        self.data = data
        self.version = version

    def get_event_data(self):
        if self.data is None or self.version != EVENTS_URL_VERSION:
            response = requests.get(EVENTS_URL, headers=headers)
            self.version = EVENTS_URL_VERSION
            self.data = (
                response.json()["record"]
                if response and response.status_code == 200
                else None
            )
        return self.data

    def get_events(self):
        events_from_server = self.get_event_data()["events"]
        event_list = []

        for event in events_from_server:
            event_list.append(
                Event(
                    event.get("id", None),
                    event.get("name", None),
                    event.get("description", None),
                    event.get("date", None),
                    event.get("link", None),
                    event.get("type", None),
                    event.get("location", None),
                    event.get("time", None),
                )
            )
        return event_list

    def get_past_events(self):
        events = self.get_events()
        past_events_list = []

        for event in events:
            event_date = datetime.strptime(event.date, "%d-%m-%Y")
            if datetime.today() > event_date:
                past_events_list.append(event)
        
        return past_events_list

    def get_upcoming_events(self):
        events = self.get_events()
        upcoming_events_list = []

        for event in events:
            event_date = datetime.strptime(event.date, "%d-%m-%Y")
            if datetime.today() <= event_date:
                upcoming_events_list.append(event)
        
        return upcoming_events_list

