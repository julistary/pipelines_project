# 👩🏼‍💻 MAIN 👩🏼‍💻 

### Importing libraries and functions 

import pandas as pd
import requests
import numpy as np
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
load_dotenv()

if (load_dotenv()):
    os.system('say -v Samantha dotenv works!')

### Downloading and opening dataset

d.download_dataset()

df = pd.read_csv("data/dataset.csv")


### Preliminary cleaning

df = d.preliminary_cleaning(df)

df_url = df['Series_Titles_URL']


### Calling the API

dict_ = api.calling_api(df_url)

### Enriching the dataframe with data taken from de API

#### We are only keeping the 100 first films

df_short = df.head(100)

df_short_clean = e.enriching(df, df_short, dict_)

df_short_clean = e.more_cleaning(df_short_clean)

### Exporting dataframe

df_short_clean.to_csv("data/df_short_clean.csv")

os.system('say -v Samantha Exporting first dataframe')

### Scraping the best movies from filmaffinity.com and creating a dataframe

filmaffinity = s.scrapping()

filmaffinity.head()

IMDB = s.cleaning(df_short_clean)


### Joining filmaffinity's dataframe and IMDB's dataframe

df_IMDB_FA = s.joining(IMDB,filmaffinity)


### Creating a new dataframe with the intersection

df_intersection = s.intersection(df_IMDB_FA, IMDB, filmaffinity)


### Exporting dataframes

df_IMDB_FA.to_csv("data/df_IMDB_FA.csv")

os.system('say -v Samantha exporting second dataframe')

df_intersection.to_csv("data/IMDB_FA_reduced.csv")

os.system('say -v Samantha exporting last dataframe')



