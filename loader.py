from pymongo import MongoClient
from datetime import datetime
import json
import os

# Writes the database of your search results
def write_db():
    # Writes Searches into the database
    client = MongoClient();
    db = client.search_results;
    path = './Searches/'
    print "Examining JSON from Searches directory"
    for file in os.listdir(path):
        if not file.endswith('.json'):
            continue

        with open(path + file) as data_file:
            data = json.load(data_file)
        event = data["event"]
        for entry in event:
            timestamp = int(entry["query"]["id"][0]["timestamp_usec"])/1000000
            text = entry["query"]["query_text"]
            text = text.replace(u"\ufffd", "'") # Replace garbage character
            result = {
              "text": text,
              "date": datetime.fromtimestamp(timestamp)
            }
            db.results.insert_one(result)
    print "Finished writing database."
