#!/usr/bin/python
import urllib,urllib2
from BeautifulSoup import BeautifulSoup 
url = 'http://www.glidenumber.net/glide/public/search/search.jsp'
parameters = {'maxhits' : '25','X_Resolution' : '1440','sortby': '0','process':'0','posted':'0','nStart':'25', 'level0': '*','level1': '*','ftoption': '&','events':'*'} 
data = urllib.urlencode(parameters)    # Use urllib to encode the parameters
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)    # This request is sent in HTTP POST
page = response.read()
soup = BeautifulSoup(page)
mydata = soup.findAll("td", {"class" : "basefontSmall"})

#print mydata
#links = soup.findAll("a", {"class" : "bluelinks"})
counter = 0
while counter < 103 :
     start = mydata[counter].string
     print start
     counter = counter + 1

#print page
