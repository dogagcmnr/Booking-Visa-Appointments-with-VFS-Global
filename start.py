import time
import xpaths
import password
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver_path = "C:\\Users\\Administrator\\Desktop\\vfs\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driver_path)

def login(xe,xpw,uid,upw):
    browser.get('https://online.vfsglobal.com/Global-Appointment/Account/RegisteredLogin')
    mail = browser.find_element_by_xpath(xe)
    pw = browser.find_element_by_xpath(xpw)
    mail.send_keys(uid)
    pw.send_keys(upw)
    time.sleep(10)
    appointment(xpaths.appointment,xpaths.selone)

def appointment(ax,sx):
    browser.find_element_by_xpath(ax).click()
    time.sleep(random.randint(3,5))
    selelement = Select(browser.find_element_by_xpath(sx))
    while True:
        selelement.select_by_visible_text('Poland Visa Application Center - Ankara')
        time.sleep(random.randint(3,5))
        selelement.select_by_visible_text('Poland Visa Application Center-Altunizade')
        time.sleep(random.randint(3,5))
        browser.find_element_by_xpath(ax).click()
        time.sleep(10)



login(xpaths.email, xpaths.password, password.userid, password.pw)