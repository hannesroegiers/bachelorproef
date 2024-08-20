import time
t0 = time.time()

import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

url = "https://www.oddsportal.com/football/belgium/jupiler-pro-league/"
driver = webdriver.Chrome(options=options)
driver.get(url)
performance_logs = driver.get_log("performance")
driver.quit()

t1 = time.time()

url = "https://www.oddsportal.com/football/belgium/jupiler-pro-league/"

filtered_logs = []
filter_list = ["Network.request", "Network.response"]

for entry in performance_logs:
    networktraffic = json.loads(entry["message"])["message"]
    if any(keyword in networktraffic["method"] for keyword in filter_list):
        filtered_logs.append(networktraffic)

urls = []
for log in filtered_logs:
    try:
        if(log["params"]["type"] == 'XHR'):
            url = log["params"]["request"]["url"]
            urls.append(url)
    except:
        pass

filter_list = [".svg", ".png", "/js/", ".js", ".css", ".ico"]
filtered_urls = [url for url in urls if not any(filter_str in url for filter_str in filter_list)]

for url in filtered_urls:
    print(url)
    
t2 = time.time()


import re

def check_url_contents(url, words=None, regex_patterns: list=None):

    headers = { 
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    
    results = {'words': {}, 'regex_patterns': {}}
    
    if response.status_code == 200:
        content = response.text
        
        if words:
            for word in words:
                count = content.lower().count(word.lower())
                results['words'][word] = count
                
        if regex_patterns:
            for regex in regex_patterns:
                pattern = re.compile(regex)
                matches = pattern.findall(content)
                results['regex_patterns'][regex] = len(matches)
                
    return results

def rank_urls(urls, words=None, regex_patterns=None):
    url_scores = {}
    for url in urls:
        restults = check_url_contents(url, words,regex_patterns)
        score=0
        if words:
            score+= sum(restults['words'].values())
        if regex_patterns:
            score+= sum(restults['regex_patterns'].values())
        url_scores[url] = score
        
    sorted_urls = sorted(url_scores.items(), key=lambda x:x[1], reverse=True)
        
    return sorted_urls
        


result = rank_urls(filtered_urls, ['odd', 'bet', 'average', 'avg'])

for index, entry in enumerate(result, start=1):
        if entry[1] < 1:
            break
        print(f"{index}: {entry[0]}")
t3 = time.time()

section1 = t1-t0
section2 = t2-t1
section3 = t3-t2
total = t3-t0

data = [
    [section1,section2,section3,total]
]

import os
import csv

file = "times2.csv"
file_exists = os.path.isfile(file)
with open(file, 'a' ,newline='') as file:
    writer = csv.writer(file)
    # Write the header only if the file does not exist
    if not file_exists:
        writer.writerow(["Section 1", "Section 2", "Section 3", "Total"])
    
    # Write the data row
    writer.writerows(data)
