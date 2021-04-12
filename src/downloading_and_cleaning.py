import os
import src.functions as f

import os
def download_dataset():
    '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
    this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
    Takes: url from kaggle
    Returns: a folder with the downloaded csv
    '''
    
    #Gets the name of the dataset.zip
    url = "https://www.kaggle.com/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows"
    
    #Gets the name of the dataset.zip
    endopint = url.split("/")[-1]
    user = url.split("/")[-2]
    
    #Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {user}/{endopint}; say -v Samantha 'downloading'"
    decompress = f"tar -xzvf {endopint}.zip; say -v Samantha 'unzipping'"
    delete = f"rm -rf {endopint}.zip; say -v Samantha 'erasing the zip'"
    make_directory = "mkdir data"
    lista = "ls >> archivos.txt"
    
    for i in [download, decompress, delete, make_directory, lista]:
        os.system(i)
    
    #Gets the name of the csv (you should only have one csv when running this code)
    lista_archivos = open('archivos.txt').read()
    nueva = lista_archivos.split("\n")
    
    #Moves the .csv into the data directory
    for i in nueva:
        if i.endswith(".csv"):
            move_and_delete = f"mv {i} data/dataset.csv; rm archivos.txt; say -v Samantha 'moving dataset'"
            return os.system(move_and_delete)

def preliminary_cleaning(df):
    """
    Cleans a dataframe.
    Args:
        df (df): the dataframe that wants to be cleaned
    Returns:
        The dataframe cleaned
    """
    df = df.drop_duplicates()
    df.dropna(axis = 0, how="all",inplace=True)
    df.drop(['Poster_Link','Overview'], axis=1, inplace = True)
    df['Series_Titles_URL'] = df['Series_Title'].apply(f.space_to_two_points)
    return df