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
  road_address = {}
  category2_data = {}
  category3_data = {}
  region_data = {}
  holiydays = {}
  with_pet = {}
  latitude_data = {}
  longitude_data = {}
  operate_data = {}
  call_num_data = {}
  print("===== 요청 페이지 수 {} =====".format(per_page))
  response = httpx.get("https://api.odcloud.kr/api/15111389/v1/uddi:41944402-8249-4e45-9e9d-a52d0a7db1cc?page=1&perPage={}".format(per_page)+"&serviceKey="+ APIKEY)
  text = response.text
  data = json.loads(text)
  for page in range(0, per_page, 1):
    result_data[page+1] = data["data"][page]["시설명"]
    road_address[page+1] = data["data"][page]["도로명주소"]
    category2_data[page+1] = data["data"][page]["카테고리2"]
    category3_data[page+1] = data["data"][page]["카테고리3"]
    region_data[page+1] = data["data"][page]["시도 명칭"]
    holiydays[page+1] = data["data"][page]["휴무일"]
    with_pet[page+1] = data["data"][page]["반려동물 동반 가능정보"]
    latitude_data[page+1] = data["data"][page]["위도"]
    longitude_data[page+1] = data["data"][page]["경도"]
    operate_data[page+1] = data["data"][page]["운영시간"]
    call_num_data[page+1] = data["data"][page]["전화번호"]
    print (data["data"][page]["시설명"])
  return {
    "시설명" : result_data,
    "도로명주소": road_address,
    "카테고리2": category2_data,
    "카테고리3": category3_data,
    "시도명칭": region_data,
    "휴무일": holiydays,
    "반려동물 동반 가능정보": with_pet,
    "위도": latitude_data,
    "경도": longitude_data,
    "운영시간": operate_data,
    "전화번호": call_num_data,
  }

@router.get("/")
async def callAPI():
  return get_culture_API(20)