import json
from radikolite_home.models import Radio


def get_radio_stations() -> list:
    with open("data/radio.json", "r") as file:
        data = json.load(file)

    stations = [
      Radio(
        radio_name = d.get("name"),
        radio_logo = d.get("logo"),
        radio_stream = d.get("stream")
      )
      for d in data
    ]
    
    return stations
