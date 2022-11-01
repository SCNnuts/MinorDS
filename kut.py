#!/usr/bin/env python
# coding: utf-8

# # Airbnb Amsterdam - Eindopdracht VA

# ## Import libraries

# In[153]:


import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import math
import geopandas as gpd
import folium
from folium import plugins
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from folium import Choropleth, Marker
from folium.plugins import HeatMap, MarkerCluster, HeatMapWithTime


# ## Woningmarkt data inladen via API 
# https://data.amsterdam.nl/datasets/03G1QUEsOQ2Xkw/woningmarkt-amsterdam/

# In[10]:


#url = 'https://api.data.amsterdam.nl/dcatd/datasets/03G1QUEsOQ2Xkw/purls/5'
#s = requests.get(url).content
#xl = pd.ExcelFile(s)
#xl.sheet_names


# In[12]:


#woz_df = xl.parse('2022_jaarboek_stad')


# In[13]:


#woz_df


# ## Amsterdam airbnb data inladen via Kaggle API
# https://www.kaggle.com/datasets/erikbruin/airbnb-amsterdam

# In[26]:


#!pip install kaggle


# In[27]:


# import kaggle
# from kaggle.api.kaggle_api_extended import KaggleApi


# In[28]:


# api = KaggleApi()
# api.authenticate()

# print("Succesfully connected to the Kaggle API!")


# In[32]:


# api.dataset_download_file("erikbruin/airbnb-amsterdam",
# file_name="calendar.csv")

# api.dataset_download_file("erikbruin/airbnb-amsterdam",
# file_name="listings.csv")

# api.dataset_download_file("erikbruin/airbnb-amsterdam",
# file_name="listings_details.csv")

# api.dataset_download_file("erikbruin/airbnb-amsterdam",
# file_name="neighbourhoods.csv")

# api.dataset_download_file("erikbruin/airbnb-amsterdam",
# file_name="neighbourhoods.geojson")

# api.dataset_download_file("erikbruin/airbnb-amsterdam",
# file_name="reviews.csv")

# api.dataset_download_file("erikbruin/airbnb-amsterdam",
# file_name="reviews_details.csv")


# In[33]:


# #unpack zipped files
# import os, zipfile

# dir_name = os.getcwd()
# extension = '.zip'

# for item in os.listdir(dir_name): # loop through items in dir
#     if item.endswith(extension): # check for ".zip" extension
#         file_name = os.path.abspath(item) # get full path of files
#         zip_ref = zipfile.ZipFile(file_name) # create zipfile object
#         zip_ref.extractall(dir_name) # extract file to dir
#         zip_ref.close() # close file
#         os.remove(file_name) # delete zipped file


# In[35]:


# #make a df from each file
# calendar_df = pd.read_csv('calendar.csv')
listings_df = pd.read_csv('listings.csv')
# listings_details_df = pd.read_csv('listings_details.csv')
# neighbourhoods_df = pd.read_csv('neighbourhoods.csv')
neighbourhoods_geoj = gpd.read_file('neighbourhoods.geojson')
# reviews_df = pd.read_csv('reviews.csv')
# reviews_details_df = pd.read_csv('reviews_details.csv')


# In[37]:


apartments = listings_df[['latitude','longitude','room_type']]


# In[79]:


price = listings_df.groupby('neighbourhood').price.mean()


# In[142]:


#price.head()


# In[87]:


neighbourhoods_geoj.set_index('neighbourhood', inplace=True)


# In[88]:


#neighbourhoods_geoj.head()


# In[100]:


m = folium.Map(location=[52.37,4.89], tiles='cartodbpositron', zoom_start=12)

fgp1 = folium.FeatureGroup(name='Heatmap').add_to(m)
HeatMap(data=apartments[['latitude', 'longitude']], radius=15, min_opacity=0.3).add_to(fgp1)

fgp2 = folium.FeatureGroup(name='Prijs per buurt', show=False).add_to(m)
folium.Choropleth(geo_data = neighbourhoods_geoj['geometry'].__geo_interface__, 
           data=price, 
           key_on="feature.id", 
           fill_color='BrBG', 
           legend_name='Average Price'
          ).geojson.add_to(fgp2)

m.add_child(fgp1)
m.add_child(folium.LayerControl())
#m


# In[104]:


m_1 = folium.Map(location=[52.37,4.89], tiles='cartodbpositron', zoom_start=12)

HeatMap(data=apartments[['latitude', 'longitude']], radius=15, min_opacity=0.3).add_to(m_1)

#m_1


# In[154]:


m2 = folium.Map(location=[52.37,4.89], tiles='cartodbpositron', zoom_start=11)

Choropleth(geo_data = neighbourhoods_geoj['geometry'], 
           data=price, 
           key_on="feature.id", 
           fill_color='BrBG', 
           legend_name='Gemiddelde prijs (€)'
          ).add_to(m2)
#m2


# In[114]:


listings_df.head()


# In[113]:


m_3 = folium.Map(location=[52.37,4.89], tiles='cartodbpositron', zoom_start=12)

locations = list(zip(listings_df.latitude, listings_df.longitude))
cluster = plugins.MarkerCluster(locations=locations,                     
               popups=listings_df["name"].tolist())  
m_3.add_child(cluster)

#m_3


# In[117]:


m_4 = folium.Map(location=[52.37,4.89], tiles='cartodbpositron', zoom_start=12)

mc = MarkerCluster()
for idx, row in listings_df.iterrows():
    if not math.isnan(row['longitude']) and not math.isnan(row['latitude']):
        mc.add_child(Marker([row['latitude'], row['longitude']]))
m_4.add_child(mc)

#m_4


# In[124]:


#sns.histplot(data=listings_df, x='price')


# In[122]:


#sns.boxplot(data=listings_df, x='price')


# In[155]:


fig = px.histogram(listings_df, x='price', labels={'count': 'aantal', 'price': 'Prijs (€)'}, title='Verdeling van Airbnb prijzen in Amsterdam')
fig.update_xaxes(rangeslider_visible=True)
#fig.show()
st.write(fig)

# In[138]:


#listings_df['neighbourhood'].value_counts()


# ## Streamlit

# In[139]:


#!pip install streamlit


# In[140]:




# In[156]:


st.title('Airbnb')

