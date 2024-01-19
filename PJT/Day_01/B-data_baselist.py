# B. 데이터 추출 - 전체 정기예금 상품 리스트

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
    
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    pp(result['result']['baseList'])