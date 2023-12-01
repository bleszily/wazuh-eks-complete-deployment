#!/var/ossec/framework/python/bin/python3

import requests
import json
from datetime import datetime, timedelta
import os

# disable insecure connection warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# send alert if no cloudflare alerts are present in the last 2 days
host = os.environ.get('INDEXER_URL').replace('\n', '')
port = 9200
auth = (os.environ.get('INDEXER_USERNAME').replace('\n', ''), os.environ.get('INDEXER_PASSWORD').replace('\n', '')) # For testing only. Don't store credentials in code.

alertsource = 'Cloudflare'

headers = {'Accept': 'application/json', 'Content-type': 'application/json'}

query = {}
query['query'] = {}
query['query']['term'] = {}
query['query']['term']['alertsource'] = alertsource

day = datetime.today().strftime("%d")
month = datetime.today().strftime("%m")
year = datetime.today().strftime("%Y")

# count to 3 days back to get last 2 days and current day
days_back = 3

count = 0

for i in range(0, days_back):
    date_aux = datetime.today() - timedelta(days=i)

    day = date_aux.strftime("%d")
    month = date_aux.strftime("%m")
    year = date_aux.strftime("%Y")

    index = 'wazuh-alerts-4.x-' + year + '.' + month + '.' + day
    elastic_url = host + '/' + index + '/_count'

    response = requests.get(elastic_url, data = json.dumps(query), auth=auth, verify=False, headers = headers)

    count = int(json.loads(response.text)['count'])

    if count != 0:
        json_response = "{\"task\":\"cloudflare_daily_alerts_check\", \"result\":\"SUCCESS\"}"
        print(json_response)
        exit()

json_response = "{\"task\":\"cloudflare_daily_alerts_check\", \"result\":\"ERROR\"}"
print(json_response)

exit()