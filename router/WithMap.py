from fastapi import APIRouter
import httpx
from dotenv import load_dotenv
import os
import json

router = APIRouter(
  prefix="/map"
)

load_dotenv()
APIKEY = os.environ.get("API_KEY")

"""
    전국 반려동물 동반 문화시설 위치 데이터 API 요청 함수
    한국문화정보원_전국 반려동물 동반 가능 문화시설 위치 데이터 API header 정보
    ===
    perPage: 요청 리스트 개수 = parameter로 요청값 입력
"""
def get_culture_API(per_page):
  result_data = {}
  print("===== 요청 페이지 수 {} =====".format(per_page))
  response = httpx.get("https://api.odcloud.kr/api/15111389/v1/uddi:41944402-8249-4e45-9e9d-a52d0a7db1cc?page=1&perPage={}".format(per_page)+"&serviceKey="+ APIKEY)
  text = response.text
  data = json.loads(text)
  for page in range(0, per_page, 1):
    result_data[page+1] = data["data"][page]["시설명"]
    # print(data["data"][page]["시설명"])
  # print(result_data)
    print (data["data"][page]["시설명"])
  return {
    "시설명" : result_data
  }

@router.get("/")
async def callAPI():
  return get_culture_API(10)