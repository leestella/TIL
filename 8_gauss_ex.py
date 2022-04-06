#네이버 웹툰 가우스 전자 시즌3~4 제목 +URL csv에 저장
# 값 출력하기
from bs4 import BeautifulSoup
import requests
import csv
url="https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

#csv파일로 쓰기
title="제목","url"
f=open("8_gauss_ex.py.csv","w",encoding='utf-8-sig',newline="")
writer=csv.writer(f)
writer.writerow(title)

soup = BeautifulSoup(res.text,"lxml")
cartoons=soup.find_all("td",attrs={"class":"title"})
"""
title=cartoons[0].a.get_text()
link=cartoons[0].a["href"]
print(title)
print("https://comic.naver.com"+link)
"""
c_title_l=[]
c_url_l=[]
# 데이터 리스트에 저장
for i in cartoons:
    title = i.a.get_text()
    c_title_l.append(title)

    urls=("https://comic.naver.com"+i.a["href"])
    c_url_l.append(urls)
# 리스트 zip으로 합침
data_all = list(zip( c_title_l,c_url_l))
# 통합 리스트 csv파일에 적기
writer.writerows(data_all)
f.close()
#csv 파일 읽기
f=open("8_gauss_ex.py.csv","r",encoding='utf-8-sig',newline="")
reader=csv.reader(f)
# 값 출력하기
for i in reader:
    print(i)