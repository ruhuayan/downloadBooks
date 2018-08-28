#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import pdfkit

browser = webdriver.Firefox()
browser.get("http://www.banq.qc.ca/accueil/") 
print "wait..."
time.sleep(5)
browser.get("https://www.banq.qc.ca/mon_dossier/mon_dossier.html")
print 'wait..'
time.sleep(2)
username = browser.find_element_by_id("NUM")
password = browser.find_element_by_id("PWD")
username.send_keys("username")
password.send_keys("password")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
time.sleep(3)
browser.get("http://iris.banq.qc.ca/alswww2.dll/APS_ZONES?fn=ViewNotice&q=0005485153")
time.sleep(3)
browser.get("http://res.banq.qc.ca/login?url=http://US2KV5PK3N.search.serialssolutions.com/?V=1.0&L=US2KV5PK3N&S=AC_T_B&C=Natural%20Language%20Processing%3A%20Python%20and%20NLTK&T=marc&tab=BOOKS")
time.sleep(5)
browser.find_element_by_css_selector('a[title=\"J\'accepte\"]').click()   #second time may not work
browser.get("http://us2kv5pk3n.search.serialssolutions.com.res.banq.qc.ca/log?L=US2KV5PK3N&D=6XM&J=TC0001830192&P=EJP&PT=EZProxy&U=http%3A%2F%2Fres.banq.qc.ca%2Flogin%3Furl%3Dhttp%3A%2F%2Fproquestcombo.safaribooksonline.com%2F9781787285101")
#browser.find_element_by_css_selector('a[class=\"SS_JournalHyperLink\"]').click() #first time

browser.get("http://proquestcombo.safaribooksonline.com.res.banq.qc.ca/book/programming/python/9781787285101/natural-language-processing-python-and-nltk/index_html#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE3ODcyODUxMDElMkZjaDAwbHZsMXNlYzAxX2h0bWwmcXVlcnk9")

html = ""
#pageNum=1

#while True:
for x in range(10):
	print "page: %d"%x
	#pageNum+=1
	print "navigating ..."
	time.sleep(3)
	try:
		page = browser.find_element_by_id("page")
		html += page.get_attribute("innerHTML")
		nextPage = browser.find_element_by_id("next")
		nextPage.click()
	except:
		break	
pdfkit.from_string(html, "test.pdf")


