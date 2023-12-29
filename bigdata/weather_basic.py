import sys
# sys란? 파이썬 인터프리터가 제공하는 변수나 함수를 제어할 수 있는 방법을 제공한다.
import urllib.request as req
import urllib.parse as parse

# 명령행에서 인수 전달하기 
# 파이썬 인터프리터가 제공하는 변수나 함수를 제어할 수 있는 방법을 제공한다.
# Example
# sys.argv -> 인자 전체
# sys.argv[0] -> 첫 번째 인자 : 명령어
# sys.argv[n] -> n 번째 인자 : 명령어의 n번쨰 인자
if len(sys.argv) <= 1:
	print("usage : download-forecast-argv <region number>")
	sys.exit()
 
regionNumber = sys.argv[1]
 
api_addr = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    "stdId" : regionNumber
}

params = parse.urlencode(values) 
url = api_addr + "?" + params
print('url = ', url)

data = req.urlopen(url).read().decode('utf-8')
print(data)