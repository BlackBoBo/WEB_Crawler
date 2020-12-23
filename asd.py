from bs4 import BeautifulSoup

def ahn():

    ahn_request = requests.get('https://asec.ahnlab.com/ko/', headers={'User-Agent': 'Mozilla/5.0'}) # 뼈대
    ahn_query0= BeautifulSoup(ahn_request.content,"html.parser")
    ahn_query = ahn_query0.body

    ahn_extract = ahn_query.find("div",{"class":"post-archive-wrap"})
    ahn_finalextract = ahn_extract.find("a",{})
    
    ahn_urlpar=re.findall('"(.+[0-9])+',str(ahn_finalextract))
    ahn_strmov=(''.join(ahn_urlpar))

    print(ahn_strmov)

    #ahn_final = ('https://blog.alyac.co.kr/'+ahn_strmov)