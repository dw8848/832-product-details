import csv
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

'''平时怎么使用浏览器，代码逻辑就怎么写'''
driver = webdriver.Chrome()
driver.get('https://www.fupin832.com/webpage/guid/html/optimization.html?nid=1023&city_no=51')
driver.implicitly_wait(10)  # 浏览器的隐式等待（弹性等待）-->死等
driver.maximize_window()  # 最大化浏览器

sum_id = []

def get_id():
    time.sleep(5)
    id_list = driver.find_element(By.XPATH,'//*[@id="prductList"]')
    id_sum = id_list.find_elements(By.TAG_NAME,'p')
    for id in id_sum:
        path = id.find_element(By.TAG_NAME,'img').get_attribute('order')
        sum_id.append(path)


def next0():
    driver.find_element(By.XPATH,'//*[@id="s_pages"]/a[7]').click()

def next1():
    driver.find_element(By.XPATH,'//*[@id="s_pages"]/a[8]').click()

def next2():
    driver.find_element(By.XPATH,'//*[@id="s_pages"]/a[9]').click()

def main():
    for i in range(335):
        print(i)
        try:
            get_id()
            if i == 0:
                next0()
            elif i == 1 or i == 2:
                next1()
            else:
                next2()
        except Exception as e:
            print('哦豁')

def parse_one_page(url):
    html = requests.get(url).text
    bf = BeautifulSoup(html)
    name = bf('span',{'style':'display: inline'})
    price = bf.find('td',class_ = 'y_detPrice')
    liang = bf.find('td',class_ = 'y_batch')
    one_prices = bf.find('td',class_ = 'y_detPrice unit-price')
    one_price = one_prices.find('span')
    shipping_location = bf('span',{'style':'margin-left: 20px;'})
    residue = bf('span',{'id':'surplus_box'})

    company = bf('span', {'style':'width:167px;height: 45px;float:left;margin-top:6px;line-height:22px;margin-left:10px;display: -webkit-box;-webkit-box-orient: vertical;-webkit-line-clamp: 2;overflow: hidden;'})
    location = bf.find('span',class_ = 'y_shopAdress')
    img_list = bf.find('ul',class_ = 'shop_cShopInfoBox')
    sum_img = ''
    for img_sum in img_list.find_all('li'):
        for paths in img_sum.find_all('img'):
            path = paths['src']
            sum_img = sum_img+' '+path

    xuke = bf.find_all('div',class_ = 'col-xs-5 padd0 hidden_food')
    changdi = bf.find_all('div',class_ = 'col-xs-4 padd0')
    try:
        xt = changdi[2].text
        zz = changdi[3].text
        zl = changdi[4].text
    except Exception as e:
        xt = '无'
        zz = '无'
        zl = '无'

    commnets = bf.find('p',class_ = 'y_scoreStar')
    commnet = commnets.find_all('span')
    commnet_sum = bf.find('ul',class_ = 'y_estListUl')
    sum_commnet = commnet_sum.find_all('li')

    print([name[0].text],[price.text],[liang.text],[one_price.text],[shipping_location[0].text],[residue[0].text],
          [company[0].text],[location.text],[sum_img],[xuke[0].text],
          [xuke[1].text],[changdi[0].text],[changdi[1].text],[xt],[zz],[zl],
          [commnet[0].text],[commnet[4].text],[sum_commnet[0].text],[sum_commnet[1].text],[sum_commnet[2].text],[sum_commnet[3].text],[sum_commnet[4].text],[sum_commnet[5].text],[sum_commnet[6].text])
    with open('date_sc_new.csv',mode='a',encoding='utf-8',newline='') as f:
        csv_write =csv.writer(f)
        csv_write.writerow([name[0].text]+[price.text]+[liang.text]+[one_price.text]+[shipping_location[0].text]+[residue[0].text]+
                           [company[0].text]+[location.text]+[sum_img]+[xuke[0].text]+
                           [xuke[1].text]+[changdi[0].text]+[changdi[1].text]+[xt]+[zz]+[zl]+
                           [commnet[0].text]+[commnet[4].text]+[sum_commnet[0].text]+[sum_commnet[1].text]+[sum_commnet[2].text]+[sum_commnet[3].text]+[sum_commnet[4].text]+[sum_commnet[5].text]+[sum_commnet[6].text])

def parse_max_page():
    for page_id in sum_id:
        try:
            new_url = f'https://www.fupin832.com/foretrade/gxs/goodsdetail.shtml?order_id={page_id}&page_name=%25E5%2595%2586%25E5%2593%2581%25E5%2588%2586%25E7%25B1%25BB%25E5%2588%2597%25E8%25A1%25A8%25E9%25A1%25B5'
            print(f'正在获取id:{page_id}')
            parse_one_page(url=new_url)
        except Exception as e:
            print('GG')



main()
driver.quit()  # 关闭浏览器
parse_max_page()
