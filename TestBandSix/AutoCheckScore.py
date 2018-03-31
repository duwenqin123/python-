# -*- coding:utf-8 -*-
import os,time
from selenium import webdriver
chromepath=os.path.abspath("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser=webdriver.Chrome(chromepath)
browser.get('http://cet.99sushe.com/')
# id=320012162201501
id=320012162203401
firstId=id
# name=��������
count=0;
while id<320012162209990:
    count+=1
    if count==50:
        count=0
        firstId+=100
        id=firstId
        print('temp id:'+str(id))
    if id==320012162203412:
        id+=1
    try:
        userElem=browser.find_element_by_css_selector('input#id')
#     userElem.clear()
    except:
        continue
    userElem.send_keys(id)
    pwdElem=browser.find_element_by_css_selector('input#name')
    pwdElem.send_keys('XX')
    pwdElem.submit()
    try:
        saveElem=browser.find_element_by_css_selector('#score_result > div:nth-child(2) > a')
        browser.save_screenshot('temp'+str(id)+'.png')
        print(id)
        break
    except:
#         tempElem=browser.find_element_by_css_selector('input#btn')
        returnElem=browser.find_element_by_css_selector('input#btn')
        returnElem.click()
#         personElem=browser.find_element_by_css_selector('#studentinfo a')
#         personElem.click()
#         scoreElems=browser.find_elements_by_css_selector('#Function a')
#         scoreElems[1].click()
#         quitElems=browser.find_elements_by_css_selector('#TopLink a')
#         quitElems[1].click()
    id+=1
print('done')