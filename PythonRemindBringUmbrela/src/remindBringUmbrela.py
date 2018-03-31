# -*- coding:utf-8 -*-
import os,datetime,time
import bs4,requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from pyautogui import press

res=requests.get('http://tianqi.2345.com/nanjing/58238.htm')
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,'lxml')
elems=soup.select('.charact')
contents=elems[0].getText()
hasRain=('雨'in contents)
print(hasRain)
hasRain=True
if hasRain:
    from selenium import webdriver
    chromepath=os.path.abspath("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    browser=webdriver.Chrome(chromepath)
    browser.get('http://mail.10080.cn')
    browser.get('http://mail.10086.cn')
    account=browser.find_element_by_id('txtUser')
    account.send_keys('18260099362')
    pwd=browser.find_element_by_id('txtPass')
    pwd.send_keys('ZQQ910713')
    pwd.submit()
    browser.maximize_window()
    time.sleep(2)
    import pyautogui
    msgPos=(258,444)
    pyautogui.click(msgPos)
    time.sleep(3)
    mobilephonePos=(297,240)
    pyautogui.click(mobilephonePos)
    pyautogui.typewrite('18260099362')
    messagePos=(234,314)
    pyautogui.click(messagePos)
    pyautogui.typewrite('Has rain!Please bring umbrella')
    sendPos=(220,686)
    pyautogui.click(sendPos)
    pos=(903,551)
    pyautogui.click(pos)
print('Done')