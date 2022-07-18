import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib import request
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urljoin
url1= "https://www.digitalwhisper.co.il"
l=[]
names=[]
parser = 'html.parser'
resp = urllib.request.urlopen(url1)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
for link in soup.find_all('a', href=True):
    l.append(link['href'])
print(l)
#check if pages in web is return 200
ok=[]
for i in range(0,200):
    c="https://www.digitalwhisper.co.il/issue"+str(i)
    p=requests.get(c)
    z=p.status_code
    if z == 200:
        ok.append(c)

for i in ok:
    url = i

#If there is no such folder, the script will create one automatically
    folder_location = r'c:\webscraping'
    if not os.path.exists(folder_location):os.mkdir(folder_location)

    response = requests.get(url)
    soup= BeautifulSoup(response.text, "html.parser")
    for link in soup.select("a[href$='.pdf']"):
    #Name the pdf files using the last portion of each link which are unique in this case
        filename = os.path.join(folder_location,link['href'].split('/')[-1])
        with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,link['href'])).content)