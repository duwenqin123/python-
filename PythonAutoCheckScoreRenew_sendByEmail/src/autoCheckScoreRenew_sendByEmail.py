# -*- coding:utf-8 -*-
import os,datetime,time
import smtplib,pyperclip
from email.mime.text import MIMEText
from email.header import Header
from pyautogui import press
from selenium import webdriver
chromepath=os.path.abspath("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser=webdriver.Chrome(chromepath)
browser.get('http://219.219.120.48/jiaowu/exit.do?type=student')
id='141070036'
password='141070036'
fileObj=open('oldScore.txt')
oldMessage=fileObj.read()
fileObj.close()
userElem=browser.find_element_by_css_selector('input[name="userName"]')
userElem.clear()
userElem.send_keys(id)
pwdElem=browser.find_element_by_css_selector('input[type="password"]')
pwdElem.send_keys(id)
pwdElem.submit()
personElem=browser.find_element_by_css_selector('#studentinfo a')
personElem.click()
scoreElems=browser.find_elements_by_css_selector('#Function a')
scoreElems[1].click()
msgElem=browser.find_element_by_class_name('TABLE_BODY')
newMessage=msgElem.text
if newMessage!=oldMessage:
    fileObj=open('oldScore.txt','w')
#     fileObj.write(newMessage)
    fileObj.close()
    
    fromAddr='1950490691@qq.com'
    toAddr='18260099362@139.com'
    message=MIMEText(newMessage,'plain','utf-8')
    message['Subject']=Header(newMessage,'utf-8')
    server=smtplib.SMTP_SSL('smtp.qq.com',465)
    server.login(fromAddr,'iduqkmyvesmxbigi')
    server.sendmail(fromAddr, toAddr, message.as_string())
    server.quit()
    browser.quit()
print('Done')