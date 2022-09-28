from re import L
import types
import requests
from datetime import date
import json 

url = "https://realty-in-us.p.rapidapi.com/properties/v3/list"

payload = {
	"limit": 1000,
	"offset": 0,
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
print (len(homes))
#iterate through the various homes 

labels = []
statuses = []
longitudes = []
latitudes = []
house_types = []
beds = []
baths = []
full_baths = []
is_price_reduceds = []
is_new_constructions = []
is_foreclosures = []
is_plans = []
is_new_listings = []
is_coming_soons = []
is_contigents = []
is_pendings = []
price_reduced_amounts = []
days_since_last_solds = []
days_since_list_dates = []
last_sold_prices = []
list_prices = []
for home in homes:

    status = (lambda s: 1 if s == "for sale" else 0)(home['status']) # assign status to 1 if its on sale, 2 otherwise
    latitude = home['location']['address']['coordinate']['lat'] # the latitude of the home 
    longitude = home['location']['address']['coordinate']['lon'] # the longitude of the home 
    description = home['description'] # description of the home 
    house_type = description['type'] # what kind of home style the house belongs to. eg. family home 
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
    statuses.append(status)
    longitudes.append(longitude)
    latitudes.append(latitude)
    house_types.append(house_type)
    beds.append(bed)
    baths.append(bath) 
    full_baths.append(full_bath)
    is_price_reduceds.append(is_price_reduced) 
    is_new_constructions.append(is_new_construction)
    is_foreclosures.append(is_foreclosure)
    is_plans.append(is_plan)
    is_new_listings.append(is_new_listing)
    is_coming_soons.append(is_coming_soon)
    is_contigents.append(is_contingent)
    is_pendings.append(is_pending)
    price_reduced_amounts.append(price_reduced_amount)
    days_since_last_solds.append(days_since_last_sold) 
    days_since_list_dates.append(days_since_list_date) 
    last_sold_prices.append(last_sold_price)
    list_prices.append(list_price)
