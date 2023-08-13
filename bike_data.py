### Source [1] in README
### This file uses manual methods to import Citi Bike data

# Web scraping libraries
import requests
import urllib.request
from bs4 import BeautifulSoup
import lxml

# Downloading, moving and unzipping files
import webbrowser
from time import sleep
import shutil
import os
from zipfile import ZipFile

# DataFrame exploration and manipulation
import pandas as pd
from glob import glob

# PostgreSQL interaction
import psycopg2
from psycopg2 import sql
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import config_file

# Manually download all zip available from Citi Bike:
    # uncomment the code block and run once:
# ---------------------------------------------------------------------------------------------------------------
# url = 'https://s3.amazonaws.com/tripdata/'
# response = requests.get(url)
# print(response)
#
# # build soup object
# soup = BeautifulSoup(response.text, features="xml")
# soup
#
# data_files = soup.find_all('Key')
# # print(data_files)
#
# # Insantiate empty list to hold all webpage schemas for looping:
# zip_files = []
# # Populate list with zip file names
# for file in range(len(data_files)-1):
#     zip_files.append(data_files[file].get_text())
# # Download Jersey City zip files
# for file in zip_files:
#     if 'JC' in file:
#         webbrowser.open_new(url + file)
#         sleep(7)

# ---------------------------------------------------------------------------------------------------------------



# unzip files and save to project folder Resources:
    # source [2]
# ---------------------------------------------------------------------------------------------------------------
# absolute_path = os.path.dirname(__file__)
# relative_path = "Resources"
# full_path = os.path.join(absolute_path, relative_path)
# source = "C:\\Users\\EvanS\\Downloads\\"
# destination = full_path
# print(destination)
#
# # Unzip files and clean up data folder
# for item in os.listdir(source):
#     if item.endswith('.zip'):
#         file_name = source + item
#         zip_ref = ZipFile(file_name)
#         zip_ref.extractall(source)
#         zip_ref.close()
#         os.remove(file_name)
# # Move from Download folder to data folder
# for item in os.listdir(source):
#         shutil.move(source + item, destination)

# ---------------------------------------------------------------------------------------------------------------



# Unify headers in each CSV file and combine into single CSV:
# ---------------------------------------------------------------------------------------------------------------
#
# files = os.listdir('.//Resources/')[1:]
# print(files)
# for csv in files:
#     df = pd.read_csv(f'./Resources/{csv}')
#     df = df.rename(columns=({'Trip Duration':'tripduration',
#                              'Start Time':'starttime',
#                              'Stop Time':'stoptime',
#                              'Start Station ID':'start station id',
#                              'Start Station Name':'start station name',
#                              'Start Station Latitude':'start station latitude',
#                              'Start Station Longitude':'start station longitude',
#                              'End Station ID':'end station id',
#                              'End Station Name':'end station name',
#                              'End Station Latitude':'end station latitude',
#                              'End Station Longitude':'end station longitude',
#                              'Bike ID':'bikeid',
#                              'User Type':'usertype',
#                              'Birth Year':'birth year',
#                              'Gender':'gender'}))
#     df.to_csv(f'./Resources/{csv}', index = None)
#
# jc_files = sorted(glob('./Resources/JC-*******citibike-tripdata.csv'))
# jc_trip_data = pd.concat((pd.read_csv(file) for file in jc_files), ignore_index = True)
# jc_trip_data.to_csv('./Resources/jc_trip_data.csv', index = False)
# for items in jc_files:
#     os.remove(items)

# ---------------------------------------------------------------------------------------------------------------

# Build and populate the postgres database:
# ---------------------------------------------------------------------------------------------------------------

# Connect to PostgreSQL
config = config_file.read_config()
user = config['SQLdb']['username']
password = config['SQLdb']['pwd']
host= config['SQLdb']['hostname']


connection = psycopg2.connect(f"dbname= 'citibike_data' user={user} password='{password}'");
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
# Obtain a DB Cursor
cursor = connection.cursor()
db_name = "citibike_data"

### Don't use this:
#----------------------------------------------------
# # Create DB in PostgreSQL
# create_database = f"CREATE DATABASE {db_name};"
# cursor.execute(create_database);
# print("Database created successfully in PostgreSQL ")
# # Closing PostgreSQL connection
# if(connection):
#     cursor.close()
#     connection.close()
#     print("PostgreSQL connection is closed")
#----------------------------------------------------

# # Build table within the new database:
# try:
#     connection = psycopg2.connect(user= user,
#                                   password=password,
#                                   host=host,
#                                   port='5432',
#                                   database='citibike_data')
#     cursor = connection.cursor()
#
# # Some data types have been amended below to account for all data in the csv (i.e. blank cells)
#     create_table_query = '''CREATE TABLE jersey_city(
#                              trip_duration INT,
#                              start_time TIMESTAMP,
#                              stop_time TIMESTAMP,
#                              start_station_id INT,
#                              start_station_name TEXT,
#                              start_station_latitude FLOAT,
#                              start_station_longitude FLOAT,
#                              end_station_id INT,
#                              end_station_name TEXT,
#                              end_station_latitude FLOAT,
#                              end_station_longitude FLOAT,
#                              bike_id INT,
#                              user_type TEXT,
#                              birth_year TEXT,
#                              gender INT); '''
#
#     cursor.execute(create_table_query)
#     connection.commit()
#     print("Table created successfully in PostgreSQL ")
#
# except (Exception, psycopg2.DatabaseError) as error:
#     print("Error while creating PostgreSQL table:", error)
#
# finally:
# # closing database connection.
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")



# # populate table with data from the single CSV file:
# try:
#     connection = psycopg2.connect(user=user,
#                                   password=password,
#                                   host=host,
#                                   port='5432',
#                                   database='citibike_data')
#     cursor = connection.cursor()
#
#     with open('./Resources/jc_trip_data.csv', 'r') as data:
#         next(data)  # Skip the header row
#         cursor.copy_from(data, 'jersey_city', sep=',')
#
#         connection.commit()
#
#         print("Table updated successfully in PostgreSQL ")
# except (Exception, psycopg2.DatabaseError) as error:
#     print("Error while updating PostgreSQL table:", error)
#
# finally:
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")

# ---------------------------------------------------------------------------------------------------------------

