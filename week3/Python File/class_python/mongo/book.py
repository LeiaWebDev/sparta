from pymongo import MongoClient
import certifi 

client = MongoClient('mongodb+srv://test:sparta@cluster0.u7yzppb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
# client = MongoClient('mongodb+srv://test:<sparta>@cluster0.u7yzppb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta

db.books.insert_one({
    'title': 'Harry Potter',
    'author': 'J.K. Rowling',
    'rating': 90
})

db.books.insert_one({
    'title': 'The Fisherman and the Fish',
    'author': 'Joseph Choi',
    'rating': 10
})

db.books.insert_one({
    'title': 'Fire in the Water',
    'author': 'Some Dude',
    'rating': 57
})

db.books.update_one({'title':'The Fisherman and the Fish'},
    {'$set':{'author':'Jimmy Kim'}})

all_books = list(db.books.find({},{'_id':False}))
for book in all_books:
    print(book)

db.books.delete_one({'rating':90})