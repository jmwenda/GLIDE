#!/usr/bin/python
import urllib,urllib2
from BeautifulSoup import BeautifulSoup 
import codecs
url = 'http://www.glidenumber.net/glide/public/search/search.jsp'
parameters = {'maxhits' : '25','X_Resolution' : '1440','sortby': '0','process':'0','posted':'0','nStart':'0', 'level0': '*','level1': '*','ftoption': '&','events':'*'} 
data = urllib.urlencode(parameters)    # Use urllib to encode the parameters
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)    # This request is sent in HTTP POST
page = response.read()
soup = BeautifulSoup(page)
table = soup.find( "table", {"border":"1", "width":"100%", "cellspacing":"1", "cellpadding":"1"} )
records=[]
for row in table.findAll('tr'):
	col = row.findAll("td", {"class" : "basefontSmall"})
        for td in col:
		td.find(text=True)

                
