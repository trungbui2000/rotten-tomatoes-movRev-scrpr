# Main file to scrape data, using an imported csv file which was donwloaded from Kaggle that has a list of movies,
# we go through each movie title and convert it the proper format of URL that Rotten Tomatoes accept and using the
# appropriate URL, we feed it into the datascraping function that consequently give back a list of attributes
# Since Rotten Tomatoes does not have a set convention for every single movie reivew, not every URL we re-constructed
# will be correct and thus, some movies will not be scraped.

# Author - Minh Hua and Trung Bui

# Importing the neccessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import random as rd

from dataScraping import printData

# The function belows are for clearning the data URL purposes since Rotten Tomatoes does not have a single URL convention for every movie review so we have to do multiple try/catch block.
def fixNormal(url):
    return url.lower().replace(" ","_").replace("_-_", "_").replace("the_","").replace(":","").replace("'","").replace("-","_").replace(",","").replace(".","").replace("!","").replace("é","e").replace("á","a")
def fixWithoutThe(url):
    return url.lower().replace(" ","_").replace("_-_", "_").replace(":","").replace("'","").replace("-","_").replace(",","").replace(".","").replace("!","").replace("é","e").replace("á","a")
def fixWithoutA(url):
    return url.lower().replace(" ","_").replace("_-_", "_").replace(":","").replace("'","").replace("-","_").replace(",","").replace(".","").replace("!","").replace("é","e").replace("á","a").replace("a_","")

# Main program code here

# Constructing a for loop that goes through the whole dataset
j = 0
err_list = []
df = pd.DataFrame(columns = ["dataIndex", "realTitle", "criticsConcensus", "tomatoMeter", "tomatoCount", 
            "audienceScore", "audienceCount", "realSynopsis", "rating", "genreString", 
            "directedBy", "studio", "runTime", "cast"])

data = pd.read_csv("movie_data.csv", error_bad_lines=False, dtype='unicode')

# Looping through the entire dataset, could be faster if you split up into smaller chunks like range(0,2000), (2000, 4000), (4000,6000) until the end of the data 
for i in range(0, len(data)):
        try:
            fixed = fixNormal(data.at[i, "title"])
            movie_data = printData("https://www.rottentomatoes.com/m/" + fixed)
            # Uncomment to keep track of what movie is being scraped
            print("Success at fixNormal at new title: " + str(i))
            df.at[j, "realTitle"] = movie_data[0]
            df.at[j, "criticsConcensus"] = movie_data[1]
            df.at[j, "tomatoMeter"] = movie_data[2]
            df.at[j, "tomatoCount"] = movie_data[3]
            df.at[j, "audienceScore"] = movie_data[4]
            df.at[j, "audienceCount"] = movie_data[5]
            df.at[j, "realSynopsis"] = movie_data[6]
            df.at[j, "rating"] = movie_data[7]
            df.at[j, "genreString"] = movie_data[8]
            df.at[j, "directedBy"] = movie_data[9]
            df.at[j, "studio"] = movie_data[10]
            df.at[j, "runTime"] = movie_data[11]
            df.at[j, "cast"] = movie_data[12]
            df.at[j, "dataIndex"] = i
            j += 1
        except:
            try:
                fixed = fixWithoutThe(data.at[i, "title"])
                movie_data = printData("https://www.rottentomatoes.com/m/" + fixed)
                # Uncomment to keep track of what movie is being scraped
                # print("Success at fixWithoutThe at new title: " + str(i))
                df.at[j, "realTitle"] = movie_data[0]
                df.at[j, "criticsConcensus"] = movie_data[1]
                df.at[j, "tomatoMeter"] = movie_data[2]
                df.at[j, "tomatoCount"] = movie_data[3]
                df.at[j, "audienceScore"] = movie_data[4]
                df.at[j, "audienceCount"] = movie_data[5]
                df.at[j, "realSynopsis"] = movie_data[6]
                df.at[j, "rating"] = movie_data[7]
                df.at[j, "genreString"] = movie_data[8]
                df.at[j, "directedBy"] = movie_data[9]
                df.at[j, "studio"] = movie_data[10]
                df.at[j, "runTime"] = movie_data[11]
                df.at[j, "cast"] = movie_data[12]
                df.at[j, "dataIndex"] = i
                j += 1
            except:
                try:
                    fixed = fixNormal(data.at[i, "title"])
                    movie_data = printData("https://www.rottentomatoes.com/m/" + fixed + "_" + data.at[i, "Year"])
                    # Uncomment to keep track of what movie is being scraped
                    # print("Success at fixNormal with new title and years: " + str(i))
                    df.at[j, "realTitle"] = movie_data[0]
                    df.at[j, "criticsConcensus"] = movie_data[1]
                    df.at[j, "tomatoMeter"] = movie_data[2]
                    df.at[j, "tomatoCount"] = movie_data[3]
                    df.at[j, "audienceScore"] = movie_data[4]
                    df.at[j, "audienceCount"] = movie_data[5]
                    df.at[j, "realSynopsis"] = movie_data[6]
                    df.at[j, "rating"] = movie_data[7]
                    df.at[j, "genreString"] = movie_data[8]
                    df.at[j, "directedBy"] = movie_data[9]
                    df.at[j, "studio"] = movie_data[10]
                    df.at[j, "runTime"] = movie_data[11]
                    df.at[j, "cast"] = movie_data[12]
                    df.at[j, "dataIndex"] = i
                    j += 1
                except:
                    try:
                        fixed = fixNormal(data.at[i, "original_title"])
                        movie_data = printData("https://www.rottentomatoes.com/m/" + fixed)
                        # Uncomment to keep track of what movie is being scraped
                        # print("Success at fixNormal with Original title: " + str(i))
                        df.at[j, "realTitle"] = movie_data[0]
                        df.at[j, "criticsConcensus"] = movie_data[1]
                        df.at[j, "tomatoMeter"] = movie_data[2]
                        df.at[j, "tomatoCount"] = movie_data[3]
                        df.at[j, "audienceScore"] = movie_data[4]
                        df.at[j, "audienceCount"] = movie_data[5]
                        df.at[j, "realSynopsis"] = movie_data[6]
                        df.at[j, "rating"] = movie_data[7]
                        df.at[j, "genreString"] = movie_data[8]
                        df.at[j, "directedBy"] = movie_data[9]
                        df.at[j, "studio"] = movie_data[10]
                        df.at[j, "runTime"] = movie_data[11]
                        df.at[j, "cast"] = movie_data[12]
                        df.at[j, "dataIndex"] = i
                        j += 1
                    except:
                        try:
                            fixed = fixWithoutA(data.at[i, "title"])
                            movie_data = printData("https://www.rottentomatoes.com/m/" + fixed)
                            # Uncomment to keep track of what movie is being scraped
                            # print("Success at fixWithoutA: " + str(i))
                            df.at[j, "realTitle"] = movie_data[0]
                            df.at[j, "criticsConcensus"] = movie_data[1]
                            df.at[j, "tomatoMeter"] = movie_data[2]
                            df.at[j, "tomatoCount"] = movie_data[3]
                            df.at[j, "audienceScore"] = movie_data[4]
                            df.at[j, "audienceCount"] = movie_data[5]
                            df.at[j, "realSynopsis"] = movie_data[6]
                            df.at[j, "rating"] = movie_data[7]
                            df.at[j, "genreString"] = movie_data[8]
                            df.at[j, "directedBy"] = movie_data[9]
                            df.at[j, "studio"] = movie_data[10]
                            df.at[j, "runTime"] = movie_data[11]
                            df.at[j, "cast"] = movie_data[12]
                            df.at[j, "dataIndex"] = i
                            j += 1
                        except:
                            err_list.append(i)
                            # Uncomment to keep track of what the movie URL that failed
                            # print("Failure: " + str(i) + (" https://www.rottentomatoes.com/m/" + fixed))
                            pass

# Movies that are not scraped will be stored in the files
with open("errors.txt", "w") as output:
    output.write(str(str(err_list).encode('utf8')))

# All the scraped movies will then be put into a csv files and stored under the appropriate file name.
df.to_csv("data-scraped.csv")
