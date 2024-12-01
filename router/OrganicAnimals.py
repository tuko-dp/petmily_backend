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
def get_orgainc_animal_API(rows):
  file_data = {}
  kind_data = {}
  happenDt_data= {}
  happenPlace_data = {}
  colorCd_data = {}
  age_data = {}
  weight_data = {}
  noticeNo_data = {}
  noticeSdt_data = {}
  noticeEdt_data = {}
  sex_data = {}
  specialMark_data = {}
  processState_data = {}
  neuterYn_data = {}
  careNm_data = {}
  careTel_data = {}
  careAddr_data = {}

  url = 'http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic'

  for i in range(rows):
    params ={'serviceKey' : APIKEY, 'care_reg_no' : '', 'care_nm' : '', 'numOfRows' : rows, 'pageNo' : '1', '_type' : 'json' }
    response = httpx.get(url=url, params=params)
    data =  json.loads(response.text)["response"]["body"]["items"]["item"][i]
    file_data[i+1] = data["filename"]
    kind_data[i+1] = data["kindCd"]
    happenPlace_data[i+1] = data["happenPlace"]
    happenDt_data[i+1] = data["happenDt"]
    colorCd_data[i+1] = data["colorCd"]
    age_data[i+1] = data["age"]
    weight_data[i+1] = data["weight"]
    noticeNo_data[i+1] = data["noticeNo"]
    noticeSdt_data[i+1] = data["noticeSdt"]
    sex_data[i+1] = data["sexCd"]
    specialMark_data[i+1] = data["specialMark"]
    noticeEdt_data[i+1] = data["noticeEdt"]
    processState_data[i+1] = data["processState"]
    neuterYn_data[i+1] = data["neuterYn"]
    careNm_data[i+1] = data["careNm"]
    careTel_data[i+1] = data["careTel"]
    careAddr_data[i+1] = data["careAddr"]


  return {
    "사진": file_data,
    "접수일": happenDt_data,
    "접수장소": happenPlace_data,
    "품종코드" : kind_data,
    "색상": colorCd_data,
    "나이": age_data,
    "무게": weight_data,
    "공고번호": noticeNo_data,
    "접수일자": noticeSdt_data,
    "성별": sex_data,
    "특징": specialMark_data,
    "만료일시": noticeEdt_data,
    "상태": processState_data,
    "보호센터": careNm_data,
    "보호주소": careAddr_data,
  }


@router.get("/")
def callAPI():
  return get_orgainc_animal_API(10)