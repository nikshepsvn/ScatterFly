# Scatterly
[Previously PyNoise]

What is Scatterly?

Scatterly is a simple script written in Python that runs in the background visiting random websites for you.

Why would I want that?

On March 29th congress passed a law that makes it legal for your Internet Service Providers (ISP) to track and sell your personal activity online. This means that things you search for, buy, read, and say can be collected by corporations and used against you. Scatterly contaminates your data with the random websites it visits to make it harder for them to analyze your data.
source : https://www.govtrack.us/congress/votes/115-2017/h202

### How do I use it?

1. Clone the repo
2. install the only dependency, selenium (pip install selenium)
3. run the script (`python make_noise.py`) when you start browsing the internet
4. close the window when your done

### Headless (Raspberry Pi!)

If you would like to run this project on a Linux server (like a Raspberry Pi) there are a few additional steps:  
```bash
$ sudo apt-get install firefox-esr  # chrome/chromedriver doesn't support RPi
$ sudo apt-get install Xvfb         # virtual display server for selenium to connect to
$ Xvfb :99 -ac &                    # run a virtual display on port 99
$ export DISPLAY=:99                # set the display environment variable
$ python make_noise.py              # make some noise!
```

Feel free to email me @ nikshepsvn@gmail.com if you have some feedback/suggestions!

![Scatterly Running](https://i.imgur.com/jF82ACF.png "Scatterly Running")

Current Version V0.03
- V0.03 Changelog : added RPi (Firefox) support
- V0.02 Changelog : added feature for bot to create noise on reddit -- making info from reddit harder to analyze.
- V0.01 Changelog : First version of bot, Uses WPI's random link generator to visit random sites on the internet.

Scatterly was inspired by : https://slifty.github.io/internet_noise/index.html
----------------------------------------------------------------------------------------

The difference between the above project and Scatterly is that Scatterly can be launched from your terminal and runs in the background meaning it doesnt open up a browser window or new tabs -- so it doesn't distract you from work or confuse you while it's running. Scatterly also randomizes the time of each visit, so it's harder to differentiate the traffic.


###TODO:
1) Use DeepLearning to generate User Profile.
2) Make Scatterly Hook up to existing browser instance.
3) Finish other common site randomizers.
