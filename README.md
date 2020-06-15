# Rotten Tomatoes Movie Review Scraper

## Purpose
The purpose of this project is to generate a scraper function that allows the user to input any Rotten Tomatoes movie URL and returns all the available information on Rotten Tomatoes about the specified movie. In the end, our goal for the project is:
1. To be able to have database of different movie names and a Python script that iterates through the database. 
2. At each iteration, we will construct the appropriate URL for the movie name
3. Using the constructed URL, we will feed it into the function named `printData` that will return the information about the movie

## Method 
* Using the library `BeautifulSoup` as a way to parse through HTML elements, we were able to precisely pinpoint the relevant information we want to extracted from the given movie. Next, we generalized the method functionality to be able to take in movies URL and named the method `printData` which is created inside `dataScraping.py`
* We then found a dataset named `movies_data.csv` that contains 45,000 movie names, and by parsing through the dataset, we can extract the movie name and use those names to construct the URL that goes into our `printData` method. Since Rotten Tomatoes does not have one set of naming convention for all its movies, there are many conventions that we found for the majority of the movies and thus, we use five try/excerpt blocks nested in each other so that if one convention is wrong, we can try other conventions. Consequently, if all conventions fail, we will put the index of the movie in the `movies_data.csv` inside the `error.txt` file and carry on to the next movie down the list. In the end all of the movies that were successfully scraped will be stored inside the file named `data-scraped.csv`. All these processes are illustrated in the `dataDownload.py`.
* Since our datascraping took a considerably long time, we came up with the solution to run multiple scrapers simultaneously to speed up the scraping processes. As a result, it we ran seven scrapers in parallel with each other and our total data scraping time was around 2 hours and 30 minutes with each processes scraped on around 6,430 movies. All of the initial scraped files are stored inside the `Scraped Files` folder, each have the naming convention of: `[starting index]-[ending index - 1].csv`. 
* We then combined all the segmented datasets that were successfully scraped together into the `combined.csv` inside the `Scraped Files` folder. 

## Deployment
1. Simply fork this repository into your computer
2. Perform `pip install bs4` for BeautifulSoup and `pip install pandas` for Pandas dataframe on your terminal.
3. Go into `dataSraping.py` and under the section `Run First`, uncomment this part of the code and run this script by typing `python3 dataScraping.py` to make sure there is no error in the method. If you did not encountered any error, proceed to the next step but if you did please read below.
    *  If there is a `[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed`, this is most likely because you have don't have the appropriate certification. Follow [this stackOverflow Link](https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error/42334357#42334357) if you did not install your Python using `homebrew` and if you used `homebrew` then follow 
[this stackOverflow Link](https://stackoverflow.com/questions/44649449/brew-installation-of-python-3-6-1-ssl-certificate-verify-failed-certificate/44649450#44649450). For the latter option, there is `certificate.py` for usage to make it faster to have the needed certifications.
4. Then to see the datascraper going through the list of movies inside `movies_data.csv`, run `python3 dataDownload.py`

## Additional Information
* Inside this repository, a Jupyter Notebook with the name `websiteScraper.ipynb` was created as a way to have faster demonstration of what was described above without forking the repository. Simply click on the notebook and it will direct you to a static HTML page and you can see the code structure and layout.
* We managed to successfully scrape 18,445 movies out of 45,000 movies inside the `movies_data.csv` database which is equivalent to a 40.9889% success rate for our scraper.

## Challenges 
* The main problem that we struggled with throughout this project is to find the appropriate conventions to increase our scraper success rate, however as there are so many conventions, it was difficult to capture all of them.
* Additionally, we found that for the majority of the movies we scraped, there are a lot of attributes that were missing from the movies and when this happens, the scraper puts "nothing" in the appropriate data slots. Below is an example of a movie that has all the attributes:
