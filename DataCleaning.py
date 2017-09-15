# import libaray
import pandas as pd
import numpy as np
import os
import datetime
import timeit

# load datasets
df_airquality = pd.DataFrame.from_csv('airquality.csv')
df_meteorology = pd.DataFrame.from_csv('meteorology.csv')
df_weatherforecast = pd.DataFrame.from_csv('weatherforecast.csv')

df_station = pd.DataFrame.from_csv('station.csv')
df_district = pd.DataFrame.from_csv('district.csv')
df_city = pd.DataFrame.from_csv('city.csv')

# data cleaning
# location df merge (station < district < city < cluster)
df_station_use=df_station[['latitude','longitude','district_id']]
df_station_use=df_station_use.reset_index()
df_station_use.columns=['station_id','lat_s','lon_s','district_id']

df_district_use=df_district[['city_id']]
df_district_use=df_district_use.reset_index()
df_district_use.columns=['district_id','city_id']

df_city_use=df_city[['latitude','longitude','cluster_id']]
df_city_use=df_city_use.reset_index()
df_city_use.columns=['city_id','lat_c','lon_c','cluster_id']

df_location=pd.merge(df_station_use, df_district_use, on='district_id', how='left')
df_location=pd.merge(df_location,df_city_use,on='city_id',how='left')

# air quality
df_aq_use=df_airquality.reset_index()
df_aq_use.columns=['station_id','time','pm25','pm10','no2','co','o3','so2']

# meteorology df
df_m_use = df_meteorology.reset_index()
df_m_use.columns=['district_id','time','weather','temp','p','rh','ws','wd']

# + weather forecast df
df_wf_use=df_weatherforecast.reset_index()
df_wf_use.columns=['city_id','t_fc','time','freq','weather','up_temp','bottom_temp','w_level','wd']
df_wf_use=df_wf_use[['city_id','time','weather','up_temp','bottom_temp','w_level','wd']]

# MERGE final dataset
# AQ + location
df_final=pd.merge(df_aq_use, df_location, on='station_id', how='left')
# + Meteorology data
df_final=pd.merge(df_m_use,df_final, on=['district_id','time'], how='outer')
# + weather forecast data
df_final=pd.merge(df_wf_use,df_final, on=['city_id','time'], how='outer')

# save csv file
df_final.to_csv('final_df.csv')
