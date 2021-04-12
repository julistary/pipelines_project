import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualization():
    sns.set_palette("cool")

    df = pd.read_csv("data/df_short_clean.csv")
    df_IMDB_FA = pd.read_csv("data/df_IMDB_FA.csv")
    df_reduced = pd.read_csv("data/IMDB_FA_reduced.csv")

    df.drop(['Unnamed: 0'],axis=1, inplace=True)
    df_IMDB_FA.drop(['Unnamed: 0'],axis=1, inplace=True)
    df_reduced.drop(['Unnamed: 0'],axis=1, inplace=True)

    ### IMDB Rating and Meta_score

    fig, ax = plt.subplots(figsize=(10, 5))
    Metascore_Rating = sns.scatterplot(x="IMDB_Rating", y="Meta_score", data=df)
    ax.set_title("Meta Score and IMDB Rating")
    Metascore_Rating.figure.savefig("images/Metascore_Rating.svg")

    ### IMDB Rating and Number of Votes

    fig, ax = plt.subplots(figsize=(10, 5))
    Votes_Rating = sns.scatterplot(x="IMDB_Rating", y="No_of_Votes", data=df)
    ax.set_title("Number of votes and IMDB Rating")
    Votes_Rating.figure.savefig("images/Votes_Rating.svg")

    ### Number of Votes and Gross

    fig, ax = plt.subplots(figsize=(10, 5))
    Votes_Gross = sns.scatterplot(x="No_of_Votes", y="Gross", data=df)
    ax.set_title("Number of votes and Gross")
    Votes_Gross.figure.savefig("images/Votes_Gross.svg")

    ### IMDB Rating and Genre

    fig, ax = plt.subplots(figsize=(10, 5))
    Rating_Genre = sns.scatterplot(x="IMDB_Rating", y="IMDB_Rating", hue = "Genres_Grouped", data=df)
    ax.set_title("IMDB Rating and Genre")
    Rating_Genre.figure.savefig("images/Rating_Genre.svg")

    ### Most frequent genres

    fig, ax = plt.subplots(figsize=(20, 5))
    frequent_genre= sns.countplot(x="Genres_Clean", data=df)
    ax.set_title("Genre's Frequency")
    plt.xticks(rotation=30)
    frequent_genre.figure.savefig("images/frequent_genre.svg")

    ### Released years 

    fig, ax = plt.subplots(figsize=(20, 5))
    released_years= sns.kdeplot(x="Released_Year", data=df)
    ax.set_title("Released Years")
    released_years.figure.savefig("images/released_years.svg")

    ### Released Years IMDB vs FILMAFFINTY

    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(15, 10))
    years_FA = sns.boxplot(x="Year_FA", data=df_IMDB_FA, ax=axs[1])
    years_IMDB = sns.boxplot(x="Year_IMDB", data=df_IMDB_FA, ax=axs[0])
    plt.savefig("images/years_IMDB_FA.svg")

    ### Number of Votes IMDB vs Filmaffinity

    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(15, 10))
    votes_IMDB = sns.boxplot(x="No_of_Votes_IMDB", data=df_IMDB_FA, ax=axs[0])
    votes_FA = sns.boxplot(x="No_of_Votes_FA", data=df_IMDB_FA,ax=axs[1])
    plt.savefig("images/votes_IMDB_FA.svg")

    ### Rating IMDB vs Filmaffinity

    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(15, 10))
    rate_IMDB = sns.boxplot(x="Rating_IMDB", data=df_IMDB_FA, ax=axs[0])
    rate_FA = sns.boxplot(x="Rating_FA", data=df_IMDB_FA,ax=axs[1])
    plt.savefig("images/rating_IMDB_FA.svg")

    ### Rating IMDB vs Filmaffinity (same films)

    fig, ax = plt.subplots(figsize=(15, 8))
    ax.set_title("Rating IMDB vs Filmaffinity")
    plt.xticks(rotation=40)
    plt.plot(df_reduced["Title"], df_reduced["Rating_IMDB"], label="IMDB")
    plt.plot(df_reduced["Title"], df_reduced["Rating_FA"], label="FA")
    plt.legend(loc="upper left")
    plt.savefig("images/rating_IMDB_FA_same_films.svg")

    ### Number of votes IMDB vs Filmaffinity (same films)

    fig, ax = plt.subplots(figsize=(15, 8))
    ax.set_title("Nr of Votes IMDB vs Filmaffinity")
    plt.xticks(rotation=40)
    plt.plot(df_reduced["Title"], df_reduced["No_of_Votes_IMDB"], label="IMDB")
    plt.plot(df_reduced["Title"], df_reduced["No_of_Votes_FA"], label="FA")
    plt.legend(loc="upper left")
    plt.savefig("images/votes_IMDB_FA_same_films.svg")

