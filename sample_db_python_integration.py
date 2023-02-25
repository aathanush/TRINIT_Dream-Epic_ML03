import pymongo

client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb=client['Users']
information=mydb.usernames
record={
    "uname":"aathanush",
    "password":"12345"
}
information.insert_one(record)