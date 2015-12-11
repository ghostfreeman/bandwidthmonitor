# Bandwidth Monitor

This simple script accesses the data usage stats from Netgear routers, and displays it to the terminal. It was designed to make this process a lot easier.

To use this, you will need to enable Traffic Meter on your Netgear router.

## Requirements
Python 2.6 (or better) and virtualenv is all you need.

## Installation
1. Clone this Git Repo
2. `mkdir .venv`
3. `virtualenv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`

To use run the command as `python bwmoni.py {username} {password}`

## License
Licensed under MIT. See LICENSE.md
