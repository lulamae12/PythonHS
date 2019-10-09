import requests
from bs4 import BeautifulSoup
from soupMaker import soupGen
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Skynet():
    def __init__(self):
        print("test")
        self.skywardLoginUrl ="https://skyward.wcs.edu/scripts/wsisa.dll/WService=wsEAplus/seplog01.w"
        self.login("hi","hi2")
        self.driver = webdriver.Chrome()

    def login(self,user,passWord):
        loginPageSoup = soupGen(self.skywardLoginUrl)
        print(loginPageSoup)
        loginDomain = loginPageSoup.find(id = "loginDistrict")

        userLoginElem = self.driver.find_element_by_id("loginBody")
    
        print(loginDomain)
        print(userLoginElem)




test = Skynet()