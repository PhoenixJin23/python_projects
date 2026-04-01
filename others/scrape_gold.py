import requests
from bs4 import BeautifulSoup
import time


def get_realtime_gold_price():
    url="https://www.huilvbiao.com/gold"

    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"}
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            soup=BeautifulSoup(response.text,"html.parser")

            price_tag=soup.find("p",id="new")
            if price_tag:
                #strip=True去掉前后空格
                price=price_tag.get_text(strip=True)
                print("请求成功！")
                return price
        else:
            print(f"请求失败，状态码：{response.status_code}")
    except Exception as e:
        print("发生错误哦:",e)


def monitor_gold(interval_seconds=60):
    """每隔一段时间获取一次金价，实现实时监控"""
    print("国内金价实时监控启动：")
    print(f"监控频率：每{interval_seconds}秒更新一次")

    try:
        while True:
            price=get_realtime_gold_price()
            if price:
                current_time=time.strftime("%H:%M:%S",time.localtime())
                print(f"[{current_time}]当前金价：{price}RMB/gram")

            #休息一下，避免频繁请求被锁IP
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\n监控已停止")


monitor_gold(10)
