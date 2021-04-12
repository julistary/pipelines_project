### Importing libraries, functions and CSV

import pandas as pd
import requests
from pandas import json_normalize
import os
from dotenv import load_dotenv
import time
import re
from bs4 import BeautifulSoup
import src.functions as f
import src.downloading_and_cleaning as d
import src.api as api
import src.enriching_and_cleaning as e
import src.scrapping as s
import src.visualization as v
load_dotenv()

if (load_dotenv()):
    os.system('say -v Samantha dotenv works!')

d.download_dataset()

df = pd.read_csv("data/dataset.csv")

df.head(3)

### Preliminary cleaning

df = d.preliminary_cleaning(df)

df_url = df['Series_Titles_URL']

df_url.head(3)

### Calling the API

#dict_ = api.calling_api(df_url)

#df_pruebas = pd.DataFrame.from_dict(dict_)

#df_pruebas.to_csv("pruebas.csv")

df_pruebas = pd.read_csv("pruebas.csv")

dict_2 = df_pruebas.to_dict()

### Enriching the dataframe with data taken from de API

#### We are only keeping the 100 first films

df_short = df.head(100)

df_short_clean = e.enriching(df, df_short, dict_2)

df_short_clean = e.more_cleaning(df_short_clean)

df_short_clean.head(4)

df_short_clean.to_csv("data/df_short_clean.csv")

os.system('say -v Samantha exporting first dataframe')

### Scrapping

filmaffinity = s.scrapping()

filmaffinity.head()

IMDB = s.cleaning(df_short_clean)

IMDB.head()

df_IMDB_FA = s.joining(IMDB,filmaffinity)

df_IMDB_FA.head()

### Intersection

df_intersection = s.intersection(df_IMDB_FA, IMDB, filmaffinity)

df_intersection

#### Exporting dataframes

df_IMDB_FA.to_csv("data/df_IMDB_FA.csv")

os.system('say -v Samantha exporting second dataframe')

df_intersection.to_csv("data/IMDB_FA_reduced.csv")

os.system('say -v Samantha exporting last dataframe')

v.visualization()







