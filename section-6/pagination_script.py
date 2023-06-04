from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import *
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

website = "https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=adc4b13b-d074-4e1c-ac46-9f54aa53072b&pf_rd_r=6Z3BNK326ZH91DJ8XS8G"

# Specify the path to the Chrome driver executable
chrome_driver_path = '/usr/bin/google-chrome'

# Create a Service object
service = Service(chrome_driver_path)

# Set Chrome options if needed
options = webdriver.ChromeOptions()
# options.add_argument('--headless')


# Create the Chrome driver instance using the Service object and options
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

# create a dataframe with the desired info
title = []
author = []
narrator = []
series = []
length = []
releaseDate = []
language = []

pagination_box = driver.find_element(By.XPATH, '//*[@id="pagination-a11y-skiplink-target"]/div/div[2]/div/span/ul')
pages = pagination_box.find_elements(By.XPATH, './li')
last_page = int(pages[-2].text)
current_page = 1

# scrape the website
while current_page <= last_page:
    print(f"scraping page{current_page}")
    product_box = driver.find_element(By.XPATH, '//*[@id="product-list-a11y-skiplink-target"]/span/ul')
    products = product_box.find_elements(By.XPATH, f'.//li[contains(@class, "productListItem")]')

    # scrape the page
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
    
    # Break if current_page == last_page
    if current_page == last_page:
        print("Completed Successfully!")
        break
    
    # Go to next page
    try:
        pagination_box = driver.find_element(By.XPATH, '//*[@id="pagination-a11y-skiplink-target"]/div/div[2]/div/span/ul')
        next_page = pagination_box.find_element(By.XPATH, './/span[contains(@class, "nextButton")]')
        next_page.click()
        # Wait for the next page to load
        WebDriverWait(driver, 15).until(EC.staleness_of(product_box))
    
    except Exception as e:
        print(e)
        pass

    current_page = current_page + 1

# create a dataframe 
df = pd.DataFrame({'title':title, 'author':author, 'narrator':narrator,'series':series, "length":length,'releaseDate':releaseDate, 'language':language})

# convert to csv
df.to_csv('best_audio_books.csv', index=False)
driver.close()
driver.quit()





