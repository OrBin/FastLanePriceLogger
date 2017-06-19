#!/usr/bin/python3

import requests
import re
import time
import sys
from pymongo import MongoClient

website_response = requests.get("https://www.fastlane.co.il/Mobile.aspx/")

if website_response.status_code != requests.codes.ok:
    # TODO log
    sys.exit(1)

price = re.search('<span id="lblPrice" class="whiteBold">(\d+)<\/span>', website_response.text).group(1)
timestamp = time.time()

client = MongoClient()
db = client.fast_lane_logs

result = db.pricelogs.insert_one({
        "timestamp_sec": timestamp,
        "price": price
    })
