#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
import streamlit as st


# In[2]:


st.set_page_config(
    page_title="VA Eind",
    layout="wide")


# ## Titel

# In[3]:


st.title('Welke factoren kunnen de Airbnb prijs beinvloeden in Amsterdam?')


# In[ ]:


h1, h2, h3, h4, h5, h6 = st.tabs(['Probleemstelling & hypothese','Gebruikte datasets','Locatie & Huisprijs','Reviews','Aantal Personen','Conclusie'])


# ### H1 Probleemstelling & hypothese

# In[4]:


from PIL import Image


# In[5]:


with h1:
    st.header('Probleemstelling & Hypothese')
    st.text('''Dit is een verslag van het onderzoek naar de AIRBNB prijs in Amsterdam. Er wordt gekeken naar
    welke factoren de grootste invloed kunnen hebben op deze prijs. De data die gebruikt is tijdens
    het onderzoek komt van Kaggle en bevat data over de AIRBNB situatie op 6 december 2018.''')
    
    image = Image.open('Airbnb.jpg')
    st.image(image, width=800)

    st.text('''De verwachte uitkomst van het onderzoek is dat de Huisprijs, Reviews en Aantal Personen de
    grootste invloed hebben op de AIRBNB prijs. In de volgende slides zal hier meer over verteld
    worden, maar eerst zullen de datasets verduidelijkt worden.''')


# ### H2 Gebruikte datasets

# In[ ]:


with h2:
    st.header('Gebruikte datasets')
    st.text('')


# ### H3 Locatie + WOZ

# In[ ]:


with h3:
    st.header('Locatie & Huisprijs')
    st.text('')


# ### H4 Reviews

# In[ ]:


with h4:
    st.header('Reviews')
    st.text('')


# ### H5 Aantal Personen

# In[ ]:


with h5:
    st.header('Aantal personen')
    st.text('')


# ### H6 Conclusie

# In[ ]:


with h6:
    st.header('Conclusie')
    st.text('')

