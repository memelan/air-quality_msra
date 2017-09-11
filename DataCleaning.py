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
# air quality + station df
final_df = df_airquality.join(df_station[['latitude','longitude','district_id']])
final_df = final_df.reset_index()
final_df.columns=['station_id','time','pm25','pm10','no2','co','o3','so2','lat','lon','district_id']

# + district df
df_district_use=df_district[['city_id']]
df_district_use=df_district_use.reset_index()
df_district_use.columns=['district_id','city_id']
final_df=pd.merge(final_df,df_district_use,on='district_id',how='left')

# + city df
df_city['lat_city']= df_city['latitude']
df_city['lon_city']= df_city['longitude']
df_city_use = df_city[['cluster_id','lat_city','lon_city']]
df_city_use = df_city_use.reset_index()
df_city_use.columns = ['city_id','cluster_id','lat_city','lon_city']
final_df = pd.merge(final_df, df_city_use, on='city_id', how='left')
