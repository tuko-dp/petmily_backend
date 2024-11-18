from fastapi import APIRouter, HTTPException, Request
from ConnectMysql import ConnectMysql
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from model import signup_model
from model import siginin_model
import bcrypt

db = ConnectMysql()

router = APIRouter(
  prefix="/user",
)

HOST="127.0.0.1"
PORT=3308
USER="root"
PW="sad123"
DB="team"

conn, cur = db.mysql_create_session(HOST, PORT, USER, PW, DB)
sql = ""

# 암호화 함수
def encrypt(pw):
  pw = pw.encode('utf-8')
  encrypt_pw = bcrypt.hashpw(pw, bcrypt.gensalt())
  return encrypt_pw

# 복호화 함수
def decrypt(pw, encrypt):
  print(bcrypt.checkpw(pw.encode("utf-8"), encrypt))

# 로그인
@router.post("/signin/")
async def sign_in(param: siginin_model.SigninUser):
  email = param.email
  pw = encrypt(param.pw)
  sql = "select * from user_table where email=%s"
  cur.execute(sql, (email))
  rows = cur.fetchall()
  if rows:
    sql = "select * from user_table where pw=%s"
    cur.execute(sql, {pw})
    rows = cur.fetchall()
    if rows:
      return rows
  return HTTPException(status_code=401, detail="Login Fail")

# 회원가입
@router.post("/signup/")
async def sign_up(param: signup_model.SignupUser):
  id = param.id
  email = param.email
  pw = encrypt(param.pw)
  name = param.name
  age = param.age
  gender = param.gender
  phone = param.phone
  address = param.address
  birth = param.birth
  calendar = param.calendar_id
  reviews = param.review_id
  sql = "select * from user_table where email=%s"
  cur.execute(sql, {email})
  rows = cur.fetchall()
  if rows:
    print("유저 있음")
    return HTTPException(status_code=401, detail="USER_EXISTS")
  sql = "insert into user_table values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
  cur.execute(sql, [id, email, pw, name, age, gender, phone, address, birth, calendar, reviews])
  cur.execute("commit;")
  result = cur.fetchone()
  print(result)
  if result == None:
    return HTTPException(status_code=200, detail="SUCCESSFUL_SIGNUP")
  return HTTPException(status_code=401, detail="FAILURE_SINGUP")