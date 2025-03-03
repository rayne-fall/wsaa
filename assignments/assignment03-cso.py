# assignment 3 - CSO
# author: Sylvia Chapman Kent
# retrieves the exchequer account (historical series) dataset from the CSO and saves it to a json file

import requests
import json

# identify dataset
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
# retrieve data
response = requests.get(url) 

# save data to json file [1]
with open("cso.json", "w") as outfile:
    json.dump(response.text, outfile)

# 1. https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/ 