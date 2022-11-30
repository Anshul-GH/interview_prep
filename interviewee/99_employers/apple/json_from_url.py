"""
USGS (US Geological Survey) publishes various earthquake data as JSON feed.
Here's a feed spanning all domestic earthquakes from the past week:
https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson

Using this JSON feed:
1) Identify every earthquake in California
"""

import pandas as pd
import requests
import json

source_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

source_data = requests.get(source_url).text

json_data = json.loads(source_data)

# print(json_data)

# json_data = pd.read_json(path_or_buf=source_url)

features = json_data['features']

record_count = len(list(features))

# print(record_count)

places_collection = []

for record_id in range(record_count):
    places_collection.append(features[record_id]["properties"]["place"])

california_identifier = "CA"

places_california = [place for place in places_collection if california_identifier in place]

print(places_california)
