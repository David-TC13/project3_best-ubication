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