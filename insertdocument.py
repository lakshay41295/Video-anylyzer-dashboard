import pandas as pd
import pymongo
from datetime import datetime
from dateutil import parser

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["videos_in"]
mycol = mydb["video_data"]
df= pd.read_csv('INvideos.csv')
df1=df.sample(n = 500)
list1=[]
list2=[]
for index, row in df1.iterrows():
    if row['dislikes']!=0:
        ratio=(row['likes']/row['dislikes'])*100
    else:
        ratio=0
    ratio1=round(ratio,2)
    if ratio1>95 and ratio1<100:
        list1.append("Controversial")
    else:
        list1.append('Non Controversial')
    
    date_obj1=datetime.strptime(row['publish_time'],'%Y-%m-%dT%H:%M:%S.%fZ').date()
    date_obj2=datetime.strptime(row['trending_date'],'%y.%d.%m').date()
    date3=date_obj2-date_obj1
    if date3.days>1:
        list2.append('non rising')
    else:
        list2.append('non rising')
    
    
df1['controversy_quote'] = list1
df1['trend_quote'] = list2
print(df1)

for index, row in df1.iterrows():
    mydict={}
    mydict['video_id']=row['video_id']
    mydict['trending_date']=row['trending_date']
    mydict['title']=row['title']
    mydict['channel_title']=row['channel_title']
    mydict['category_id']=row['category_id']
    mydict['publish_time']=row['publish_time']
    mydict['tags']=row['tags']
    mydict['views']=row['views']
    mydict['likes']=row['likes']
    mydict['dislikes']=row['dislikes']
    mydict['comment_count']=row['comment_count']
    mydict['thumbnail_link']=row['thumbnail_link']
    mydict['comments_disabled']=row['comments_disabled']
    mydict['ratings_disabled']=row['ratings_disabled']
    mydict['video_error_or_removed']=row['video_error_or_removed']
    mydict['controversy_quote']=row['controversy_quote']
    mydict['trend_quote']=row['trend_quote']
    x = mycol.insert_one(mydict)
   