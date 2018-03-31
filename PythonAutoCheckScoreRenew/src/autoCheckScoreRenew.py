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
    fileObj.write(newMessage)
    fileObj.close()
    pyperclip.copy(newMessage)
    
    browser.get('http://mail.10086.cn')
    account=browser.find_element_by_id('txtUser')
    account.send_keys('18260099362')
    pwd=browser.find_element_by_id('txtPass')
    pwd.send_keys('ZQQ910713')
    pwd.submit()
    browser.maximize_window()
    time.sleep(2)
    import pyautogui
#     msgPos=(258,444)
    msgPos=pyautogui.locateCenterOnScreen('msg.PNG')
    pyautogui.click(msgPos)
    time.sleep(3)
#     mobilephonePos=(297,240)
    mobilephonePos=pyautogui.locateCenterOnScreen('mobile.PNG')
    pyautogui.click(mobilephonePos)
    pyautogui.typewrite('18260099362')
#     messagePos=(234,314)
#     messagePos=pyautogui.locateCenterOnScreen('sendMsg.PNG')
#     if pyautogui.locateOnScreen('sendMsg.PNG')!=None:
    pyautogui.press('enter')
    pyautogui.moveRel(0,100)
    pyautogui.click()
    pyautogui.hotkey('ctrl','v')
#     sendPos=(220,686)
    sendPos=pyautogui.locateCenterOnScreen('send.PNG')
    pyautogui.click(sendPos)
#     conformPos=(903,551)
#     sendElem=browser.find_element_by_class_name('icoG.btnSure.MB_But_0.YesButton')
    time.sleep(2)
    conformPos=pyautogui.locateCenterOnScreen('conform.PNG')
    pyautogui.click(conformPos)
print('Done')


