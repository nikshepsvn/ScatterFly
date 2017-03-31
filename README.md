# PyNoise

What is PyNoise?

PyNoise is a simple script written in Python that runs in the background visiting random websites for you.

Why would I want that?

On March 29th congress passed a law that makes it legal for your Internet Service Providers (ISP) to track and sell your personal activity online. This means that things you search for, buy, read, and say can be collected by corporations and used against you. PyNoise contaminates your data with the random websites it visits to make it harder for them to analyze your data.
source : https://www.govtrack.us/congress/votes/115-2017/h202

How do I use it?

1. Clone the repo
2. install the only dependency, selenium (pip install selenium)
3. run the script (python make_noise.py) when you start browsing the internet
4. close the window when your done

Feel free to email me @ nikshepsvn@gmail.com if you have some feedback/suggestions!

![PyNoise Running](https://i.imgur.com/jF82ACF.png "PyNoise Running")


----------------------------------------------------------------------------------------
PyNoise was inspired by : https://slifty.github.io/internet_noise/index.html
----------------------------------------------------------------------------------------

The difference between the above project and PyNoise is that pynoise can be launched from your terminal and runs in the background meaning it doesnt open up a browser window or new tabs -- so it doesn't distract you from work or confuse you while it's running. PyNoise also randomizes the time of each visit, so it's harder to differentiate the traffic.
