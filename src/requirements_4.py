import requests
import pandas as pd
def st_b_zn(lat,lon,token):
    url = f"https://api.foursquare.com/v3/places/search?query=starbucks&ll={lat},{lon}&radius=500&limit=1"

    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response_0 = requests.get(url, headers=headers)
    starbucks = response_0.json()
    return starbucks

def bs_st_zn(lat,lon,token):

    url = f"https://api.foursquare.com/v3/places/search?ll={lat},{lon}&radius=1000&categories=19043&limit=3"

    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response_1 = requests.get(url, headers=headers)
    bus_stop = response_1.json() 
    return bus_stop

def park(lat,lon,token):
    url = f"https://api.foursquare.com/v3/places/search?ll={lat},{lon}&radius=500&categories=19020&limit=1"

    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response_4 = requests.get(url, headers=headers)
    parking = response_4.json()
    return parking

def airport(lat,lon,token):

    url = f"https://api.foursquare.com/v3/places/search?ll={lat},{lon}&radius=50000&categories=19040&limit=1"

    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }


    response_2 = requests.get(url, headers=headers)
    airport = response_2.json()
    return airport

def schools(lat,lon,token):
    url = f"https://api.foursquare.com/v3/places/search?ll={lat},{lon}&radius=5000&categories=12057&limit=5"

    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response_3 = requests.get(url, headers=headers)
    school = response_3.json()
    return school

def restaurant(lat,lon,token):
    url = f"https://api.foursquare.com/v3/places/search?ll={lat},{lon}&radius=500&categories=13377&limit=1"

    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response_5 = requests.get(url, headers=headers)
    restaurant = response_5.json()
    return restaurant

def basketball(lat,lon,token):
    url = f"https://api.foursquare.com/v3/places/search?ll={lat},{lon}&radius=10000&categories=18008&limit=1"

    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response_6 = requests.get(url, headers=headers)
    basketball = response_6.json()
    return basketball

def def_zn(starbucks,bus_stop,parking,airport,school,restaurant,basketball):
    
    def dict_(json_response):
        try:
            proc_dict={
            'name':json_response['results'][0]['name'],
            'lat': json_response['results'][0]['geocodes']['main']['latitude'],
            'lon': json_response['results'][0]['geocodes']['main']['longitude'],
            'distance (m)': json_response['results'][0]['distance']
            }
            return proc_dict
        except:
            return f'This place is not in within our criteria'
    star_b = dict_(starbucks)
    b_stop = dict_(bus_stop)
    air_p  = dict_(airport)
    schl   = dict_(school)
    prk    = dict_(parking)
    rst    = dict_(restaurant)
    bsk    = dict_(basketball)
    list_conditions= [star_b, b_stop,air_p,schl,prk,rst,bsk]
    def_zn= list_places_nearby(list_conditions)
    return def_zn

def list_places_nearby(list_conditions):
    try:
        df=pd.DataFrame(list_conditions)
        return df
    except:
        return("This place doesn't meet the criteria")
