import json
from flask import Flask, render_template
import urllib.request as req
import bs4
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


def cr():
    url = "https://flights.evaair.com/zh-tw/"
    result = {
        "departures": [],
        "destinations": [],
        "prices": []
    }
    # 在傳入網址時加入headers以模仿一般使用者
    request = req.Request(url, headers={
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Mobile Safari/537.36"
    })
    # 將資料讀入
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")  # 解析HTML code
    # 尋找所有<span class="fare-atom-origin-destination-origin-city">的內容放到列表departures中
    departures = root.find_all(
        "span", class_="fare-atom-origin-destination-origin-city")
    destinations = root.find_all(
        "span", class_="fare-atom-origin-destination-destination-city")
    prices = root.find_all("span", class_="fare-atom-price-total-price")

    for i in range(len(departures)):
        result["departures"].append(departures[i].string)
        result["destinations"].append(destinations[i].string)
        result["prices"].append(prices[i].string)
    return result


@app.route("/craw")
def craw():
    a = cr()
    return json.dumps(a)


if __name__ == "__main__":
    app.run()
