###
#Leo Zeng
#may 28 210019
#citation automate
#a program to automate using citation machine
#this webcite seems to load inconsistant, im putting 3 seconds wait time for each action,
#and repeating the action. also, some webcites eg.qoura doesn't work
#paste all webcites on "list_of_webcites.txt" file to work
###



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time


#opens citation webcite
#options = webdriver.ChromeOptions()
#options.binary_location = "E:/applications/Google/Chrome/Application/chrome.exe"
#chrome_driver_binary = "F:/seleniumchromedriver/chromedriver.exe"
#driver = webdriver.Chrome(chrome_driver_binary, options=options)
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome("E:/applications/Google/Chrome/Application/chrome.exe")

driver = webdriver.Chrome()
driver.get("http://www.citationmachine.net/mla/cite-a-website")

file1 = open("list_of_webcites.txt","r")
f1 = file1.readlines()

for lineNum in f1:

    link = lineNum
    print(lineNum)

    #inputs url
    try:
        url = driver.find_element_by_name("q")
        url.send_keys(link)
    except:
        pass
    try:
        url = driver.find_element_by_name("q")
        url.send_keys(link)
    except:
        pass
    driver.implicitly_wait(100)

    #search webcite

    try:
        search = driver.find_element_by_class_name("search-button")
        search.click()
    except:
        pass
    try:
        search = driver.find_element_by_class_name("search-button")
        search.click()
    except:
        pass
    driver.implicitly_wait(100)


    #select
    try:
        select = driver.find_element_by_class_name("select-result")
        select.click()
    except:
        pass
    try:
        select = driver.find_element_by_class_name("select-result")
        select.click()
    except:
        pass
    driver.implicitly_wait(100)

    #final step
    try:
        finalStep = driver.find_element_by_class_name("continue")
        finalStep.click()
    except:
        pass
    try:
        finalStep = driver.find_element_by_class_name("continue")
        finalStep.click()
    except:
        pass
    driver.implicitly_wait(100)

    #create citation
    try:
        create = driver.find_element_by_class_name("btn-citation")
        create.click()
    except:
        pass
    try:
        create = driver.find_element_by_class_name("btn-citation")
        create.click()
    except:
        pass
    driver.implicitly_wait(100)


    #create another citation
    try:
        another = driver.find_element_by_class_name("bab")
        another.click()
    except:
        pass
    try:
        another = driver.find_element_by_class_name("bab")
        another.click()
    except:
        pass
    driver.implicitly_wait(100)

#your biblography has 2 citations in it.
try:
    bibliography = driver.find_element_by_id("bibliography-title-text")
    bibliography.click()
except:
    pass
try:
    bibliography = driver.find_element_by_id("bibliography-title-text")
    bibliography.click()
except:
    pass



print("finish")



