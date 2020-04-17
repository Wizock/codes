#def fibb(n):
#    a = 0
#    b = 1
#
#    for i in range(n):
#        c = a+b
#        a = b
#        b = c + a
#        print(str(a)+":"+":"+str(c))
#
#fibb(25)
import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

#function to get corona info

res = requests.get("https://www.worldometers.info/coronavirus/").text
soup = BeautifulSoup(res,'html-parser')
soup.encode('utf-8')
cases = soup.find("div", {"class": "maincounter-number"}).get_text().strip()

#function for notification

def notifyMe(title,message):
    notification.notify(
        title = title,
        mesasge = message,
        timeout = 5)
while True:
    notifyMe('total number of cases',cases)
    time.sleep(10)
