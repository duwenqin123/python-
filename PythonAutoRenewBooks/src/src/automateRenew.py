# -*- coding=utf-8 -*-
import os,datetime,time
from selenium import webdriver

chromepath=os.path.abspath("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser=webdriver.Chrome(chromepath)
browser.get('http://book.njulib.cn/')
time.sleep(3)
account=browser.find_element_by_id('user_id')
account.send_keys('141070010')
pwd=browser.find_element_by_id('user_pwd')
pwd.send_keys('141070010')
login=browser.find_element_by_id('in_buttom')
login.click()
# elem=browser.find_element_by_css_selector('a[href="book_lst.php"]')
# elem.click()
time.sleep(5)
books=browser.find_elements_by_class_name('home_right_book_ul')
lenOfBooks=len(books)
print(lenOfBooks)
for i in range(lenOfBooks):
    index=books[i].text.find('应还日期')+5
    returnDay=books[i].text[index:index+10]
    returnTime=datetime.datetime.strptime(returnDay,'%Y-%m-%d')
    nowTime=datetime.datetime.now()
    print(nowTime,returnTime)
    numberOfDays=(returnTime-nowTime).days
    print(numberOfDays)
    if  numberOfDays<=2:
        renewElems=browser.find_elements_by_css_selecto('input.btn.btn-success')
        renewElems[i].click()
# browser.quit()
