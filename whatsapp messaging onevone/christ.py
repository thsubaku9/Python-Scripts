import os
import time
import pyautogui
from selenium import webdriver as wb
os.chdir('C:\\Users\\MAHE\\Desktop')

namels=list()
finalls=list()
genericmsg="Merry Christmas "
m1=wb.Chrome()      #edit this based on your browser type
m1.get('https://web.whatsapp.com/')
time.sleep(3)       #just waiting
#searching part
e2=m1.find_elements_by_class_name('rAUz7'); e2=e2[1]
e2.click()
vv=m1.find_elements_by_class_name('chat-title')
vv[0].click()

for j in range(1,9):
    xx=m1.find_elements_by_class_name('chat-title')
    for i in xx:
        ee=i.find_element_by_class_name('emojitext')
        namels+=[ee.get_attribute('title')]
        pyautogui.scroll(500)       #site is dynamic in nature
        
#rectifying part

namels.sort()
temp=''
for i in range(0,len(namels)-1):
    if(namels[i]!=namels[i+1] and namels[i]!=temp):
        finalls+=[namels[i]]
    elif(namels[i]==namels[i+1] and namels[i]!=temp):
        finalls+=[namels[i]]
        temp=namels[i]
        
#sending part
for name in finalls:
    ele=m1.find_element_by_xpath('//span[contains(text(),'+name+')]')
    ele.click()
    time.sleep(0.5)
    el1=m1.find_element_by_class_name('pluggable-input-body')
    gg=genericmsg+name
    el1.send_keys(gg)
    m1.find_element_by_class_name('compose-btn-send').click()
    time.sleep(0.5)
#done part 
    




