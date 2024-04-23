from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def web_scrape(url):
    options = Options()
    options.add_argument("--enable-performance-logging")
    # options.set_preference("profiling.enable_additional_profiling_types", True)
    # options.set_preference("profiling.logging_prefs.performance", "ALL")
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    #service = Service(executable_path='C:\geckodriver.exe')
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    log = driver.get_log("performance")
    driver.quit()
    
    return log
    
# url = "https://www.oddsportal.com/football/belgium/jupiler-pro-league/"
url = "https://www.javatpoint.com/"
scraped = web_scrape(url)
# print(f"scraped title: {scraped}")
# print(f"scraped log: {scraped}")
print(scraped)

