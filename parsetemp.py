from bs4 import BeautifulSoup
import requests,sys,webbrowser
l=len(sys.argv[1:])

str="+".join(sys.argv[1:l])
res = requests.get('http://google.com/search?q=%s'%str)
res.raise_for_status()
examplesoup= BeautifulSoup(res.text,"lxml")
linkelems=examplesoup.findAll("h3",{"class":"r"})
for i in range(int(sys.argv[l])):
	webbrowser.open('http://google.com' + linkelems[i].a.get('href'))



