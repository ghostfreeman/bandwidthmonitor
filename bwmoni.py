#!/usr/bin/env python
import requests
import bs4
import sys

total = len(sys.argv)

if total == 3:
  response = requests.get('http://routerlogin.net/traffic_stattbl.htm', auth=(sys.argv[1], sys.argv[2]))
  soup = bs4.BeautifulSoup(response.text, "html.parser")

  # Pull out the data showing data used this month
  bandwidth = soup.select("td[width=85]")[1]
  bwstr = bandwidth.contents[0]
  bwMeg = int(bwstr.split("/")[0])
  bwGig = round((bwMeg / 1024), 2)

  response2 = requests.get("http://routerlogin.net/traffic_meter.htm", auth=(sys.argv[1], sys.argv[2]))
  soup2 = bs4.BeautifulSoup(response2.text, "html.parser")
  #import pdb; pdb.set_trace()
  bwToday = soup2.select("td[width=17%] p")[3]
  bwTodayCont = bwToday.contents[0]

  print "Total amount of bandwidth used this month: "+str(bwGig)+" GB ("+str(bwMeg)+" MBytes)"
  print "Total used today: "+str(bwTodayCont)+" MBytes"
else:
  print "Insufficient arguments. See README.md"
