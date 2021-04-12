
import os
import requests 

def calling_api(df_url):

    """
    Requests and safe information from an API
    Args:
        df_url(string): the string that needs to be added to the url to make the call
    Returns:
        A dictionary with de data collected
    """
   
    api_key = os.getenv("token")
    api_host = os.getenv("host")

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': api_host
        }

    url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/"

    imdb_id = list()
    rating_votes = list()
    cast = list()

    os.system('say -v Samantha calling the API, it may take a few minutes, please wait')

    for film in df_url.head(100):
        try: 
            response = requests.request("GET", url + film, headers=headers).json()
            imdb_id.append(response['id'])
            rating_votes.append(response['rating_votes'])
            cast.append(response['cast'])
        except:
            imdb_id.append("Unknown")
            rating_votes.append("Unknown")
            cast.append("Unknown")

    os.system('say -v Samantha Call completed')
    
    dict_ = {'imdb_id' : imdb_id, 'rating_votes' : rating_votes, 'cast': cast}

    return(dict_)




