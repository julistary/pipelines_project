import requests
from bs4 import BeautifulSoup
import re
import os
import src.functions as f
import pandas as pd

def scrapping():
    """
    Creates a dataframe with information scrapped from filmaffinity web.
    Returns:
        The new dataframe
    """

    # Scrapping
    os.system('say -v Samantha scrapping from filmaffinity.com')

    url = "https://www.filmaffinity.com/us/topgen.php?genre=&fromyear=&toyear=&country=&nodoc&notvse"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")

    titles = soup.find_all("div", {"class": "mc-title"})

    list_of_titles = [film.getText().strip() for film in titles]

    director = soup.find_all("div", {"class": "mc-director"})

    list_of_directors = [dir_.getText().strip() for dir_ in director]

    rating = soup.find_all("div", {"class": "avg-rating"})

    list_of_rating = [rate.getText().strip() for rate in rating]

    users = soup.find_all("div", {"class": "rat-count"})

    list_of_users = [user.getText().strip() for user in users]
    
    ### Cleaning new dataframe

    users = list()
    for user in list_of_users:
        user = user.replace(",", "")
        users.append(int(user))

    pattern_title = r'^.+?(?=\  )'
    pattern_year = r'\d{4}'

    titles = list()
    years_str = list()
    for string in list_of_titles:
        titles.append(re.search(pattern_title,string).group())
        years_str.append(re.search(pattern_year,string).group())

    years = list()
    for year in years_str:
        years.append(int(year))

    dict_ = {'Title_FA' : titles, 'Year_FA' : years, 'Director_FA' : list_of_directors, 'Rating_FA' : list_of_rating, 'No_of_Votes_FA' : users} 

    filmaffinity = pd.DataFrame(dict_)

    return filmaffinity

def cleaning(IMDB):
    """
    Cleans a dataframe.
    Args:
        IMDB (df): the dataframe that wants to be cleaned
    Returns:
        The dataframe cleaned
    """

    IMDB.drop(['Star1_Character1','Star2_Character2','Star3_Character3','Star4_Character4','IMDB_ID', 'Gross','Meta_score' ,'Runtime','Certificate','Genre', 'Genres_Clean', 'Genres_Grouped' ],axis=1,inplace=True)

    IMDB = IMDB.head(30)

    IMDB = IMDB.rename(columns={'Series_Title': 'Title_IMDB', 'Released_Year': 'Year_IMDB','IMDB_Rating': 'Rating_IMDB', 'Director' : 'Director_IMDB', 'No_of_Votes' : 'No_of_Votes_IMDB'  })

    return(IMDB)

def joining(IMDB, filmaffinity):
    """
    Joins two dataframe
    Args:
        IMDB (df): first dataframe
        filmaffinity(df): second dataframe
    Returns:
        The dataframe of the two dataframes joined.
    """

    df = IMDB.join(filmaffinity)

    return df

def intersection(df,IMDB, filmaffinity):

    """
    Creates a new dataframe with the intersection of two dataframes.
    Args:
        df (df): dataframe needed for nested functions to work
        IMDB (df): first dataframe
        filmaffinity(df): second dataframe
    Returns:
        The dataframe of the intersection
    """
    
    titles_IMDB = set(df['Title_IMDB'])
    titles_FA = set(df['Title_FA']) 

    intersection = titles_IMDB.intersection(titles_FA)

    list(intersection).sort()

    IMDB_reduced = f.create(IMDB,'Title_IMDB',intersection)

    filmaffinity_reduced = f.create(filmaffinity,'Title_FA',intersection)

    IMDB_red = IMDB_reduced.sort_values(by=['Title_IMDB'])

    FA_red = filmaffinity_reduced.sort_values(by=['Title_FA'])

    IMDB_red = IMDB_red.reset_index()
    FA_red = FA_red.reset_index()

    IMDB_red.drop(['index'],axis=1, inplace=True)

    FA_red.drop(['index'],axis=1, inplace=True)

    df_reduced = FA_red.join(IMDB_red)

    df_reduced.drop(['Year_FA','Year_IMDB', 'Director_FA', 'Director_IMDB', 'Title_IMDB'],axis=1,inplace=True)

    df_reduced = df_reduced.rename(columns = {'Title_FA' : 'Title'})

    return df_reduced