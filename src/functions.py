import numpy as np

def space_to_two_points(string):
    try:
        return string.replace(" ", ":")
    except:
        return string


def result_to_df(list_,name):
    import pandas as pd
    list_ = pd.Series(list_)
    list_ = list_.to_frame(name)
    return list_


def list_of_characters(index,list_,cast):
    for actor in cast:
        try:
            list_.append(actor[index]['character'])
        except:
            list_.append('Unknown')
    return(list_)

def string_to_int(string):
    """
    Turns a string into a integer (if possible)
    Args:
        string (string): string to work with 
    Returns:
        If it is possible it returns the string as an integer, if not, it returns nan.
    """
    try:
        string = string.replace(",", "")
        return int(string)
    except: 
        return np.nan

def create(df,column,list_):
    """
    Creates a subdataframe with those values of the given column present in the given list 
    Args:
        df (dataframe): dataframe to work with 
        column (series): column of the dataframe to be filtered on
        list_ (list): list with the values that are used for filtering 
    Returns:
        The subdataframe
    """
    return df[df[column].isin(list_)]