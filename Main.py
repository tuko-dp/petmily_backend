from typing import Union
from fastapi import FastAPI
from ConnectMysql import ConnectMysql

# 라우터로 처리한 API 가져오기
from router import User
from router import WithMap
from router import OrganicAnimals

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

# router 객체 등록
app.include_router(User.router)
app.include_router(WithMap.router)
app.include_router(OrganicAnimals.router)