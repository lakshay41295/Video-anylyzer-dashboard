import pandas as pd
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["videos_in"]
mycol = mydb["video_data"]
df= pd.read_csv('INvideos.csv')
df1=df.sample(n = 500)
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
    mydict['description']=row['description']
    x = mycol.insert_one(mydict)
   