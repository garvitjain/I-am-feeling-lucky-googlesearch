from bs4 import BeautifulSoup
import requests,sys,webbrowser
str="+".join(sys.argv[1:])
res = requests.get('http://google.com/search?q=%s'%str)
res.raise_for_status()
examplesoup= BeautifulSoup(res.text,"lxml")
linkelems=examplesoup.findAll("h3",{"class":"r"})
for i in range(4):
	webbrowser.open('http://google.com' + linkelems[i].a.get('href'))



