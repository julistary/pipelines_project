# Pipelines Project

<img width=200 src="https://screwthehighroad.files.wordpress.com/2015/07/imdb.png">

## Goal
This is a python project that was sent to us at the Ironhack data analytics bootcamp. 

For this project, we had to choose a dataset, enriching it through the use of apis or web scrapping and build a data pipeline that processes the data and produces a result. 

The tools to be used are functions, list comprehensions, string operations, pandas, and error handling, etc. 

## Libraries
- [Pandas](https://pandas.pydata.org/docs/)
- [Requests](https://docs.python-requests.org/en/master/)
- [Os](https://docs.python.org/3/library/os.html)
- [Dotenv](https://pypi.org/project/python-dotenv/)
- [Re](https://docs.python.org/3/library/re.html)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Numpy](https://numpy.org/doc/)

## My project

I selected from kaggle a dataset with information about the top 1000 movies from ***IMDB*** and a RapidAPI API with complementary information about those movies, also from ***IMDB***. 

From that dataframe, I expanded information on the top 100 movies thanks to the API, cleaned the resulting dataframe and came to certain conclusions. 

Then, I created another dataframe with the 30 best movies according to filmaffinity thanks to web scrapping. I put it together with the initial IMDB dataframe and came to some conclusions. 

## Steps followed

1. Downloading and importing dataset
2. Enriching it with data from the API
3. Cleaning it 
4. Creating a new dataframe with information from web-scrapping filmaffinity.com
5. Joining it with the IMDB dataframe
6. Plotting and extracting conclusions