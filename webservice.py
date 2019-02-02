#Import the modules
import requests
import json


# Get the feed
r = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc")
#r.text

print(r)

# Convert it to a Python dictionary
data = json.loads(r.text)

# Loop through the result.
for item in data['data']['items']:

    print ("item['title'])", item['title'])
    print
