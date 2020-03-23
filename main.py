from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "D:\COVID 19 NOTIFICATION SYSTEM\coronavirus.ico",
        timeout = 10
        )

def getData(url):
    r = requests.get(url)
    return r.text



if __name__ == "__main__":
    while True:
    
        myHtmlData = getData("https://www.mohfw.gov.in/")
        
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        
        myDataStr = ''
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split('\n\n')

        states = ['Uttar Pradesh', 'Maharashtra', 'Telangana', 'Gujarat', 'Delhi']
        for item in itemList[:22]:
            dataList = item.split('\n')
            if dataList[1] in states:
                nTitle = 'Cases of COVID-19'
                nMessage = f"State: {dataList[1]} \n Indian: {dataList[2]}  Foreign: {dataList[3]} \n Cured: {dataList[4]}  Deaths: {dataList[5]}"
                notifyMe(nTitle, nMessage)
                time.sleep(2)
        time.sleep(3600)