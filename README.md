# Send_Elon_to_Mars
This is a webscraping web app for displaying the collected information in a webpage. We are **not** sending Dr. Elon Musk to Mars, but hey he might want to check out the weather before parking his car there next time.

# Dependencies 
Splinter
Requests
BeautifulSoup
Pandas
Bootstrap
time

# Mission to Mars

This is a basic version of a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Scraping

Initial scraping used Python, Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. 
Used Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.
Also used MongoDB and Flask.
Used Pymongo for CRUD applications for the database.
Used Bootstrap to structure HTML template.


### NASA Mars News

* Scrapes the [NASA Mars News Site](https://mars.nasa.gov/news/) and collects the latest News Title and Paragraph Text. The text is defined with variables.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images - Featured Image

* The url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Used splinter to navigate the site and obtain the image url for the current Featured Mars Image and assigned the url string to a variable called `featured_image_url`. It needs to be saved a jpg in full size with the complete url string for this image.

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

### Mars Weather

* Taken from the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scraping of the latest Mars weather tweet from the page. Saved the tweet text for the weather report as a variable called `mars_weather`.

```python
# Example:
mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
```

### Mars Facts

* From the Mars Facts webpage [here](http://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Taken from the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* The Jupyter notebook was transformed to a Python script called `scrape_mars.py` with a function called `scrape` that will execute all scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, created a route called `/scrape` that will import the `scrape_mars.py` script and call the `scrape` function.

  * Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` that will query the Mongo database and pass the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that takes the mars data dictionary and display all of the data in the appropriate HTML elements. Design examples:

![final_app_part1.jpg](Images/final_app_part1.jpg)
![final_app_part2.jpg](Images/final_app_part2.jpg)

- - -


* 

