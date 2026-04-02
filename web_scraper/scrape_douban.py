import requests
from bs4 import BeautifulSoup


"""获取豆瓣电影Top250"""
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}
for start_num in range(0,250,25):
    response=requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=headers)
    #print(response.status_code)
    html=response.text
    soup=BeautifulSoup(html,"html.parser")
    all_titles=soup.find_all("span",attrs={"class":"title"})
    for title in all_titles:
        title_string=title.string
        if "/" not in title_string:
            print(title_string)

            