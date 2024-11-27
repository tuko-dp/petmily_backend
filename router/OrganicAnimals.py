from fastapi import APIRouter
import httpx
from dotenv import load_dotenv
import os
import json

router = APIRouter(
  prefix="/organic"
)

load_dotenv()
APIKEY = os.environ.get("ANI_KEY")

"""
    전국동물보호센터정보표준데이터 API 요청 함수
"""
def get_orgainc_animal_API():
  url = 'http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic'
  params ={'serviceKey' : APIKEY, 'care_reg_no' : '', 'care_nm' : '', 'numOfRows' : '1', 'pageNo' : '1', '_type' : 'json' }
  response = httpx.get(url=url, params=params)
  data =  json.loads(response.text)
  print(data["response"]["body"])
  return data["response"]["body"]["items"]["item"][0]


@router.get("/")
def callAPI():
  return get_orgainc_animal_API()