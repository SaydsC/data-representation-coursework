#assignment 3

# Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, 
# and stores it into a file called "cso.json".

#Reference: lecture2  - API's in the wild

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.PxAPIv1/en/31/FI/FIQ02?query=%7B%22query%22:%5B%5D,%22response%22:%7B%22format%22:%22json-stat2%22,%22pivot%22:null,%22codes%22:false%7D%7D"

def getAll():
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll()),file=fp)