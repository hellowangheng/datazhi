# 搜狗·疫情数据爬取（Python）

上周已经分享过[搜狗·疫情数据爬取（R语言）](https://www.cnblogs.com/wheng/p/12318520.html)，这次分享一下**搜狗·疫情数据爬取（Python）**

不说废话，直接上代码。有什么问题，可以在留言区讨论。

```python
from urllib import request
from lxml import etree
import re
import pandas as pd
import json

url="http://sa.sogou.com/new-weball/page/sgs/epidemic?type_page=WEB"
response = request.urlopen(url)      #请求

html = response.read()#获取
html = html.decode("utf-8")#解码

xml = etree.HTML(html)
datas = xml.xpath('//html/body/script[1]/text()')

datas=re.sub('window.type_page = \"WEB\"\n      window.__INITIAL_STATE__ = ',"",datas[0])

area=json_data["data"]["area"]

citytempdate = []
provincetempdate = []
for i in area:
    provinceShortName = i["provinceShortName"]
    confirmedCount = i["confirmedCount"]
    curedCount = i["curedCount"]
    deadCount = i["deadCount"]
    provincetempdate.append([provinceShortName,confirmedCount,curedCount,deadCount])
    for j in i["cities"]:
        cityName = j["cityName"]
        confirmedCount=j["confirmedCount"]
        curedCount=j["curedCount"]
        deadCount=j["deadCount"]
        citytempdate.append([provinceShortName,cityName,confirmedCount,curedCount,deadCount])
  
dt_city = pd.DataFrame(citytempdate,columns=["PROVINCESHORTNAME","CITYNAME","CONFIRMEDCOUNT","CUREDCOUNT","DEADCOUNT"])
dt_province = pd.DataFrame(provincetempdate,columns=["PROVINCESHORTNAME","CONFIRMEDCOUNT","CUREDCOUNT","DEADCOUNT"])


```
各城市（部分）数据如下：

|      | PROVINCESHORTNAME | CITYNAME | CONFIRMEDCOUNT | CUREDCOUNT | DEADCOUNT |
| ---: | ----------------: | -------: | -------------: | ---------: | --------- |
|    0 |              湖北 |     武汉 |          41152 |       3507 | 1309      |
|    1 |              湖北 |     孝感 |           3279 |        449 | 70        |
|    2 |              湖北 |     黄冈 |           2831 |        839 | 78        |
|    3 |              湖北 |     荆州 |           1501 |        305 | 37        |
|    4 |              湖北 |     鄂州 |           1274 |        244 | 35        |
|    5 |              湖北 |     随州 |           1267 |        140 | 24        |
|    6 |              湖北 |     襄阳 |           1155 |        151 | 20        |

各省分总体（部分）数据如下：

|      | PROVINCESHORTNAME | CONFIRMEDCOUNT | CUREDCOUNT | DEADCOUNT |
| ---: | ----------------: | -------------: | ---------: | --------- |
|    0 |              湖北 |          58182 |       6693 | 1696      |
|    1 |              广东 |           1322 |        524 | 4         |
|    2 |              河南 |           1246 |        509 | 16        |
|    3 |              浙江 |           1171 |        507 | 0         |
|    4 |              湖南 |           1006 |        498 | 3         |
|    5 |              安徽 |            973 |        280 | 6         |
|    6 |              江西 |            930 |        275 | 1         |
|    7 |              江苏 |            626 |        258 | 0         |
|    8 |              重庆 |            552 |        211 | 5         |
|    9 |              山东 |            541 |        191 | 2         |

转载请注明：

微信公众号：数据志

简书：数据志

博客园：https://www.cnblogs.com/wheng/

CSDN：https://blog.csdn.net/wzgl__wh

GitHub（数据、代码）：https://github.com/hellowangheng/datazhi/tree/master/2019-nCoV

