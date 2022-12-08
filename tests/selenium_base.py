from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

chrome_options = ChromeOptions()
chrome_options.add_extension("adblock.crx")


path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path, options=chrome_options)


driver.get("https://www.investing.com/stock-screener/")

driver.maximize_window()

driver.switch_to.window(driver.window_handles[0])  

# counter = 0
# while True:

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # element = WebDriverWait(driver, 60).until(
        # EC.presence_of_element_located((By.ID, "maisVagas"))
    # )
    # element.click()
    
    # time.sleep(1)



    
    

    
