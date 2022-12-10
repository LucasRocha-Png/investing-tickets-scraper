# Import the library
from investing_tickets_scraper.scraper import Scraper
import pandas as pd

# Create the object scraper using the imported class
scraper = Scraper()

# Configurates the scraper
scraper.config(chromedriver_path="C:\Program Files (x86)\chromedriver.exe", # Chromedriver_path = chromedriver for Selenium, if you don't know what is it, check this video "https://youtu.be/Xjv1sY630Uc" and install it
                country="Argentina")  # Country = the country you want to scrap the tickeks. To check all countries available you can use "print(scraper.contries_available())"
                                                                                                      


# Start scrapping
scraper.scrap() # It will open the Google Chrome and scrap it. Is recommended not to use the mouse and the keboard

# Return the data as a pandas dataframe
df = scraper.return_dataframe()
#print(df) # df
df.to_csv("result.csv")
#