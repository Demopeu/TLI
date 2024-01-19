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

def Find_data(intr_rate,save_trm,intr_rate_type,intr_rate_type_nm,intr_rate2,dcls_month,fin_prdt_cd,fin_co_no):
   new_dict = {}
   new_dict['저축금리유형'] = intr_rate_type
   new_dict['저축금리유형명'] = intr_rate_type_nm
   new_dict['저축 기간'] = save_trm
   new_dict['저축 금리'] = intr_rate
   new_dict['최고 우대금리'] = intr_rate2

   return new_dict


def new_dict(Lst1,Lst2):
  newDit = []
  for i in range(len(Lst1)):
      New = {}
      cd=Lst1[i]['fin_prdt_cd']
      TMI = []
      for j in range(len(Lst2)):
          if Lst2[j]['fin_prdt_cd'] == cd:
              F = Find_data(**Lst2[j])
              TMI.append(F)
      #   print(New, TMI)
      New['금리정보'] = TMI
      New['금융회사명'] = Lst1[i]['kor_co_nm']
      New['금융상품명'] = Lst1[i]['fin_prdt_nm']
      #   print(newDit)
      newDit.append(New)
  

  return newDit

if __name__ == '__main__':
    # json 형태의 데이터 반환
  result = get_deposit_products()['result']
  baseList = result['baseList']
  optionList = result['optionList']
  pp(new_dict(baseList,optionList))