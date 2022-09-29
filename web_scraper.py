from re import L
import types
import requests
from datetime import date
import json 
import csv
import pandas as pd
url = "https://realty-in-us.p.rapidapi.com/properties/v3/list"
labels = ["status", "longitude", "latitude", "house_type", "beds", "baths", "full_baths", "price_reduced", "new_construction", "foreclosure", "plans", "new_listing", "is_coming_soon", "is_contingent", "is_pending",
"price_reduced_amount", "days_since_last_sold", "days_since_list_date", "last_sold_prices", "list_prices"]
data = []
page = 0
while page < 20:

    payload = {
        "limit": 200,
        "offset": page,
        "postal_code": "94582",
        "status": ["for_sale", "sold", "ready_to_build"],
        "sort": {
            "direction": "desc",
            "field": "list_date"
        }
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "c29b2f48f1msh0572d65324876dfp1d06b3jsnc138972bcbaf",
        "X-RapidAPI-Host": "realty-in-us.p.rapidapi.com"
    }

    homes = json.loads(requests.request("POST", url, json=payload, headers=headers).text)['data']['home_search']['results']

    #iterate through the various homes 

    for home in homes:
        status = (lambda s: 1 if s == "for_sale" else 0)(home['status']) # assign status to 1 if its on sale, 2 otherwise

        latitude = home['location']['address']['coordinate']['lat'] # the latitude of the home 
        longitude = home['location']['address']['coordinate']['lon'] # the longitude of the home 
        description = home['description'] # description of the home 

        #what kind of house is it?
        if description['type'] == "single_family":
            house_type = 1
        if description['type'] == "townhomes":
            house_type = 2
        if description['type'] == "condos":
            house_type = 3
        else:
            house_type == 0
        
        #sqft of house 
        sqft = description["sqft"]

        #sqft of lot 
        if not description["lot_sqft"]:
            lot_sqft = 0
        else:
            lot_sqft = description["lot_sqft"]
    
        bed = description['beds'] # number of beds
        bath = description['baths'] # number of bathrooms
        full_bath = description['baths_full'] # number of full bathrooms
        flags = home['flags'] # key
        is_price_reduced = (lambda s: 0 if s == None else 1)(flags['is_price_reduced']) # whether the price has been reduced (depreciating value)
        is_new_construction = (lambda s: 0 if s == None else 1)(flags['is_new_construction']) # whether the property is newly constructed
        is_foreclosure = (lambda s: 0 if s == None else 1)(flags['is_foreclosure']) # has the property been up for foreclosure 
        is_plan = (lambda s: 0 if s == None else 1)(flags['is_plan']) 
        is_new_listing = (lambda s: 0 if s == None else 1)(flags['is_new_listing']) # is it a new listing 
        is_coming_soon = (lambda s: 0 if s == None else 1)(flags['is_coming_soon']) # is the house yet to be built 
        is_contingent = (lambda s: 0 if s == None else 1)(flags['is_contingent'])
        is_pending = (lambda s: 0 if s == None else 1)(flags['is_pending']) # is the house sale pending 
        if not home['price_reduced_amount']:
            price_reduced_amount = 0 
        else:
            price_reduced_amount = home['price_reduced_amount'] # how much the price is reduced by 
        if not home['last_sold_date']:
            last_sold_date = date.today()
        else:
            last_sold_date = date(int(home['last_sold_date'][0:4]), int(home['last_sold_date'][5:7]), int(home['last_sold_date'][8:10])) # last sold date as a date object
        days_since_last_sold = (date.today() - last_sold_date).days # days since last sold 
        list_date = date(int(home['list_date'][0:4]), int(home['list_date'][5:7]), int(home['list_date'][8:10])) # list date as date object
        days_since_list_date = (lambda x: 0 if status != 1 else (date.today() - list_date).days)(status) # days since list date only if the property is for sale 
        last_sold_price = home['last_sold_price']# the price at which the property was last sold 
        list_price = home['list_price']
        #estimate = home['estimate']['estimate']

        # append all of the home values to lists
        house_data = [status, longitude, latitude, house_type, bed, bath, full_bath, is_price_reduced, is_new_construction, is_foreclosure, is_plan, is_new_listing, is_coming_soon, is_contingent, is_pending, price_reduced_amount, days_since_last_sold, days_since_list_date, last_sold_price, list_price]
        data.append(house_data)
    page += 1


filename = "house_data.csv"
with open(filename, 'w') as csvfile: 
    # writing the data to a csv file 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(labels) 
    csvwriter.writerows(data)
df = pd.read_csv("data.csv")
df.head(10)
