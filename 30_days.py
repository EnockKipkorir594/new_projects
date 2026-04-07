'''
The goal is to essentially to build an API using Flask and MongoDB database 
Use some dummy data of students with the following attribues:
name, age, skills, country, date of birth , city 
The tools required to complete this task are :
Flask 
MongoDB
Postman 

'''
from flask  import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/v1.0/students', methods= ['GET'])
def students():
    student_list = [
        {
        'name':'John Mcginn',
        'country':'Croatia',
        'city':'London',
        'skills': ['HTML', 'CSS', 'Python']
    },
    {
        'name':'Yuri Tielemans',
        'country':'England',
        'city':'Afgani',
        'skills':['MongoDB','Flask','C++']

    },
    {
        'name':'Marcus Rashford',
        'country':'England',
        'city':'North London',
        'skills':['CSS', 'C#', 'Django']
    },
    {
        'name': 'Mark Zuckenberg',
        'country':'USA',
        'city':'Sillicon Valley',
        'skills':['JS', 'Python', 'Cursor'] 
    },
    {
        'name':'Peter Griffin',
        'country':'UK',
        'city':'Luton',
        'skills':['Lovable', 'ML', 'Devops', 'Cybersecurity']
    }
    ]
    return jsonify(student_list)


if __name__ == '__main__':

    port = int(os.environ.get('PORT',5000))
    app.run(debug= True, host='0.0.0.0', port=port)



