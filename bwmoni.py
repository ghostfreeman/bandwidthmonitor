#!/usr/bin/env python
import requests
import bs4
import sys

total = len(sys.argv)

if total == 3:
  response = requests.get('http://routerlogin.net/traffic_stattbl.htm', auth=(sys.argv[1], sys.argv[2]));
  soup = bs4.BeautifulSoup(response.text, "html.parser");

  # Pull out the data showing data used this month
  bandwidth = soup.select("td[width=85]")[1]
  bwstr = bandwidth.contents[0]
  print "Total amount of bandwidth used this month: "+bwstr.split("/")[0]+" MBytes."
else:
  print "Insufficient arguments. See README.md"
