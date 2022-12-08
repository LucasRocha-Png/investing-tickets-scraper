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



class Scrapper():    
    def __init__(self):
        """
        Import the list of countries available and set other variables
        """
        
        self.folder = os.path.dirname(__file__)
        self.countries = pd.read_csv(f"{self.folder}\\countries_available.csv")["Countries"].to_list()
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
        Set the configuration for the scrapper
        """
       
        if country not in self.countries:
            raise ValueError("Country is not avaible, check if you typed correctly and with . Check all countries available in Scrapper().countries_available()")
        else:
            self.country = country
            
        if not os.path.isfile(chromedriver_path):
            raise ValueError(f"Chromedriver not found at {chromedriver_path}")
        else:
            self.chromedriver_path = chromedriver_path
        
    def scrap(self):
        """
        Scrap investing.com site
        """
        if self.chromedriver_path == None or self.country == None:
            raise ValueError("chromedriver_path and country are equal to None. Set chomedriver_path and country at Scrapper().config()")
        
        #Configurate Selenium
        chrome_options = ChromeOptions()
        chrome_options.add_extension(f"{self.folder}\\adblock.crx")
        driver = webdriver.Chrome(self.chromedriver_path, options=chrome_options)
        
        #Open page
        driver.get("https://www.investing.com/stock-screener/")
        #driver.maximize_window()
        driver.switch_to.window(driver.window_handles[0])  
        
        #Wait for close sing up page
        # close_bar = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "popupCloseIcon largeBannerCloser")))
        
        #Locate index bar and set the country
        bar = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/section/div[6]/div[1]/a/input")))
        bar.clear()
        bar.send_keys(self.country)
        time.sleep(2)
        bar.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5)
        bar.send_keys(Keys.ENTER)
        time.sleep(5) #Wait until page is loaded
        
        #Take the columns of the table
        columns = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/section/div[11]/div[5]/table/thead")))
        columns = columns.get_attribute('innerHTML')
        columns = BeautifulSoup(columns, "lxml")
        columns = columns.findAll("th")
        list_columns = []
        for column in columns:
            column = column.text
            list_columns.append(column)
        list_columns = list_columns[1:-1]

        
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
        
        #remove the elements from each table catched
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
       
        df = pd.DataFrame(frame)
        df = df[df.columns[1:-1]]
        df.columns = list_columns
        self.df = df
        
    def return_dataframe(self):
        return self.df
    
if __name__ == "__main__":
    scrapper = Scrapper()
    
    
    CHROMEDRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
    COUNTRY = "Brazil"
    
    scrapper.config(chromedriver_path = CHROMEDRIVER_PATH, country=COUNTRY)
    scrapper.scrap()    
    df = scrapper.return_dataframe()    
        