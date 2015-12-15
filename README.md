# Bandwidth Monitor

This simple script accesses the data usage stats from Netgear routers (via page scraping), and displays it to the terminal. It was designed to make this process a lot easier.

To use this, you will need to enable Traffic Meter on your Netgear router.

*I make no guarantee this will work on all Netgear routers.* I've only tested it on the WNDR3700 series. This application is designed to work with stock Netgear firmware, from all routers 2012 and onward. If you are using DD-WRT/Tomato/Monowall/Etc, or another brand of router, then stop reading and find something that will work with that brand of router.

## Requirements
Python 2.6 (or better) and virtualenv is all you need. Request and BeautifulSoup are installed as dependencies.

## Installation
1. Clone this Git Repo
2. `mkdir .venv`
3. `virtualenv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`

To use run the command as `python bwmoni.py {username} {password}` or if you want to have a command you can link to /usr/local, chmod +x and use `bwmonitor.sh {username} {password}`.

## Possible issues
It may occassionaly return a "list index out of range" error. If this occurs, try again. A race condition could be the cause that unfortunately, is beyond my control (it originates on the router during BasicAuth). Should it repeatedly occur, check your authentication settings to be sure they are correct.

The script may produce additional issues if anything besides a 200 OK is retrieved. The most common cause of this is insufficient/incorrect authentication credentials.

## Enhancements
The script is feature-complete as far as I am concerned. If you feel like you can enhance it, or want to use it as a basis for a fork for other stock routers/SNMP protocol support, feel free to fork it. Pull Requests will more than likely be ignored.

## License
Licensed under MIT. See LICENSE.md
