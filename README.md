<p align="center">
  <img src = "https://i.imgur.com/4Jx3kyC.png" />
</p>

### What is ScatterFly?

ScatterFly is a program designed to make it harder for ISP's to sell or analyze your personal data by intelligently obfuscating it.

### Wait, ISP's can sell my personal data?

On March 29th the US congress passed a law that makes it legal for your Internet Service Providers (ISP) to track and sell your personal activity online. This means that things you search for, buy, read, and say can be collected by corporations and used against you. ScatterFly contaminates your data with the random websites it visits in an attempt to make it harder for them to analyze your data.
source : https://www.govtrack.us/congress/votes/115-2017/h202

### How do I use it?
```bash
1. download the latest release and extract files into a folder
2. install the dependencies (pip install -r requirements.txt)
3. run the script (python make_noise.py) when you start browsing the internet
4. ctrl + x or close the terminal window when you are finished
```
If you would like to run this project on a Linux server (like a Raspberry Pi) there are a few additional steps:  
```bash
$ sudo apt-get install firefox-esr  # chrome/chromedriver doesn't support RPi
$ sudo apt-get install Xvfb         # virtual display server for selenium to connect to
$ Xvfb :99 -ac &                    # run a virtual display on port 99
$ export DISPLAY=:99                # set the display environment variable
$ python make_noise.py              # make some noise!
```

<p align="center">
  <img src = "https://i.imgur.com/jF82ACF.png" />
  <br>   ScatterFly Running 
</p>

### Current Version V0.06
- V0.06 Changelog : major changes, added amazon, tumblr and youtube!
- V0.05 Changelog : code clean up and modularization
- V0.04 Changelog : added feature for bot to create noise on ebay -- making shopping data from ebay harder to analyze.
- V0.03 Changelog : added RPi (Firefox) support
- V0.02 Changelog : added feature for bot to create noise on reddit -- making info from reddit harder to analyze.
- V0.01 Changelog : First version of bot, Uses WPI's random link generator to visit random sites on the internet.

ScatterFly was inspired by : https://slifty.github.io/internet_noise/index.html

The difference between the above project and ScatterFly is that ScatterFly can be launched from your terminal and runs in the background meaning it doesnt open up a browser window or new tabs -- so it doesn't distract you from work or confuse you while it's running. ScatterFly also randomizes the time of each visit, so it's harder to differentiate the traffic.


### TODO:
1) Use DeepLearning to generate User Profile.
2) Make ScatterFly Hook up to existing browser instance.
3) Reduce and replace dependencies as much as possible (urlroullete and other 3rd party sites)
4) Click on all ads on any particular website to give more false leads
5) Add feature to Obfuscate torrent and tracker data as well! :O
6) Enable feature to track bandwith usage and time running.
7) Enable "DeepDive" feature for sites by clicking links within the same domain on a page

### DONE:
1̶)̶ ̶F̶i̶n̶i̶s̶h̶ ̶o̶t̶h̶e̶r̶ ̶c̶o̶m̶m̶o̶n̶ ̶s̶i̶t̶e̶ ̶r̶a̶n̶d̶o̶m̶i̶z̶e̶r̶s̶.̶ (currently only facebook, tumblr, amazon, ebay, youtube and reddit!)

### Feel free to email me @ nikshepsvn@gmail.com if you have some feedback/suggestions!
