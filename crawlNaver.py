#-*- coding: utf-8 -*-

import os
import urllib
import openpyxl
import requests

from datetime import datetime
from bs4 import BeautifulSoup
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webserver.settings")

import django
django.setup()

from parsed_data.models import NaverData

#setup
titleUrlList=[]
titleList=[]
priceList=[]
dataSetList=''
naverUrl="https://search.shopping.naver.com/best100v2/detail.nhn?catId=5000"
urlCode=[6631,6632,6633,6634,6635,6637,6638,6639,6640,6641,6642,6643,6644,6645,6679,6680,6681,6682,6683,6685,6686,6687,6688,6689,6690,6691,6692,6693]
searchName=['강아지_건식사료','강아지_소프트사료','강아지_캔사료','강아지_수제사료','강아지_분유우유','강아지_개껌','강아지_사사미','강아지_수제간식','강아지_비스킷시리얼쿠키','강아지_동결건조간식','강아지_캔파우치','강아지_저키스틱','강아지_통살소시지','강아지_음료','고양이_건식사료','고양이_캔사료','고양이_파우치사료','고양이_수제사료','고양이_분유우유','고양이_캔파우치','고양이_수제간식','고양이_사사미','고양이_동결건조간식','고양이_저키스틱','고양이_통살소시지','고양이_비스킷시리얼쿠키','고양이_캣닢캣그라스','고양이_음료']
#print len(urlCode)
#print len(searchName)

print "\n\n\n-----> 네이버 TOP100 크롤러"
print "-----> 버젼1.0, 만든이: psychofass\n\n"

#for i in range(0, 1):
for i in range(0, len(urlCode)):
	targeturl_first=naverUrl+str(urlCode[i])
	#targeturl_first = "https://search.shopping.naver.com/best100v2/detail.nhn?catId=50006640"
	soup_first = BeautifulSoup(urllib.urlopen(targeturl_first).read(), "html.parser")

	editData_first_title = soup_first.find_all('p', {'class': "cont"})
	editDataStr_first_title = str(editData_first_title)
	editDataStr_first_title = editDataStr_first_title.replace('<p class="cont">','')
	editDataStr_first_title = editDataStr_first_title.replace(',','')
	editDataStr_first_title = editDataStr_first_title.replace('</p>','')
	editDataStr_first_title = editDataStr_first_title.replace(']','')
	editDataStr_first_title = editDataStr_first_title.replace('[','')
	editDataStr_first_title = editDataStr_first_title.replace('target="_blank" ','')
	editDataStr_first_title = editDataStr_first_title.replace('" ','\n')
	editDataStr_first_title = editDataStr_first_title.replace('<a href="','')

	editData_first_price = soup_first.find_all('div', {'class': "price"})
	editDataStr_first_price = str(editData_first_price)
	editDataStr_first_price = editDataStr_first_price.replace('strong','')
	editDataStr_first_price = editDataStr_first_price.replace('div','')
	editDataStr_first_price = editDataStr_first_price.replace('low','')
	editDataStr_first_price = editDataStr_first_price.replace('num','')
	editDataStr_first_price = editDataStr_first_price.replace('span','')
	editDataStr_first_price = editDataStr_first_price.replace('class','')
	editDataStr_first_price = editDataStr_first_price.replace('price','')
	editDataStr_first_price = editDataStr_first_price.replace('"','')
	editDataStr_first_price = editDataStr_first_price.replace('<','')
	editDataStr_first_price = editDataStr_first_price.replace('>','')
	editDataStr_first_price = editDataStr_first_price.replace('/','')
	editDataStr_first_price = editDataStr_first_price.replace('=','')
	editDataStr_first_price = editDataStr_first_price.replace(',','')
	editDataStr_first_price = editDataStr_first_price.replace('[','')
	editDataStr_first_price = editDataStr_first_price.replace(']','')
	editDataStr_first_price = editDataStr_first_price.replace(' ','')
	editDataStr_first_price = editDataStr_first_price.replace('최저','')
	editDataStr_first_price = editDataStr_first_price.replace('\n','')
	editDataStr_first_price = editDataStr_first_price.replace('원','원\n')
	editDataStr_first_price = editDataStr_first_price.replace('ico_mobiletitle모바일에서구매가능한가격입니다모바일가격','')

	#print editDataStr_first_title
	#print editDataStr_first_price

	setLines_title = editDataStr_first_title.splitlines()
	setLines_price = editDataStr_first_price.splitlines()

	for line_Title in setLines_title:
		#print line_Title
		if 'http' in line_Title:
			titleUrlList.append(line_Title)
			print line_Title
		elif 'title' in line_Title:
			spaceTitle1 = line_Title.find('title="') #뒤에서부터 공백이 있는 문자열의 인덱스를 찾아 변수에 저장한다.
			titleTemp = line_Title[spaceTitle1:] #찾아낸 문자열 인덱스 뒤로 다 잘라낸다.
			spaceTitle2 = line_Title.find('>') 
			titleTemp = titleTemp[:spaceTitle2] 
			titleTemp = titleTemp.replace('"','')
			titleTemp = titleTemp.replace('title=','')
			titleTemp = titleTemp.replace(' ','')
			titleList.append(titleTemp)

	#for line_Title in setLines_price:
	#	priceList.append(line_Title)

	#for parsingNum in range(0, len(priceList)):
	#	dataSet=titleList[parsingNum]+","+priceList[parsingNum]+","+titleUrlList[parsingNum]
	#	dataSetList=dataSetList+'\n'+dataSet
		#print titleList[parsingNum]

	#변수초기화
	#dataSet =''
	#dataSetList =''
	#print titleList
	#print priceList
	#print titleUrlList
	titleList =[]
	priceList =[]
	titleUrlList =[]

print "-----> 출력완료"