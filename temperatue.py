from bs4 import BeautifulSoup
import requests,sys,webbrowser    

str="temperature"
str+="+"+sys.argv[1]
print "Getting Temperature....."
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
}

res = requests.get('http://google.com/search?q=%s'%str,headers=headers)
res.raise_for_status()
examplesoup= BeautifulSoup(res.text,"lxml")    
linkelems=examplesoup.findAll("span",{"id":"wob_tm"})
print "Temperature in "+sys.argv[1]+" is "+linkelems[0].getText()+"C"
