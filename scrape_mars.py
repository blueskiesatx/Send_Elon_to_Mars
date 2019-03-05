##scrape_mars 
#coding: utf-8
#Import dependencies Beautiful soup for parsing and splinter for site navigation
#using chrome browser

from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from selenium import webdriver
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pandas as pd
import re
import requests

def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}

##Visit the NASA news url and scrape
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')

    #Save the most recent article, with title and date
    article=soup.find("div",class_="list_text")
    news_title = article.find("div",class_="content_title").text
    news_date = article.find("div",class_ ="list_date").text
    news_p = soup.find("div", class_= "article_teaser_body").text
    
    mars_data["Title"] = news_title
    mars_data["Date"] = news_date
    mars_data["Summary"] = news_p
    
#JPL Mars Space Images - Featured Image
#JPL Mars url
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')

    browser.find_by_id('full_image').click()
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    featured_image_url = 'https://www.jpl.nasa.gov' + soup.find('img', class_ = 'fancybox-image')['src'] 
    mars_data['featured_image_url'] = featured_image_url

#Mars Weather
#Scraping latest Mars weather from their Twitter
    # executable_path = {"executable_path": "chromedriver"}
    # browser= Browser("chrome", **executable_path, headless=False)

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    weather_soup = bs(html, 'html.parser')
    mars_weather = weather_soup.find('div', class_='js-tweet-text-container').find("p",class_="tweet-text").get_text()
    mars_data['mars_weather'] = mars_weather

#In case they tweeted something complicated, can scrape recent tweet
    # html = browser.html
    # weather_soup = bs(html, 'html.parser')
    # mars_recent_tweet=mars_weather.find("p",class_="tweet-text").get_text()
    # mars_data["mars_recent_tweet"] = mars_recent_tweet

#Mars Facts
#Visit the facts url and scrape data. Put into panda.
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    time.sleep(1)
    tables = pd.read_html(url)
    
    df_mars = tables[0]
    df_mars.columns = ['Description', 'Value']

    #Put facts into html
    html_mars = df_mars.to_html()
    mars_data['html_mars'] = html_mars

#Mars Hemisphere Images
    hemisphere_image_urls = []

#Cerberus Hemisphere
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    browser.find_link_by_partial_text('Cerberus Hemisphere Enhanced').click()
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    cerberus_url = soup.find('div', class_ = 'downloads').a['href']
    cerberus_title = soup.find("h2", class_="title").text
    cerberus = {
        'title': cerberus_title,
        'img_url': cerberus_url
    }
    hemisphere_image_urls.append(cerberus)

#Schiaparelli Hemisphere

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    browser.find_link_by_partial_text('Schiaparelli Hemisphere Enhanced').click()
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    schiaparelli_url = soup.find('div', class_= 'downloads').a['href']
    schiaparelli_title = soup.find('h2', class_='title').text
    schiaparelli = {
        'title': schiaparelli_title,
        'img_url': schiaparelli_url
    }   
    hemisphere_image_urls.append(schiaparelli)

#Syrtis Major Hemisphere
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    browser.find_link_by_partial_text('Syrtis Major Hemisphere Enhanced').click()
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    syrtis_url = soup.find('div', class_ = 'downloads').a['href']
    syrtis_title = soup.find("h2", class_='title').text
    syrtis= {
        'title': syrtis_title,
        'img_url': syrtis_url
    }
    hemisphere_image_urls.append(syrtis)

#Valles Marineris Hemisphere

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    browser.find_link_by_partial_text('Valles Marineris Hemisphere Enhanced').click()
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    valles_url = soup.find('div', 'downloads').a['href']
    valles_title = soup.find('h2', class_='title').text
    valles = {
        'title': valles_title,
        'img_url': valles_url
    }
    hemisphere_image_urls.append(valles)
    

    mars_data['hemisphere_image_urls'] = hemisphere_image_urls

    return mars_data