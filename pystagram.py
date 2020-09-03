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

# アカウント・パスワード
insta_id = "piyo_univ_html.css"
insta_password = "gobugobu0131"

#タグ・各々いいねする数
hash_tags = ["プログラミング","プログラミング初心者","プログラミング学習","プログラミング勉強中","プログラミング入門"]
like_amount = 30
scroll_cnt = 6
search_cnt = 0

driver = webdriver.Chrome("c:/driver/chromedriver.exe")

def scroll(cnt):
    i=0
    while cnt > i:
        pyautogui.hotkey('End')
        driver.implicitly_wait(7)
        sleep(3)
        i += 1;

def access(hash_tag):
    driver.get("https://www.instagram.com/accounts/login/")
    driver.implicitly_wait(10)
    sleep(random.randint(1, 5))

    # ログインID・PWを入力
    elem_search_word = driver.find_element_by_name("username")
    elem_search_word.send_keys(insta_id)
    sleep(random.randint(1, 2))
    password = driver.find_element_by_name('password')
    password.send_keys(insta_password)
    sleep(random.randint(1, 2))
    password.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    sleep(7)
    # ２段階認証の保存を選択
    elem_search_word = driver.find_element_by_css_selector("button.sqdOP").click()
    driver.implicitly_wait(5)
    sleep(7)

    # ポップアップの後でを選択
    elem_search_word = driver.find_element_by_css_selector("button.aOOlW").click()
    driver.implicitly_wait(2)
    sleep(7)

    # 検索窓をアドレスバーに直接入力
    driver.get(f'https://www.instagram.com/explore/tags/{hash_tag}/')
    driver.implicitly_wait(6)
    sleep(7)

def good():
    driver.find_element_by_xpath(
        "//article/div[1]/div[1]/div[1]/div[1]/div[1]/a").click()
    sleep(random.randint(1, 10))  # エラーになるまでいいねしつづける
    like_count = 0
    while (like_count < like_amount):
        try:
            # いいね判定
            sleep(random.randint(1, 10))
            driver.find_element_by_css_selector("[aria-label=「いいね！」を取り消す]")
            sleep(random.randint(1, 10))
            # いいねされていたらパス
            print("いいね済み、パス")
            driver.find_element_by_css_selector(
                "a.coreSpriteRightPaginationArrow").click()
            sleep(random.randint(1, 10))
        except:
            # いいねする
            driver.find_element_by_css_selector("span.fr66n").click()
            like_count += 1
            sleep(random.randint(1, 10))
            print(like_count)
            print("いいね！")
            driver.find_element_by_css_selector(
                "a.coreSpriteRightPaginationArrow").click()
            sleep(random.randint(1, 10))
            pass
    print(like_count)
    print("いいねしました！")
    like_count = 0
    search_cnt+=1;

for hash_tag in hash_tags:
    access(hash_tag)
    scroll(scroll_cnt)
    good()
    driver.close()



