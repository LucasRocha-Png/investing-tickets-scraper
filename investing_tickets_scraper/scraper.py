"""
Creates a class that scrappes "Investing.com" site
"""

import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup



class Scraper():    
    def __init__(self):
        """
        Import the list of countries available and set other variables
        """
        
        self.folder = os.path.dirname(__file__)
        self.countries = pd.read_csv(f"{self.folder}/countries_available.csv")["Countries"].to_list()
        self.chromedriver_path = None
        self.country = None
        self.df = None
    
    def countries_available(self):
        """
        Return the list of countries available
        """
        return self.countries
            
        
    def config(self, chromedriver_path, country):
        """
        Set the configuration for the scraper
        """
       
        if country not in self.countries:
            raise ValueError("Country is not avaible. Check all countries available in Scraper().countries_available()")
        else:
            self.country = country
            
        if not os.path.isfile(chromedriver_path):
            raise ValueError(f"Chromedriver not found at {chromedriver_path}")
        else:
            self.chromedriver_path = chromedriver_path
    
    def parse_columns(self, columns):
        """
        Parses the columns of the table
        """
        columns = BeautifulSoup(columns, "lxml")
        columns = columns.findAll("th")
        list_columns = []
        for column in columns:
            column = column.text
            list_columns.append(column)
        return list_columns
        
    def parse_tables(self, tables):
        """
        Parses the table
        """
        frame = []
        for table in tables:
            soup = BeautifulSoup(table, "lxml")
            rows = soup.findAll("tr")
            for row in rows:
                elements = row.findAll("td")
                line = []
                for element in elements:
                    element = element.text
                    line.append(element)
                frame.append(line)
        return pd.DataFrame(frame)            
    
    def scrap(self):
        """
        Scrap investing.com site
        """
        if self.chromedriver_path == None or self.country == None:
            raise ValueError("chromedriver_path and country are equal to None. Set chomedriver_path and country at Scraper().config()")
        
        #Configure Selenium
        chrome_options = ChromeOptions()
        chrome_options.add_extension(f"{self.folder}/adblock.crx")
        driver = webdriver.Chrome(self.chromedriver_path, options=chrome_options)
        
        #Open the page
        driver.get("https://www.investing.com/stock-screener/")
        driver.maximize_window()
        driver.switch_to.window(driver.window_handles[0])  
        
        #Locate the country bar and set the country
        bar = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/section/div[6]/div[1]/a/input")))
        bar.clear()
        bar.send_keys(self.country)
        time.sleep(0.5)
        bar.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        bar.send_keys(Keys.ENTER)
        time.sleep(5)
        
        #Get table columns
        columns = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/section/div[11]/div[5]/table/thead")))
        columns = columns.get_attribute('innerHTML')
        list_columns = self.parse_columns(columns)

        #Locate Table and change page
        tables = []
        while True:
            try:
            
                time.sleep(2)
                
                table = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/section/div[11]/div[5]/table/tbody")))
                table = table.get_attribute('innerHTML')
                tables.append(table)
                
                next_page = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/section/div[11]/div[5]/div[2]/div[3]/a")))
                next_page.click()
            except:
                driver.quit()
                break
        #------------------------
        
        #Parses the table
        df = self.parse_tables(tables)
        df.columns = list_columns
        self.df = df
        
    def return_dataframe(self):
        """
        Return dataframe
        """
        
        return self.df
    
