#selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

#options.add_argument('--user-data-dir=C:/Users/James/AppData/Local/Google/Chrome/User Data')
#options.add_argument('--profile-directory=Profile 2')

options.add_argument("--profile-directory=Profile 2")
options.add_argument("--user-data-dir=C:/Users/James/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#time.sleep(10)
#driver = webdriver.Chrome(options=options)

#driver = webdriver.Chrome()
driver.get("https://www.tiktok.com/search/video?q=glass%20rinser&t=1685614943172")
#driver.get("https://www.bbc.com")
driver.implicitly_wait(1) 
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#time.sleep(10)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#element = driver.find_elements(By.TAG_NAME, "h1")[0].text
#print(element)

#element1 = driver.find_element(By.CSS_SELECTOR, "div.tiktok-1s72ajp-DivWrapper e1cg0wnj1 > a").get_attribute('href') 
												    
#print(element1)

#element2 = driver.find_element(By.TAG_NAME, "body").text
#print(element2)

#element3 = driver.page_source
#print(element3)

#doom scrolling 
number = 50
iritiration = 0
html = driver.find_element(By.TAG_NAME,"html")

while iritiration <= number:
    html.send_keys(Keys.END)
    time.sleep(5)
    iritiration +=1
time.sleep(10)

# Solution works
element4 = driver.find_elements(By.CSS_SELECTOR,"div#main-content-search_video div.tiktok-1s72ajp-DivWrapper a")
#print(element4)
links = []
for e in element4:
    links.append(e.get_attribute("href"))
    #print(links)

for link in links:
    print(link)

#select = Select(element)
#select.all_selected_options
driver.close()


#%%
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import mechanicalsoup

#micanical soup 
browser = mechanicalsoup.StatefulBrowser()
#browser.open("https://www.tiktok.com/search/video?q=glass%20rinser&t=1685614943172")
#print(browser.page)
#browser.page()
#does not load relevant tags

#urllib
page = urlopen("https://www.tiktok.com/search/video?q=glass%20rinser&t=1685614943172")
#print(page)
#does not load relevant tags

#requests
r = requests.get("https://www.tiktok.com/search/video?q=glass%20rinser&t=1685614943172", auth=('user', 'pass'))
#cleprint(r)
#print(r.url)
#print(r.encoding)
#print(r.json)
#print(r.text)
#print(r.content)
#does not load relevant tags

#b4s
#soup = BeautifulSoup(page, 'html.parser')
#soup = BeautifulSoup(r.text, 'html.parser')
#soup = BeautifulSoup(r.content, 'html.parser')
#print(soup)
#print(soup.prettify())
#a = soup.find_all("div")
#for i in a:
#    print(i)

# h = r.headers
# print(h)
# %%
