 #疫情数据爬取
library(rvest)
library(rjson)
url<-"http://sa.sogou.com/new-weball/page/sgs/epidemic?type_page=WEB"
page<-read_html(url)

html_dt<-page%>%html_nodes(xpath="//html/body/script[1]/text()")%>%html_text(trim = TRUE)

#删除不必要的js代码
a3<-sub('window.type_page = \"WEB\"\n      window.__INITIAL_STATE__ = ',"",html_dt)

josn_date<-fromJSON(a3)
#Real_time_epidemic

#全国昨日数据
yesterdayIncreased<-josn_date$data$domesticStats$yesterdayIncreased
# 各个省具体数据
provinceDetail<-josn_date$data$mapStats$provinceDetail

#省内具体市数据
area<-josn_date$data$area
# 省 市 确诊 疑似 治愈 死亡 

dt_last<- as.data.frame(t(matrix(unlist(area[[1]]),nrow=3,byrow=FALSE)))

citytempdate<-c()
provincetempdate<-c()

for (i in area) {
  provinceShortName<-i$provinceShortName
  
  confirmedCount<-i$confirmedCount
  curedCount<-i$curedCount
  deadCount<-i$deadCount
  provincetempdate<-c(c(provinceShortName,confirmedCount,curedCount,deadCount),provincetempdate)
  
  
  for (j in i$cities) {
    print("atart")
    #print(j)
    cityName<-j$cityName
    confirmedCount=j$confirmedCount
    curedCount=j$curedCount
    deadCount=j$deadCount
    #print(cityName)
    citytempdate<-c(c(provinceShortName,cityName,confirmedCount,curedCount,deadCount),citytempdate)
  }
}

}
#各个地区确诊人数、治愈人数、死亡人数 dt_city


dt_city<-data.frame(matrix(citytempdate,ncol=5,byrow=TRUE))
colnames(dt_city)<-c("PROVINCESHORTNAME","CITYNAME","CONFIRMEDCOUNT","CUREDCOUNT","DEADCOUNT")

#dt_province
dt_province<-data.frame(matrix(provincetempdate,ncol=4,byrow=TRUE))
colnames(dt_province)<-c("PROVINCESHORTNAME","CONFIRMEDCOUNT","CUREDCOUNT","DEADCOUNT")




write.csv(dt_city,"epidemic_city20200216.csv")
write.csv(dt_province,"epidemic_province20200216.csv")


#数据保存至数据库
library(RMySQL)
library(RMariaDB)

con <- dbConnect(MariaDB(), host="127.0.0.1", dbname="epid", user="root", password="1234")
dbListTables(con)
dbReadTable(con,"city_dt")
city<-data.frame(dt_city,DT=c(format(Sys.Date(),"%Y%m%d")))
province<-data.frame(dt_province,DT=c(format(Sys.Date(),"%Y%m%d")))
dbWriteTable(con,"city_dt",city,overwrite =FALSE,append=TRUE,row.names=FALSE) 
dbWriteTable(con,"province_dt",province,overwrite =FALSE,append=TRUE,row.names=FALSE) 
