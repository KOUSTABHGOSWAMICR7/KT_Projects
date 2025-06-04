from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['QA_database']
collection = db['QA_collection']

def insert_data():
    data = [
        {'intent': 'java', 'answer': 'Java is a programming language.'},
        {'intent': 'ejs', 'answer': 'EJS is a view engine.'},
        {'intent': 'jinja', 'answer': 'Jinja is a template engine.'}
    ]
    if collection.count_documents({}) == 0:
        collection.insert_many(data)
