# Rotten Tomatoes Movie Review Scraper

## Purpose
The purpose of this project is to generate a scraper function that allows the user to input any Rotten Tomatoes movie URL and returns all the available information on Rotten Tomatoes about the specified movie. In the end, the goal of our project is:
1. To be able to have database of different movie names and a Python script that iterates through the database. 
2. At each iteration, we will construct the appropriate URL for the movie name
3. Using the constructed URL, we will feed it into the function named `printData` that will return the information about the movie

## Method 
* Using the library BeautifulSoup as a way to parse through HTML elements, we were able to precisely pinpoint the relevant information we want to extracted from the given movie. Next, we generalized the method functionality to be able to take in movies URL and named the method `printData` which is created inside `dataScraping.py`
* We then found a dataset named `movies_data.csv` that contains 45,000 movie names, and by parsing through the dataset, we can extract the movie name and use those names to construct the URL that goes into our `printData` method. Since Rotten Tomatoes does not have one set of naming convention for all its movies, there are many possibilites/convention that we found for the majority of the movies and thus, we use 5 nested try/excerpt blocks. As a result, we managed to get 

