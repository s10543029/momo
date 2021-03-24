# ppt 自動爬蟲 標題及網頁
import requests as req
import bs4

#目標網站
url = "https://www.ptt.cc/bbs/FATE_GO/index.html"

#請求網站
r = req.get(url)

#檢查回應。如果是200則成功請求
print(r)
for i in range(2):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    sel = soup.select("div.title a")#標題
    u = soup.select("div.btn-group.btn-group-paging a")#a標籤
    print("本頁的URL為"+url)
    url = "https://www.ptt.cc"+ u[1]["href"] #上一頁的網址
    root = bs4.BeautifulSoup(r.text,"html.parser")#找到所有屬性class = "m-ent"
ment = root.find_all("div",class_="title")#一個一個印出要的資料
for title in ment:
    print(title.a.string)#取得文章標題
    print("https://www.ptt.cc"+title.a.get("href"))#取得文章連結
