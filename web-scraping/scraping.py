import json
import requests
from bs4 import BeautifulSoup

def getNewsData():
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }

    response = requests.get(
        "https://news.google.com/home?hl=en-US&gl=US&ceid=US:en", headers=headers
    )

    soup = BeautifulSoup(response.content,'html.parser')
    news_results = []
    
    for el in soup.select("div.XlKvRb"):
        news_results.append(
            {
                "link": el.find('a')['href'],
                "title": el.select_one("a.gPFEn").get_text(),
                "time": el.select_one('time.hvbAAd').get_text(),
                "source": el.select_one("div.vr1PYe").get_text(), 
                "author": el.select_one("div.bInasb").get_text()
            }
        )
    print(json.dumps(news_results, indent=2))

if __name__ == "__main__":
    print("scraping started...")
    getNewsData()

print('hello')
