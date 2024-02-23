from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import boto3
from config import *
from pymysql import connections

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'  # SQLite database file
db = SQLAlchemy(app)


bucket = custombucket
region = customregion
db_conn = connections.Connection(
    host = customhost,
    user = customuser,
    password = custompass,
    db = customdb
)

@app.route("/")   
def index():
    return render_template('index.html')

# s3 = boto3.client('s3')  

# @app.route("/login")   
# def index():
#     return render_template('login.html')

# sns = boto3.client('sns', region_name='us-east-1')

# def publish_to_sns(message, topic_arn):
#     sns.publish(
#         TopicArn=topic_arn,message_to_publish = 'You have added an entry to employee database!'
# sns_topic_arn = '1:975050072755:EmailNotification'

# publish_to_sns(message_to_publish, sns_topic_arn) 


#         Message=message
#     )

# Example usage
# 

@app.route('/submit', methods=['POST'])
def submit(e_id,name,email,department,manager):
    e_id=request.form['eid'],
    name = request.form['name']
    email= request.form['email'],
    department=request.form['department'],
    manager=request.form['manager']
    
    # if request.files['photo']:
    #     print("image upload initiated")
    #     photo = request.files['photo']
    #     s3.upload_fileobj(photo, "addemployedata", f"employee_photos/{e_id}_{photo.filename}")
        

    
    insert_sql = "INSERT INTO employee (id, name, email, department, manager) VALUES (%s, %s, %s, %s,%s)"
    curser = db_conn.cursor()

# Execute the SQL query with the provided values
    curser.execute(insert_sql, (e_id, name, email, department, manager))

# Commit the changes to the database
    db_conn.commit()
    # message = f"Employee {name} with ID {e_id} added."
    # publish_to_sns(message)
    return render_template('success.html')
    
    


#     # Check if email is already registered
#     if Employee.query.filter_by(email=data['email']).first():
#         return jsonify({'error': 'Email already exists'}), 400


#     # Add user to the database
#     new_employee = Employee(email=data['email'], password=data['password'])
#     db.session.add(new_employee)
#     db.session.commit()


#     return jsonify({'message': 'Signup successful', 'user': {'email': new_employee.email}}), 201


# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()


#     # Find employee by email
#     employee = Employee.query.filter_by(email=data['email']).first()


#     if not employee or employee.password != data['password']:
#         return jsonify({'error': 'Invalid email or password'}), 401


#     return jsonify({'message': 'Login successful', 'user': {'email': employee.email}}), 200
# @app.route('/users', methods=['GET'])
# def get_users():
#     users = Employee.query.all()
#     user_data = [{'id': user.id, 'email': user.email} for user in users]
#     return jsonify(user_data)


# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     # Get form data from the request
#     form_data = request.json


#     # Create a new FormData object and save it to the database
#     new_form = FormData(fullname=form_data['fullname'],
#                         email=form_data['email'],
#                         phone=form_data['phone'],
#                         amount=form_data['amount'],
#                         terms=form_data['terms'])
#     db.session.add(new_form)
#     db.session.commit()


#     # Return a response
#     return jsonify({"message": "Form submitted successfully!"})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug= True)



