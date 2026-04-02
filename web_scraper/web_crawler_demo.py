import requests
from bs4 import BeautifulSoup


def scrape_books():
    url="http://books.toscrape.com/"

    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}
    content=requests.get(url).text #提取文本
    soup=BeautifulSoup(content,"html.parser")

    name_list=soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    print(f"成功发现{len(name_list)}本书！")
    for book in name_list:
        name=book.h3.a["title"]
        price=soup.find("p",attrs={"class":"price_color"}).get_text()
        print(f"书名：{name},价格：{price[1:]}")


scrape_books()


