# 정적 크롤링 연습
from bs4 import BeautifulSoup
import requests

#쿠팡에서 노트북 검색창 1~4 page 크롤링 
for i in range(1,5):
    print(f"----{i}페이지 크롤링중-----\n")
    url=f'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=1=4&backgroundColor='
    res = requests.get(url)
    res.raise_for_status()
    s=BeautifulSoup(res.text,"lxml")
#find_all에서 큰 단위 빼오기 (find_all과 select는 list형태라 .text 못 붙임)
    computers = s.find_all("dl", attrs={"class": "search-product-wrap"})
    for computer in computers:
        # name=computer.find("div",attrs={"class":"name"}).text 아래식과 같은 작용
        name = computer.select_one("div.name").text
        price = computer.select_one("strong.price-value").text
        print(f"{name} \n {price}")
