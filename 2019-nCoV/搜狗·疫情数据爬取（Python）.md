# 搜狗·疫情数据爬取（Python）

前面已经说过，这次，不说废话，直接上代码。

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

