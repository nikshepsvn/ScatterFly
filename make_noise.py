#necassary imports
import os
import json
import urllib2
import platform
import time
from random import randint
from selenium import webdriver

print "Generating some random trafific...."


#setting up driver to simulate user and also start chrome in background
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")

#choosing chrome driver based on OS
if 'Linux' in (platform.system()):
    driver = webdriver.Chrome(os.getcwd()+'/chromedriver_linux',chrome_options=chrome_options)
elif 'Windows' in (platform.system()):
    driver = webdriver.Chrome(os.getcwd()+'/chromedriver.exe',chrome_options=chrome_options)
elif 'Darwin' in (platform.system()):
    driver = webdriver.Chrome(os.getcwd()+'/chromedriver_mac',chrome_options=chrome_options)

linklist = []
#indefinte loop to visit random website and stay on the page for a random amount of time
print '''Please select which of these sites you visit most often (choose all that is applicable) :
1. Reddit
2. Facebook
3. YouTube
4. Tumblr
5. Amazon
6. Ebay'''


while(1):
    x = raw_input()
    if (x != "S"):
        linklist.append(x)
    else:
        print "You have succesfully entered " + (str(len(linklist))) + " sites."
        break;

def randomsite():
        driver.get("http://www.uroulette.com/visit/oqvsoq")
        time.sleep(randint(0,7))
        print "currently on site: " + driver.current_url

def randomreddit():
    driver.get("http://reddit.com/r/random")
    url = driver.current_url+"top/.json?count=10"
    req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
    jsonposts = json.loads(urllib2.urlopen(req).read())
    leng = len(jsonposts['data']['children'])
    for i in range(0,leng):
        driver.get("http://reddit.com"+jsonposts['data']['children'][i]['data']['permalink'])
        print "currently on site: " + driver.current_url
        time.sleep(randint(0,5))
    print "currently on site: " + driver.current_url
    time.sleep(randint(0,4))

while(1):
    if '1' in linklist:
        randomreddit()
