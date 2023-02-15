from pymongo import MongoClient
import pandas as pd
from cartoframes.viz import Map, Layer, popup_element
from folium import Choropleth, Circle, Marker, Icon, Map
def palo_alto_address():
    client = MongoClient("localhost:27017")
    db = client["Ironhack"]
    comp = db.get_collection("companies")
    companies_name   = {'name':
                            {"$regex": 
                            '(SurveyMonkey|LivingSocial|Zynga|BrightSource|Better Place|Tesla Motors|SolarCity|Telefonica|Comcast|SunEdison)',
                            "$options" :'i'}}
    companies_city   = {'offices.city':'Palo Alto'}
    companies_city_1 = {'offices.city':'San Francisco'}                

    project_= {'offices.address1':1,'offices.city':1,'_id':0}
    project_1= {'name':1,'offices.address1':1,'offices.city':1,'_id':0}
    address = list(comp.find({ "$and": 
                [companies_name,{'$or':
                                 [companies_city,companies_city_1]}]},project_ ))
    address_lst= []
    for i in address:
        for key, value in i.items():
            for j in value:
                address_lst.append(j)
    df_address= pd.DataFrame(address_lst)
    df_address=df_address.apply(lambda x: x[df_address['city'].isin(['Palo Alto', 'San Francisco'])])
    return df_address

def d_address(address):
    address_lst= []
    for i in address:
        for key, value in i.items():
            for j in value:
                address_lst.append(j)
    df_address= pd.DataFrame(address_lst)
    df_address=df_address.apply(lambda x: x[df_address['city'].isin(['Palo Alto', 'San Francisco'])])
   
    return df_address

def lst_coordinates():
    list_1= [
        {'name':'Tesla','lat':37.3942781,'lon':-122.152006817},
        {'name':'Better Place','lat':37.3942641 ,'lon':-122.14902917 },
        {'name':'SurveyMonkey','lat':37.4451016 ,'lon': -122.162978817},
        {'name':'Zynga', 'lat':37.76476,'lon':-122.406779318}
    ]
    df_coordinates= pd.DataFrame(list_1)
    return df_coordinates

def map_palo_alto():
    palal_lat = 37.4256293
    palal_lon = -122.2053912

    palal_map = Map(location=[palal_lat, palal_lon], zoom_start = 9)
    return palal_map

def map_places(df_coordinates):
    
    palal_lat = 37.4256293
    palal_lon = -122.2053912

    palal_map = Map(location=[palal_lat, palal_lon], zoom_start = 9)
    
    for index, row in df_coordinates.iterrows():
        ubications = {"location": [row["lat"], row["lon"]]}
        if row["name"] == "Tesla":        
            icon = Icon (
                        color="blue",
                        opacity = 0.6,
                        prefix = "fa",
                        icon="briefcase",
                        icon_color = "black"
                        )
        elif row["name"] == "Better Place":
            icon = Icon (
                        color="red",
                        opacity = 0.6,
                        prefix = "fa",
                        icon="briefcase",
                        icon_color = "yellow"
                        )
        elif row["name"] == "SurveyMonkey":
            icon = Icon (
                        color="purple",
                        opacity = 0.6,
                        prefix = "fa",
                        icon="briefcase",
                        icon_color = "white"
                    )
        elif row["name"] == "Zynga":
            icon = Icon (
                        color="white",
                        opacity = 0.6,
                        prefix = "fa",
                        icon="briefcase",
                        icon_color = "black"
                    )

                #3. Marker
        new_marker = Marker(**ubications, icon = icon, radius = 200)

                #4. Add the Marker
        new_marker.add_to(palal_map)
    return palal_map