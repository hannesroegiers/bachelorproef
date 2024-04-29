from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def web_scrape(url):
    options = Options()
    options.add_argument("--enable-performance-logging")
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    log = driver.get_log("performance")
    driver.quit()
    
    return log
    

url = "https://www.javatpoint.com/"
scraped = web_scrape(url)
with open("network_dump.txt", 'w') as f:
    for i in scraped:
        print(f"\n{i}")
        f.write(i)
    f.close()
print(scraped)

