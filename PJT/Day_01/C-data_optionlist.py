# C. 데이터 가공 - 전체 정기예금 옵션 리스트

from pprint import pprint as pp
import requests

def get_deposit_products():
  api_key = "7637bc8b1d584436880b0942a8e8fb80"
  url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

  params = {
     'auth' : api_key,
     'topFinGrpNo' : '020000',
     'pageNo':1
  }
  result = requests.get(url, params = params).json()
  return result

# 원하는 데이터만 추출하여 출력되는 결과를 아래와 같이 변경하여 반환하는 함수를 작성
def Find_data(fin_co_no,intr_rate,save_trm,intr_rate_type,intr_rate_type_nm,intr_rate2,dcls_month,fin_prdt_cd):
   new_dict = {}
   new_dict['금융상품코드'] = fin_co_no
   new_dict['저축 금리'] = intr_rate
   new_dict['저축 기간'] = save_trm
   new_dict['저축금리유형'] = intr_rate_type
   new_dict['저축금리유형명'] = intr_rate_type_nm
   new_dict['최고 우대금리'] = intr_rate2

   pp(new_dict)
    
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    optionList = result['result']['optionList']
    for i in range(len(optionList)):
        Find_data(**optionList[i])