# D. 데이터 가공 - 새로운 값을 만들어 반환하기

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

def new_dict(base_list,option_list):
   result = []
   for product in base_list:
      new_product = {}
      options = []
      for option in option_list:
         new_option = {}
         if option['fin_prdt_cd'] == product['fin_prdt_cd']:
            new_option['저축금리유형'] = option['intr_rate_type']
            new_option['저축금리유형명'] = option['intr_rate_type_nm']
            new_option['저축 기간'] = option['save_trm']
            new_option['저축 금리'] = option['intr_rate']
            new_option['최고 우대금리'] = option['intr_rate2']
            options.append(new_option)
      new_product['금융회사명'] = product['kor_co_nm']
      new_product['금융상품명'] = product['fin_prdt_nm']
      new_product['금리정보'] = options
      result.append(new_product)

   return result

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()['result']
    baseList = result['baseList']
    optionList = result['optionList']
    pp(new_dict(baseList,optionList))