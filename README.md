# investing-tickets-scrapper
#### This package scraps all tickets available from "investing.com" site

## How to install
Installing "investing-tickets-scrapper" from pypi (recomended).
```bash
pip install investing-tickets-scrapper
```

#### or

Installing "investing-tickets-scrapper" using the repository.
```bash
pip install -e .
```

## How to use

```python
# Import the library
from investing_tickets_scrapper.scrapper import Scrapper
import pandas as pd

# Create the object scrapper using the imported class
scrapper = Scrapper()

# Configurates the scrapper
scrapper.config(chromedriver_path="C:\Program Files (x86)\chromedriver.exe", # Chromedriver_path = chromedriver for Selenium, if you don't know what is it, check this video "https://youtu.be/Xjv1sY630Uc" and install it
                country="United States")  # Country = the country you want to scrap the tickeks. To check all countries available you can use "print(scrapper.contries_available())"
                                                                                                      
# Start scrapping
scrapper.scrap() # It will open the Google Chrome and scrap it. Is recommended not to use the mouse and the keboard

# Return the data as a pandas dataframe
df = scrapper.return_dataframe()
print(df) # df

#
```
