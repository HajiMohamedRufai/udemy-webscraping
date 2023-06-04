from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import *
import pandas as pd

website = "https://www.audible.com/search"

# Specify the path to the Chrome driver executable
chrome_driver_path = '/usr/bin/google-chrome'

# Create a Service object
service = Service(chrome_driver_path)

# Set Chrome options if needed
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Create the Chrome driver instance using the Service object and options
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

xpath = '//*[@id="product-list-a11y-skiplink-target"]/span/ul'
# box == ul_box == product_box
product_box = driver.find_element(By.XPATH, xpath)

products = product_box.find_elements(By.XPATH, f'{xpath}//li[contains(@class, "productListItem")]')

# create a dataframe with the desired info
title = []
author = []
narrator = []
series = []
length = []
releaseDate = []
language = []


for product in products:
    title.append(product.find_element(By.XPATH, './/h3').text.strip())
    author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text.split(':')[1].strip())

    try:
        narrator.append(product.find_element(By.XPATH, './/li[contains(@class, "narratorLabel")]').text.split(':')[1].strip())
    except NoSuchElementException:
        narrator.append("N/A")
    
    try:
        series.append(product.find_element(By.XPATH, './/li[contains(@class, "seriesLabel")]').text.split(':')[1].strip())
    except NoSuchElementException:
        series.append("N/A")
    
    try:
        length.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text.split(':')[1].strip())
    except NoSuchElementException:
        length.append("N/A")
    
    try:
        releaseDate.append(product.find_element(By.XPATH, './/li[contains(@class, "releaseDateLabel")]').text.split(':')[1].strip())
    except NoSuchElementException:
        releaseDate.append("N/A")
    
    try:
        language.append(product.find_element(By.XPATH, './/li[contains(@class, "languageLabel")]').text.split(':')[1].strip())
    except NoSuchElementException:
        releaseDate.append("N/A")

        
# create a dataframe 
df = pd.DataFrame({'title':title, 'author':author, 'narrator':narrator,'series':series, "length":length,'releaseDate':releaseDate, 'language':language})

# convert to csv
df.to_csv('audio_books.csv', index=False)
