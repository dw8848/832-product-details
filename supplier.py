import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import requests

'''平时怎么使用浏览器，代码逻辑就怎么写'''
driver = webdriver.Chrome()
driver.get('https://www.fupin832.com/pub_web.shtml?pgid=1030')
driver.implicitly_wait(10)  # 浏览器的隐式等待（弹性等待）-->死等
driver.maximize_window()  # 最大化浏览器

def next():
    driver.find_element(By.XPATH,'//*[@id="page_tool"]/a[6]').click()

sum_id = []
sum_name = []
sum_loation = []
sum_img = []

def get_id(j):
    time.sleep(5)
    path = driver.find_element(By.XPATH,'//*[@id="gongyingshang0'+str(j)+'"]/div[1]/a').get_attribute('onclick')
    path = path.strip("pubOnClick('")
    path = path.strip(",false,false)")
    path = path.strip("'")
    sum_id.append(path)
    name = driver.find_element(By.XPATH,'//*[@id="gongyingshang0'+str(j)+'"]/div[1]/a/div[2]/div[1]/span').text
    loation = driver.find_element(By.XPATH,'//*[@id="gongyingshang0'+str(j)+'"]/div[1]/a/div[2]/div[2]/span').text
    img_list = driver.find_element(By.XPATH,'//*[@id="gongyingshang0'+str(j)+'"]/div[1]/a/div[2]/div[3]/div[1]')
    img_sum = img_list.find_elements(By.TAG_NAME,'img')
    img = ''
    for i in img_sum:
        path = i.get_attribute('src')
        img += ' '+path
    print(name,loation,img)
    sum_name.append(name)
    sum_loation.append(loation)
    sum_img.append(img)

def main():
    for i in range(1):
        print(i)
        for j in range(5):
            try:
                get_id(j)
            except Exception as e:
                print('哦豁')
        next()

def parse_one_page(url):
    html = requests.get(url).text
    bf = BeautifulSoup(html)
    print(html)
    #name = bf('span',{'style':'font-size: 18px;color: #666666;'})
    #dengji = bf.find_all('td',class_ = 'y_detPrice')
    products = bf.find_all('div',class_ = 'y_shopItem')
    print(products)
    #for product in products:
        #name1 = product.find_all('span',class_ = 'show-all')
        #print(name1)

def parse_max_page():
    for i in range(len(sum_id)):

        try:
            new_url = f'https://www.fupin832.com'+sum_id[i]
            print(f'正在获取id:',i)

        except Exception as e:
            print('GG')
        parse_one_page(url=new_url)

main()
print(sum_id)
driver.quit()  # 关闭浏览器
parse_max_page()
