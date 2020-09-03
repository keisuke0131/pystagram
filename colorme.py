from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib.parse
import time
from time import sleep
import pyautogui
import random

cnt=0
while cnt<100:
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("--incognito")
  driver = webdriver.Chrome("c:/driver/chromedriver.exe")
  driver.get("https://award.shop-pro.jp/2020?utf8=%E2%9C%93&keyword=%E3%82%91%E3%81%B3%E3%81%99%E8%B6%B3%E8%A2%8B")
  driver.implicitly_wait(10)
  elem_search_word = driver.find_element_by_css_selector("button.button").click()
  cnt+=1
  print(cnt)
  sleep(2)
  driver.close()






