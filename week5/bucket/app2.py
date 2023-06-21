from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
import certifi
import requests
from bs4 import BeautifulSoup
from flask import jsonify
from pymongo import MongoClient 

client = MongoClient('mongodb+srv://test:sparta@cluster0.u7yzppb.mongodb.net/?retryWrites=true&w=majority', tlsCAfile=certifi.where())
db = client.bucket

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('indexbucket.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    count = db.bucket.count_documents({})
    num = count + 1
    doc = {
        'num':num,
        'bucket': bucket_receive,
        'done': 0
    }
    db.bucket.insert_one(doc)
    return jsonify ({'msg':'data saved!'})

    # sample_receive = request.form['sample_give']
    # print(sample_receive)
    # return jsonify({'msg': 'POST /bucket request!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)},{'$set':{'done':1}})
    return jsonify ({'msg': 'Update done!'})
                         
    # sample_receive = request.form['sample_give']
    # print(sample_receive)
    # return jsonify({'msg': 'POST /bucket/done request!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    buckets_list = list(db.bucket.find({},{'_id':False}))
    return jsonify ({'buckets':buckets_list})
    # return jsonify({'msg': 'GET request!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
