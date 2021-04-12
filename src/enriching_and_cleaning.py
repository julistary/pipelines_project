import src.functions as f

def enriching(df, df_short, dict_):

    """
    Enriches and cleans a dataframe with data from dictionaries
    Args:
        df (df): dataframe needed for nested functions to work
        df_short (df): dataframe in which the data will be appended
        dict_ (dict): dictionary with stored data 
    Returns:
        The dataframe enriched and cleaned
    """

    imdb_id = dict_['imdb_id']
    cast = dict_['cast']

    #### Adding the IMDB ID to de dataframe

    IMDB_ID = f.result_to_df(imdb_id, 'IMDB_ID')
    df_short = df_short.join(IMDB_ID)

    #### Adding the main characters of de films to de dataframe

    Character1 = list()
    Star1 = list(df_short['Star1'])
    Character1 = f.list_of_characters(0,Character1,cast)

    Character2 = list()
    Star2 = list(df_short['Star2'])
    Character2 = f.list_of_characters(1,Character2,cast)

    Character3 = list()
    Star3 = list(df_short['Star3'])
    Character3 = f.list_of_characters(2,Character3,cast)

    Character4 = list()
    Star4 = list(df_short['Star4'])
    Character4 = f.list_of_characters(3,Character4,cast)

    Character1 = f.result_to_df(Character1, 'Character1')
    Character2 = f.result_to_df(Character2, 'Character2')
    Character3 = f.result_to_df(Character3, 'Character3')
    Character4 = f.result_to_df(Character4, 'Character4')

    df_short = df_short.join(Character1)
    df_short = df_short.join(Character2)
    df_short = df_short.join(Character3)
    df_short = df_short.join(Character4)

    df_short["Star1_Character1"] = df_short.apply(lambda row: f"{row['Star1']} as {row['Character1']}", axis = 1)
    df_short["Star2_Character2"] = df_short.apply(lambda row: f"{row['Star2']} as {row['Character2']}", axis = 1)
    df_short["Star3_Character3"] = df_short.apply(lambda row: f"{row['Star3']} as {row['Character3']}", axis = 1)
    df_short["Star4_Character4"] = df_short.apply(lambda row: f"{row['Star4']} as {row['Character4']}", axis = 1)

    df_short_clean = df_short.drop(['Star1','Star2','Star3','Star4','Character1','Character2','Character3','Character4', 'Series_Titles_URL' ], axis=1)

    return df_short_clean

def more_cleaning(df_short_clean):
    """
    Cleans a dataframe.
    Args:
        df_short_clean (df): the dataframe that wants to be cleaned
    Returns:
        The dataframe cleaned
    """
    
    ### Cleaning the column 'Genre'

    #### Selecting the accurate genre

    genres = list(df_short_clean['Genre'])

    main_categories = set(['Action', 'Comedy','Fantasy', 'Horror','Mystery', 'Romance', 'Thriller', 'Drama','Adventure'])

    genres_list = list()
    for genre in genres:
        try:
            genres_list.append(list(genre.split(", ")))
        except:
            genres_list.append(genre)

    genres_clean = list()

    for g in genres_list:
        g = set(g)
        if len(list(g.intersection(main_categories))) > 0:
            genres_clean.append(list(g.intersection(main_categories)))
        else:
            genres_clean.append(list(g))

    genres_clean_2 = list()
    main_categories_2 = set(['Action', 'Comedy','Fantasy', 'Horror','Mystery', 'Romance', 'Thriller','Adventure'])
    for g in genres_clean:
        if len(g) == 1:
            genres_clean_2.append(g)
        else: 
            g = set(g)
            genres_clean_2.append(list(g.intersection(main_categories_2)))

    genres_def = list()
    for g in genres_clean_2:
        if len(g) == 1:
            genres_def.append(g[0])
        else:
            genres_def.append(g[0] + ' + ' + g[1])

    for genre in genres_def: 
        if genre == 'Adventure + Action':
            genre = 'Action + Adventure'

    Genres_Clean = f.result_to_df(genres_def, 'Genres_Clean')

    df_short_clean = df_short_clean.join(Genres_Clean)

    #### Grouping the genres

    group_of_genres = ['Drama', 'Action + Adventure', 'Mystery', 'Comedy']
    genres_grouped = list()
    for g in genres_def: 
        if g == 'Action' or g == 'Adventure':
            genres_grouped.append('Action + Adventure')
        elif g == 'Drama' or g == 'Action + Adventure' or g == 'Mystery' or g == 'Comedy':
            genres_grouped.append(g)
        else:
            genres_grouped.append('Other')

    Genres_Grouped = f.result_to_df(genres_grouped, 'Genres_Grouped')

    df_short_clean = df_short_clean.join(Genres_Grouped)

    #### Cleaning column 'Gross'

    df_short_clean['Gross'] = df_short_clean['Gross'].apply(f.string_to_int)

    return df_short_clean