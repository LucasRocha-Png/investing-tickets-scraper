from investing_tickets_scrapper.scrapper import Scrapper

scrapper = Scrapper()
scrapper.config(chromedriver_path="C:\Program Files (x86)\chromedriver.exe", country="Japan")
scrapper.scrap()
df = scrapper.return_dataframe()
df.to_csv("result.csv")
