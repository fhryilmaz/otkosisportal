from pymongo import MongoClient, ASCENDING
import sys
import time
import datetime




uri = "mongodb://otkoadmin:otkoadmin@35.204.4.232:27017"
clientMongo = MongoClient(uri)
db = clientMongo['Field_Storage']
collection = db['Tags']






deviceName = "100ENGKAEL100"
dailyreportDay = "20-06-2018"
startdailyreportTimeStamp = time.mktime(datetime.datetime.strptime(dailyreportDay+"-0-0-0","%d-%m-%Y-%H-%M-%S").timetuple())
stopdailyreportTimeStamp = time.mktime(datetime.datetime.strptime(dailyreportDay+"-23-59-59","%d-%m-%Y-%H-%M-%S").timetuple())
dailyreportfileName = deviceName+"-"+dailyreportDay+".html"







report = open("C:/Users/fahri/Desktop/OtkoAdminServices/var/www/report_archive/"+dailyreportfileName,"w")
reportLines = []

reportLines.append("<!DOCTYPE html>")
reportLines.append("<html>")
reportLines.append("<body>")
reportLines.append("<h1>"+deviceName+"</h1>")
reportLines.append("<h1>"+dailyreportDay+"  Günlük Enerji Raporu</h1>")
reportLines.append("</body>")
reportLines.append("</html>")

report.writelines(reportLines)
report.close()


cursor = collection.find({"$and":[{"tagtimeStamp":{"$gt":1529442000.0}},
                      {"tagtimeStamp":{"$lt":1529528399.0}},
                      {"tagName":{"$in":["/^100ENGKAEL100/"]}}]})




print(cursor.count(False))
for doc in cursor:
    print(doc)