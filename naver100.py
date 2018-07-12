#-*- coding: utf-8 -*-

import os
import urllib
import openpyxl
import requests
from progress.bar import Bar
from datetime import datetime
from bs4 import BeautifulSoup
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webserver.settings")

import django
django.setup()
from parsed_data.models import NaverData

#setup
total_data=[]
titleUrlList=[]
titleList=[]
priceList=[]
imgList=[]
dataSetList=''
editData_img_total=''
editData_title_total=''
editData_price_total=''
dataFinal = ''

naverUrl="https://search.shopping.naver.com/best100v2/detail.nhn?catId=5000"
urlCode=[6631,6632,6633,6634,6635,6637,6638,6639,6640,6641,6642,6643,6644,6645,6679,6680,6681,6682,6683,6685,6686,6687,6688,6689,6690,6691,6692,6693]
searchName=['강아지_건식사료','강아지_소프트사료','강아지_캔사료','강아지_수제사료','강아지_분유우유','강아지_개껌','강아지_사사미','강아지_수제간식','강아지_비스킷시리얼쿠키','강아지_동결건조간식','강아지_캔파우치','강아지_저키스틱','강아지_통살소시지','강아지_음료','고양이_건식사료','고양이_캔사료','고양이_파우치사료','고양이_수제사료','고양이_분유우유','고양이_캔파우치','고양이_수제간식','고양이_사사미','고양이_동결건조간식','고양이_저키스틱','고양이_통살소시지','고양이_비스킷시리얼쿠키','고양이_캣닢캣그라스','고양이_음료']
#print len(urlCode)
#print len(searchName)

print "\n\n\n-----> 네이버 TOP100 크롤러"
print "-----> 버젼1.0, 만든이: psychofass\n\n"

barIndex = len(urlCode)
bar = Bar('Processing', max=barIndex)

def parse_Naver100():
	global dataSetList

	for i in range(0, 1):
	#for i in range(0, len(urlCode)):
		targeturl=naverUrl+str(urlCode[i])
		contents = requests.get(targeturl).text
		soup = BeautifulSoup(contents, "html.parser")

		for tag in soup.select('div[class=thumb_area]'):
			#editData_img = tag.text.strip()
			editData_img = tag.find('img')['data-original']
			imgList.append(editData_img)
			#print editData_img
		for tag in soup.select('p[class=cont]'):
			editData_title = tag.text.strip()
			titleList.append(editData_title)
			#print editData_title
		for tag in soup.select('div[class=price]'):
			editData_price = tag.text.strip()
			editData_price_str = editData_price.encode('utf-8')
			editData_price_str = editData_price_str.replace('모바일가격','')
			editData_price_str = editData_price_str.replace('최저','')
			editData_price_str = editData_price_str.replace('원','')
			editData_price_str = editData_price_str.replace(',','')
			priceList.append(editData_price_str)
			#print editData_price_str
		for tag in soup.select('p[class=cont]'):
			linkUrl = tag.find('a')['href']
			titleUrlList.append(linkUrl)
			#print linkUrl

		
	#file ouput
	for parsingNum in range(0, len(titleList)):
		dataSet=titleList[parsingNum]+","+priceList[parsingNum]+","+imgList[parsingNum]+","+titleUrlList[parsingNum]
		dataSetList=dataSetList+'\n'+dataSet

	dataUtf = dataSetList.encode('utf-8')
	
	bar.next()
	
	#print dataUtf
	return dataUtf

parse_Naver100()

if __name__=='__main__':
	naver_data_dic = parse_Naver100()
	setLines = naver_data_dic.splitlines() #editDataStr 변수 안에 있는 데이터를 한 줄씩 분리해서 setLines에 저장
	for line in setLines: #setLines를 한 줄씩 읽어서 line변수에 넣는다.

		f1 = line.find(',')
		title = line[:f1]
		remain1 = line[f1+1:]
		print title

		f2 = remain1.find(',')
		price = remain1[:f2]
		remain2 = remain1[f2+1:]
		print price

		f3 = remain2.find(',')
		img = remain2[:f3]
		remain3 = remain2[f3+1:]
		print img

		f4 = remain3.find(',')
		url = remain3[:f4]
		print url

		NaverData(title=title, price=price, imgLink=img, urlLink=url).save()

bar.finish()
