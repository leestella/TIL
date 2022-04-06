# 1. 네이버 뉴스에 암호화폐 검색후 뉴스제목과 내용 5p스크래핑하기

# 2. csv파일로 저장

# 3. 저장된 파일을 이용하여 출력

import warnings
warnings.filterwarnings('ignore')
import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup
b=webdriver.Chrome()
b.implicitly_wait(10)
b.get("http://naver.com")
b.find_element_by_xpath('//*[@id="query"]').send_keys("암호화폐\n")
b.implicitly_wait(10)
b.find_element_by_xpath('//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()
b.implicitly_wait(10)


title="제목","내용"
f=open("Q2.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)
data_l=[]
data1_l=[]

for i in range(1,6):
    b.implicitly_wait(10)
    b.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    html=b.page_source
    b.find_element_by_xpath(f'//*[@id="main_pack"]/div[2]/div/div/a[{i}]').click
    s=BeautifulSoup(html,'html.parser')
    data=s.select('a.news_tit')
    data1=s.select('a.api_txt_lines.dsc_txt_wrap') # 클래스 하위에 클래스로 구성 .으로 연결
    for i in data:
        data_l.append(i.text) # 전체 값이 아닌 페이지당 data에서 text값만 추출 해주어야함
    for i in data1:
        data1_l.append(i.text)
data_all = list(zip(data_l, data1_l))
writer.writerows(data_all)
f.close()
f=open("Q2.csv","r",encoding='utf-8-sig',newline="")
reader=csv.reader(f)
for i in reader:
    print(i)