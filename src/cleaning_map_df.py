from pymongo import MongoClient
import pandas as pd
import seaborn as sns
import numpy as np
import re
import plotly.express as px
from plotly import graph_objects as go
import matplotlib.pyplot as plt
import requests
import geopandas as gpd
from cartoframes.viz import Map, Layer, popup_element
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import json
import os
from dotenv import load_dotenv

def data_together( df_coordinates, df_zg):
    zg_coord = df_coordinates.drop([0,1,2])
    frames = [zg_coord, df_zg]
    df_all = pd.concat(frames)
    df_all.reset_index(inplace= True)
    df_all.drop(columns=['index'],inplace=True)
    return df_all


def points(df_all):
    sf_lat = 37.7576171
    sf_lon = -122.486017213
    sf_map = Map(location=[sf_lat, sf_lon], zoom_start = 11)
    for index, row in df_all.iterrows():
        
        ubication = {"location": [row["lat"], row["lon"]]}
        if row["name"] == 'Zynga':        
            icon = Icon (
                color="white",
                opacity = 0.6,
                prefix = "fa",
                icon="briefcase",
                icon_color = "black"
            )
        elif row["name"] == 'Starbucks':        
            icon = Icon (
                color="green",
                opacity = 0.6,
                prefix = "fa",
                icon="coffee",
                icon_color = "white"
            )
        elif row["name"] == 'De Haro & Mariposa':        
            icon = Icon (
                color="red",
                opacity = 0.6,
                prefix = "fa",
                icon="bus",
                icon_color = "black"
            )
        elif row["name"] == "San Francisco International Airport (SFO)":        
            icon = Icon (
                color="lightblue",
                opacity = 0.6,
                prefix = "fa",
                icon="plane",
                icon_color = "black"
            )
        elif row["name"] == "City College of San Francisco Mission Campus":        
            icon = Icon (
                color="gray",
                opacity = 0.6,
                prefix = "fa",
                icon="book",
                icon_color = "white"
            )
        elif row["name"] == "Tower Valet Parking":        
            icon = Icon (
                color="white",
                opacity = 0.6,
                prefix = "fa",
                icon="map-marker",
                icon_color = "blue"
            )
        elif row["name"] == "Next Level Burger Potrero Hill":        
            icon = Icon (
                color="beige",
                opacity = 0.6,
                prefix = "fa",
                icon="cutlery",
                icon_color = 'purple'
            )
        elif row["name"] == "Berry Basketball Courts":
            icon = Icon (
                color="blue",
                opacity = 0.6,
                prefix = "fa",
                icon="futbol-o",
                icon_color = "brown",
                icon_size=(14, 14)
            )
        new_marker = Marker(**ubication,icon=icon)
        
        new_marker.add_to(sf_map)
    return sf_map