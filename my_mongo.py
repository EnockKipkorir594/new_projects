from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
from dotenv import load_env

load_env()

app = Flask(__name__)

client = MongoClient(os.getenv("DATABASE_URL"))

db = client.myDatabase
students_collections = db.students
@app.route('/api/v1.o/students', methods = ['GET'])

def get_students():
    students = list(students_collections.find({}, {'_id':0}))
    return jsonify(students)

def add_students():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({'error':'Student must have name'}), 400
    students_collections.insert_one(data)
    return jsonify({'student':'student added successfully'}), 201

if __name__ == '__main__':    


    port = int(os.environ.get('PORT', 5000))
    app.run(debug= True, host= '0.0.0.0', port=port)
