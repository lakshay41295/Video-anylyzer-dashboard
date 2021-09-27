from flask_pymongo import PyMongo
from flask import Flask
import flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/videos_in"
cors = CORS(app)
mongo = PyMongo(app)

@app.route("/")
def home():
    online_users = mongo.db.video_data.find()
    list1=[]
    for i in online_users:
        dict1={}
        dict1["video_id"]=i["video_id"]
        dict1["trending_date"]=i["trending_date"]
        dict1["title"]=i["title"]
        dict1["publish_time"]=i['publish_time']
        list1.append(dict1)

    return flask.jsonify(ok=True, videos_data=list1)


if __name__=='__main__':
    app.run(debug=True)
