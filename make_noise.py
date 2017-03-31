#necassary imports
import os
import platform
import time
from random import randint
from selenium import webdriver

print "Generating some random trafific...."


#setting up driver to simulate user and also start chrome in background
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")

#choosing chrome driver based on OS
if 'Linux' in (platform.system()):
    driver = webdriver.Chrome(os.getcwd()+'/chromedriver_linux',chrome_options=chrome_options)
elif 'Windows' in (platform.system()):
    driver = webdriver.Chrome(os.getcwd()+'/chromedriver.exe',chrome_options=chrome_options)
elif 'Darwin' in (platform.system()):
    driver = webdriver.Chrome(os.getcwd()+'/chromedriver_mac',chrome_options=chrome_options)

linklist = []
#indefinte loop to visit random website and stay on the page for a random amount of time
print '''Please select which of these sites you visit most often (choose all that is applicable)
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
    time.sleep(randint(5,20))
    print "currently on site: " + driver.current_url

while(1):
    if '1' in linklist:
        randomreddit()
