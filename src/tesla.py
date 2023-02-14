import requests
import pandas as pd
def st_b_zn(token):
    url = "https://api.foursquare.com/v3/places/search?query=starbucks&ll=37.394278,-122.152007&radius=500&limit=5"

    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response_0 = requests.get(url, headers=headers)
    starbucks = response_0.json()
    return starbucks

def bs_st_zn(token):

    url = "https://api.foursquare.com/v3/places/search?ll=37.394278,-122.15200&radius=1000&categories=19043&limit=3"


    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response_1 = requests.get(url, headers=headers)
    bus_stop = response_1.json() #bustop in within 1000m
    return bus_stop

def park(token):
    url = "https://api.foursquare.com/v3/places/search?ll=37.394278,-122.15200&radius=500&categories=19020&limit=1"
    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response_4 = requests.get(url, headers=headers)
    parking = response_4.json()
    return parking

def airport(token):

    url = "https://api.foursquare.com/v3/places/search?ll=37.394278,-122.15200&radius=50000&categories=19040&limit=1"
    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }


    response_2 = requests.get(url, headers=headers)
    airport = response_2.json()#airport in within 50km
    return airport

def schools(token):
    url = "https://api.foursquare.com/v3/places/search?ll=37.394278,-122.15200&radius=5000&categories=12009&limit=5"
    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response_3 = requests.get(url, headers=headers)
    school = response_3.json()#school in within 5000m
    return school

def restaurant(token):
    url = "https://api.foursquare.com/v3/places/search?ll=37.394278,-122.15200&radius=500&categories=13377&limit=1"

    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response_5 = requests.get(url, headers=headers)
    restaurant = response_5.json()#airport in within 500m
    return restaurant

def basketball(token):
    url = "https://api.foursquare.com/v3/places/search?ll=37.394278,-122.15200&radius=10000&categories=18008&limit=1"

    headers = {
        "accept": "application/json",
        "Authorization": (token)
    }

    response_6 = requests.get(url, headers=headers)
    basketball = response_6.json()#airport in within 10km
    return basketball

def def_tl(starbucks,bus_stop,parking,airport,school,restaurant,basketball):
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
    df_tl= list_places_nearby(list_conditions)
    return df_tl

def list_places_nearby(list_conditions):
    try:
        df=pd.DataFrame(list_conditions)
        return df
    except:
        return("This place doesn't meet the criteria")
