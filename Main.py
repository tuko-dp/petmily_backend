from typing import Union
from fastapi import FastAPI
from ConnectMysql import ConnectMysql
from bs4 import BeautifulSoup
import requests

# 라우터로 처리한 API 가져오기
from router import User
from router import WithMap
from router import OrganicAnimals
from router import PetProfile

# app이라는 객체를 생성
app = FastAPI()
db = ConnectMysql()

# 프로젝트 진행 중에는 본임 MySQL 정보를 담고 평가직전 RDS 정보를 env 파일을 사용하여 붙일 예정
HOST="127.0.0.1"
PORT=3308
USER="root"
PW="sad123"
DB="team"

conn, cur = db.mysql_create_session(HOST, PORT, USER, PW, DB)

@app.get("/")
def read_root():
  sql = "SELECT NOW();"
  cur.execute(sql)  
  print(cur.fetchall())
  # cur.close()
  return {
    "Hello": "World!!"
  }

@app.get("/news")
def crawling_news():
  titles = []
  url_list = []

  url = "https://www.pet-news.or.kr/news/articleList.html?sc_sub_section_code=S2N69&view_type=sm"
  res = requests.get(url)
  if(res.status_code == 200):
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    section = soup.select('#section-list')
    # print(section)

    for h4 in section:
      h4_titles = h4.find_all("h4", {"class":"titles"})
      for title in h4_titles:
        titles.append(title.text.replace("\"", ""))

    for url in section:
      urls = url.select("#section-list > ul > li > div > h4 > a")
      for link in urls:
        url_list.append(link.attrs['href'])
    
    print(url_list)
    return {
      "제목": titles,
      "링크": url_list,
    }
  else:
    print(res.status_code)

# router 객체 등록
app.include_router(User.router)
app.include_router(WithMap.router)
app.include_router(OrganicAnimals.router)
app.include_router(PetProfile.router)