from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from splinter import Browser
import requests

def scrape():
    # Latest News

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    title = soup.find("div", class_="content_title").get_text()
    news_p = soup.find("div", class_='rollover_description_inner').get_text()


    # Featured Image
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    images = soup.find_all('div', class_='carousel_items')
    
    for url in images:
        urlfull = url.find('article')['style']
  
    url = urlfull.split("'",-1)[1]
    featured_image_url = 'https://www.jpl.nasa.gov' + url
    browser.quit()
    
    # Mars Weather

    url3 = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url3)

    soup = bs(response.text, 'html.parser')
    weather = soup.find("div", class_="js-tweet-text-container").get_text()

    # Mars Fact Table

    url4 = 'https://space-facts.com/mars/'

    tables = pd.read_html(url4)
    df = tables[0]
    df.columns = ['Info Title', 'Data']
    df2 = df.set_index('Info Title')
    mars_data = df2.to_html()
    mars_data.replace('\n', '')

    # Mars Hemispheres

    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response = requests.get(url5)
    soup = bs(response.text, 'html.parser')

    # Cererbus

    url6 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    response = requests.get(url6)
    soup = bs(response.text, 'html.parser')
    clink = soup.find_all('img', class_='wide-image')
    for link in clink:
        url6f = link['src']

    # Schiaparelli

    url7 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    response = requests.get(url7)
    soup = bs(response.text, 'html.parser')
    slink = soup.find_all('img', class_='wide-image')
    for link in slink:
        url7f = link['src']

    # Syrtis Major

    url8 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    response = requests.get(url8)
    soup = bs(response.text, 'html.parser')
    smlink = soup.find_all('img', class_='wide-image')
    for link in smlink:
        url8f = link['src']

    # Valles Marineris

    url9 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    response = requests.get(url9)
    soup = bs(response.text, 'html.parser')
    vmlink = soup.find_all('img', class_='wide-image')
    for link in vmlink:
        url9f = link['src']

    # All Hemispheres

    hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": 'https://astrogeology.usgs.gov' + url6f},
    {"title": "Valles Marineris Hemisphere", "img_url":'https://astrogeology.usgs.gov' + url7f},
    {"title": "Schiaparelli Hemisphere", "img_url": 'https://astrogeology.usgs.gov' + url8f},
    {"title": "Syrtis Major Hemisphere", "img_url":'https://astrogeology.usgs.gov' + url9f},
    ]

    mars_stuff = {
        'news_title' : title,
        'news_p' : news_p,
        'featured_image_url' : featured_image_url,
        'mars_weather' : weather,
        'mars_facts' : mars_data, 
        'mars_hemispheres' : hemisphere_image_urls}

    return mars_stuff

