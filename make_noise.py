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

#indefinte loop to visit random website and stay on the page for a random amount of time

while(1):
    driver.get("http://www.uroulette.com/visit/oqroon")
    print "currently on site:" + driver.current_url
    time.sleep(randint(0,7))
