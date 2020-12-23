from bs4 import BeautifulSoup
import requests
import re
import schedule
import threading


boan_saved=1                                                                       # 이전 URL 담아주는 역할
Daily_saved=1
bird_saved=1
ES_saved=1
ES2_saved=1
ahn_saved=1



def boan():

    boan_request = requests.get('http://www.boannews.com/media/t_list.asp')        # 응답확인
    boan_query = BeautifulSoup(boan_request.content, "html.parser")                # 전체내용 가져오기
    
    boan_extract = boan_query.find("div",{"class":"news_list"})                    # 원하는 내용 추출
    boan_finalextract = boan_extract.find('a')                                     # 원하는 내용 최종 추출2
    
    boan_urlpar=re.findall('href="(.+)"',str(boan_finalextract))                   # 정규식으로 필요 URL 추출
    boan_strmove=(''.join(boan_urlpar))                                            # 파싱한 리스트URL을 문자열로 변환
    boan_final = ('https://www.boannews.com/'+boan_strmove)                        

    global boan_saved                                                              # 동일 URL일 경우에만 출력하게 만듬
                                                                                   
    #print(boan_saved)                                                             # 전역변수의 출력을 확인
    
    if boan_saved != boan_final:                                                   # 다른 도메인일 경우 출력
        print(boan_final)     
        boan_saved = boan_final                                                    # 출력한 URL을 전에 출력했던 URL과 비교해주는 변수
            
        threading.Timer(30, boan).start()                                         # (@초 마다, 실행할것)
    else:
        print("동일 URL보안")
        threading.Timer(30, boan).start()
        
print('start')
boan()


def Daily():

    Daily_request = requests.get('https://www.dailysecu.com/news/articleList.html?sc_section_code=S1N2&view_type=sm')
    Daily_query= BeautifulSoup(Daily_request.content, "html.parser")
    
    Daily_extract = Daily_query.find("div",{"class":"list-titles"})
    Daily_finalextract = Daily_extract.find('a')
    
    Daily_urlpar=re.findall('"(.+)" ',str(Daily_finalextract))                 
    Daily_strmove=(''.join(Daily_urlpar))                                         
    Daily_final = ('https://www.dailysecu.com/'+Daily_strmove)                     
    
    global Daily_saved                                                              
                                                                               
    if Daily_saved != Daily_final:                                                   
        print(Daily_final)     
        Daily_saved = Daily_final                                                   
        threading.Timer(30, Daily).start()                                         
    else:
        print("동일 URL데일리")
        threading.Timer(30, Daily).start()

Daily()


def bird():
    bird_request = requests.get('https://hummingbird.tistory.com/', headers={'User-Agent': 'Mozilla/5.0'}) 
    bird_query= BeautifulSoup(bird_request.content, "html.parser")
    
    bird_extract = bird_query.find("div",{"class":"post-item"})
    bird_finalextract = bird_extract.find("a",{}) 
    
    bird_urlpar=re.findall('href="(.+)"',str(bird_finalextract))                  
    bird_strmove=(''.join(bird_urlpar))                                         
    bird_final = ('https://hummingbird.tistory.com'+bird_strmove)                    
    
    global bird_saved                                                              
                                                                               
    if bird_saved != bird_final:                                                   
        print(bird_final)     
        bird_saved = bird_final                                                   
        threading.Timer(1800, bird).start()                                         
    else:
        print("동일 URL버드")
        threading.Timer(1800, bird).start()
bird()

def ES():
    ES_request = requests.get('https://blog.alyac.co.kr/category/악성코드%20분석%20리포트', headers={'User-Agent': 'Mozilla/5.0'})
    ES_query0= BeautifulSoup(ES_request.content, "html.parser")
    ES_query= ES_query0.body
    
    ES_extract = ES_query.find("ul",{"class":"list_article list_sub list_sub_type1"})
    ES_finalextract = ES_extract.find("a",{})
    
    ES_urlpar=re.findall('href="(.+)"',str(ES_finalextract))
    ES_strmov=(''.join(ES_urlpar))
    ES_final = ('https://blog.alyac.co.kr'+ES_strmov)
    
    global ES_saved                                                              
                                                                               
    if ES_saved != ES_final:                                                   
        print(ES_final)     
        ES_saved = ES_final                                                   
        threading.Timer(1200, ES).start()                                         
    else:
        print("동일 URL이스트1")
        threading.Timer(1200, ES).start()
ES()

def ES2():
    ES2_request = requests.get('https://blog.alyac.co.kr/category/국내외%20보안동향', headers={'User-Agent': 'Mozilla/5.0'}) 
    ES2_query0= BeautifulSoup(ES2_request.content, "html.parser")
    ES2_query= ES2_query0.body
   
    ES2_extract = ES2_query.find("ul",{"class":"list_article list_sub list_sub_type1"})
    ES2_finalextract = ES2_extract.find("a",{})
    
    ES2_urlpar=re.findall('href="(.+?=[0-9]+)+',str(ES2_finalextract))
    ES2_strmov=(''.join(ES2_urlpar))
    ES2_final = ('https://blog.alyac.co.kr'+ES2_strmov)
    
    global ES2_saved                                                              
                                                                               
    if ES2_saved != ES2_final:                                                   
        print(ES2_final)     
        ES2_saved = ES2_final                                                   
        threading.Timer(1200, ES2).start()                                         
    else:
        print("동일 URL이스트2")
        threading.Timer(1200, ES2).start()
ES2()

def ahn():

    ahn_request = requests.get('https://asec.ahnlab.com/ko/', headers={'User-Agent': 'Mozilla/5.0'}) 
    ahn_query0= BeautifulSoup(ahn_request.content,"html.parser")
    ahn_query = ahn_query0.body

    ahn_extract = ahn_query.find("div",{"class":"post-archive-wrap"})
    ahn_finalextract = ahn_extract.find("a",{})
    
    ahn_urlpar=re.findall('"(.+[0-9])+',str(ahn_finalextract))
    ahn_strmov=(''.join(ahn_urlpar))

    global ahn_saved                                                              
                                                                                   
    if ahn_saved != ahn_strmov:                                                   
        print(ahn_strmov)     
        ahn_saved = ahn_strmov                                                   
                
        threading.Timer(1200, ahn).start()                                         
    else:
        print("동일 URL안랩")
        threading.Timer(1200, ahn).start()
            
ahn()



#앞으로 할 일

#URL 기사 작성시간 , 중복코드 정리