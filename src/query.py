import pandas as pd
import numpy as np
import plotly.express as px
from plotly import graph_objects as go
import matplotlib.pyplot as plt

def regex():
    companies_name = {'name':
                            {"$regex": 
                            '^(|ux|ui|frontend|backend|gaming|game|gamer|web|software)',
                            "$options" :'i'}}
    companies_cat = {'category_code':
                            {"$regex": 
                            '(network|ux|ui|frontend|backend|gaming|games|game|social|gamer|web|develop|software)',
                            "$options" :'i'}}
    companies_tag = {'tag_list':
                            {"$regex": 
                            '(network|design|ux|ui|frontend|backend|gaming|game|gamer|social|web|software)',
                            "$options" :'i'}}
    companies_desc = {'description':
                             {"$regex": 
                            '(network|ux|ui|frontend|backend|gaming|games|game|social|gamer|web|develop|software)',
                            "$options" :'i'}}
    companies_overview ={'overview':
                            {"$regex": 
                            '(network|ux|ui|frontend|backend|gaming|games|game|social|gamer|web|develop|software)',
                            "$options" :'i'}}
    filter_ = {
            "$or": [companies_name, companies_cat, companies_tag, companies_desc, companies_overview]
            }    
    return filter_

def project_():
    projection = {'name': 1,
                  'offices.city':1,
                  'offices.state_code':1,
                  'offices.country_code':1,
                  'offices.latitude':1, 
                  'offices.longitude':1,
                  'total_money_raised':1,              
                  '_id': 0}
    return projection

def figure_city(filt_list):
    city=[i['offices'] for i in filt_list]
    list_cities=[j for i in city for j in i]
    df= pd.DataFrame(list_cities)
    df['count'] = df.groupby('city')['city'].transform('count')
    df.sort_values(by=['count'], ascending = False, inplace= True)
    df.drop_duplicates(subset = ['city'], inplace = True)
    df.rename(columns={"country_code": "country"},inplace = True)
    df.reset_index(inplace= True)
    df.drop('index',axis =1, inplace =True)
    df.dropna(subset=['city'], inplace = True)
    df.drop(2, inplace=True)
    df.reset_index(inplace= True)
    df.drop('index',axis =1, inplace =True)
    df_top10_city = df.iloc[:10] 
    return df_top10_city


def fig_city(df_top10_city):
    fig_city = px.bar(df_top10_city, x="city", y="count", color='country',
             height=400,
             title='Cities with more companies which meets our criteria')
    return fig_city.show()

def company_df(filt_list):
    name_company = [i ['name']for i in filt_list]
    raised_company=[i ['total_money_raised']for i in filt_list]
    dict_name= {'name':name_company, 'amount': raised_company}
    df_name= pd.DataFrame (dict_name)
    df_name['amount'] = df_name['amount'].apply(lambda x : x.replace('M',''))
    df_name[['currency', 'amount']] = df_name['amount'].str.extract(r'(\D*)(\d.*)')
    df_name.currency.unique()
    df_name = df_name.astype({'amount': 'float'})
    df_name['us$_value_per_M'] = np.where(df_name['currency'] == '€',df_name['amount'] * 1.06864,
                                    (np.where(df_name['currency'] == 'C$',
                                            df_name['amount'] * 0.748393,
                                    (np.where(df_name['currency'] == '£', 
                                            df_name['amount'] * 1.20603, 
                                    (np.where(df_name['currency'] == '¥',
                                            df_name['amount'] * 0.00761048,
                                    (np.where(df_name['currency'] == 'kr',
                                            df_name['amount'] * 0.095483485,
                                    (np.where(df_name['currency'] == '$',
                                            df_name['amount'], df_name['amount'] * 1,
                                            )))))))))))
    df_name = df_name.sort_values( by= 'us$_value_per_M', ascending= False).reset_index()
    df_name.drop(labels = 'index', axis= 1, inplace =True)
    return df_name

def fig_raised(df_name):
    fig_raised = px.scatter_3d(df_name, x='name', y='currency', z='us$_value_per_M',color='currency',title= 'Companies and money raised',
                    symbol='currency',size='amount')
    return fig_raised.show()

def count_df(df_name):
    df_count = df_name.groupby(by= ['currency']).agg({'name':'count'})
    df_count['currency'] = df_count.index
    df_count = df_count.rename(columns = {'name':'no_companies'})
    df_count.sort_values(by=['no_companies'], ascending = False, inplace=True)
    df_count.reset_index(drop=True, inplace =True)    
    return df_count


def co_curr(df_count):
    fig_no_companies = go.Figure(go.Funnel(
    y = df_count['currency'],
    x = df_count['no_companies'],
    textposition = "inside",
    textinfo = "value+percent total",
    opacity = 0.65, marker = {"color": ["deepskyblue", "lightsalmon", "tan", "teal", "silver"],
    "line": {"width": [4, 2, 2, 3, 1, 1], "color": ["wheat", "wheat", "blue", "wheat", "wheat"]}},
    connector = {"line": {"color": "royalblue", "dash": "dot", "width": 3}})
    )
    return fig_no_companies.show()

def top_ten(df_name):
    df_name= df_name[:10]
    fig_companies = px.bar(df_name, x="name", y="us$_value_per_M", color='amount',
             height=400,
             title='Top ten companies incomes')
    return fig_companies.show()

def location():
    companies_location = {'name':
                            {"$regex": 
                        '^(SurveyMonkey|LivingSocial|Zynga|BrightSource|Better Place|Tesla Motors|SolarCity|Telefonica|Comcast|SunEdison)',
                        "$options" :'i'}}
    return companies_location

def city_list(flt):
    city_lst= [j for i in flt for key, value in i.items() for j in value]
    df_cc= pd.DataFrame(city_lst)
    return  df_cc

def top_ten_fig(df_cc):
    fig_=df_cc["city"].value_counts().plot(kind="bar", title="Top ten companies' location")
    plt.xticks(rotation=90);
    return fig_