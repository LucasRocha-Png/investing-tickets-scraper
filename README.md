# investing-tickets-scraper
#### This package scraps all tickets available from "investing.com" site

## How to install
Installing "investing-tickets-scraper" from pypi (recomended).
```bash
pip install investing-tickets-scraper
```

## How to use

```python
# Import the library
from investing_tickets_scraper.scraper import Scraper
import pandas as pd

# Create the object scraper using the imported class
scraper = Scraper()

# Configurates the scraper
scraper.config(chromedriver_path="C:\Program Files (x86)\chromedriver.exe", # Chromedriver_path = chromedriver for Selenium, if you don't know what is it, check this video "https://youtu.be/Xjv1sY630Uc" and install it
                country="United States")  # Country = the country you want to scrap the tickeks. To check all countries available you can use "print(scraper.contries_available())"
                                                                                                      
# Start scraping
scraper.scrap() # It will open the Google Chrome and scrap it. Is recommended not to use the mouse and the keboard

# Return the data as a pandas dataframe
df = scraper.return_dataframe()
print(df) # df
```
