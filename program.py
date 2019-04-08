# coding:utf-8

# shaji saki19941211@gmail.com
import time
import os
import sys
from selenium import webdriver

#vote_fromis
def vote():
    driver.get("http://mama.mwave.me/en/vote")
    for i in range(18):
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[1]').click()
            if(i == 1):
                driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[6]').click()
            elif(i == 17):
                driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[31]').click()
                time.sleep(90)
                break
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
            time.sleep(1)
        except:
            pass

#logout
def logout():
    try:
        driver.get("https://www.mwave.me/en/signin?redirectUrl=http://mama.mwave.me/en")
        driver.find_element_by_text('SIGN-OUT').click() #logout
        time.sleep(1)
    except:
        pass
    finally:
        driver.get("https://www.mwave.me/en/signin?redirectUrl=http://mama.mwave.me/en")


#read login_info from file
print("正在读取账号信息...")
login_info = {}
login_info_object = open("login_info.txt","r")
for i in range(6):
    key = login_info_object.readline().strip('\n') #type:string
    value = login_info_object.readline().strip('\n')
    login_info[key]=value
login_info_object.close()
print(login_info)

#open Chrome
driver = webdriver.Chrome(executable_path=(os.getcwd() + "/chromedriver.exe"))
driver.get("https://www.mwave.me/en/signin?redirectUrl=http://mama.mwave.me/en")
time.sleep(1)
logout()

#twitter
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[2]').click()
driver.find_element_by_id('username_or_email').click()
driver.find_element_by_id('username_or_email').send_keys(login_info["twitter_id"])
driver.find_element_by_id('password').click()
driver.find_element_by_id('password').send_keys(login_info["twitter_pw"])
driver.find_element_by_id('password').click()
driver.find_element_by_id('allow').click()
vote()
logout()

#facebook
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[5]').click()
driver.find_element_by_id('email').click()
driver.find_element_by_id('email').send_keys(login_info["facebook_id"])
driver.find_element_by_id('pass').click()
driver.find_element_by_id('pass').send_keys(login_info["facebook_pw"])
driver.find_element_by_id('password').click()
driver.find_element_by_id('loginbutton').click()
vote()
logout()

#weibo
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[7]').click()
driver.find_element_by_id('userID').click()
driver.find_element_by_id('userID').send_keys(login_info["weibo_id"])
driver.find_element_by_id('passwd').click()
driver.find_element_by_id('passwd').send_keys(login_info["weibo_pw"])
driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
vote()
logout()


'''
#google
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[7]').click()
driver.find_element_by_id('view_container').click()
driver.find_element_by_id('view_container').send_keys(username)
#
'''
