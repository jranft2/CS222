from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
import requests
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Josephjj224:0j2VRcnTCPHv@ep-summer-dream-42168815.us-east-2.aws.neon.tech/CS222-91' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)


# User Model for Database
class Student(db.Model):
    name = db.Column(db.String(120), primary_key=True)
    netid_email = db.Column(db.String(80), nullable=False, unique=True)
    github = db.Column(db.String(120), nullable=True)
    leetcode = db.Column(db.String(120), nullable=True)
    bio = db.Column(db.String(120), nullable=True)
    pfp_url = db.Column(db.String(120), nullable=True)

class Enroll(db.Model):
    netid_email = db.Column(db.String(255), db.ForeignKey('student.netid_email'), primary_key=True)
    course_number = db.Column(db.String(255), db.ForeignKey('course.number'), primary_key=True)

class Course(db.Model):
    number = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))

class Major(db.Model):
    name = db.Column(db.String(255),primary_key = True)
    type_of_degree = db.Column(db.String(255))

class Studies(db.Model):
    netid_email	=db.Column(db.String(255),db.ForeignKey('student.netid_email'),primary_key = True)
    major_name=db.Column(db.String(255),db.ForeignKey('major.name'),primary_key = True)
    degree_type=db.Column(db.String(255),db.ForeignKey('major.degree_type'),primary_key = True)



    
@app.route('/')
def index():
    return '<h1>Hello from Flask!</h1>'

#github endpoint
@app.route('/github/<username>', methods=['POST'])
def get_github_user(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'User not found'}), 404
    

# save user details endpoint  
@app.route('/save-user-details', methods=['POST'])
def createuser():
    student_data = {
        'netid_email': request.headers.get("netidemail") or '',
        'name': request.headers.get("name") or '',
        'github': request.headers.get("github") or '',
        'leetcode': request.headers.get("leetcode") or '',
        'bio': request.headers.get("bio") or '',
        'pfp_url': request.headers.get("pfpurl")or '',
    }


    existing_record = Student.query.filter_by(netid_email=student_data['netid_email']).first()

    if(existing_record):
        existing_record.name = student_data['name']
        existing_record.github = student_data['github']
        existing_record.leetcode = student_data['leetcode']
        existing_record.bio = student_data['bio']
        existing_record.pfp_url = student_data['pfp_url']

        db.session.commit()
        db.session.close()
        return jsonify({'status': 'User updated'}), 201


    else:
        # If the user doesn't exist, insert a new record
        new_student = Student(**student_data)
        db.session.add(new_student)

        db.session.commit()
        db.session.close()

        return jsonify({'status': 'User added'}), 201


# leetcode endpoint  
@app.route('/leetcode/<username>', methods=['GET'])
def get_leetcode_user(username):
    url = f'https://leetcodestats.cyclic.app/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'User not found'}), 404




# Endpoint to search user based on email
@app.route('/user/<int:user_email>', methods=['GET'])
def get_user(user_email):
    user = User.query.get(user_email)
    if user:
        return jsonify({'UIN': user.email, 'name': user.name, 'major': user.major})
    else:
        return jsonify({'error': 'User not found'}), 404
    


# Endpoint to add a new user to the database
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], major=data['major'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully!'}), 201

  
  
# Endpoint to add a new user to the database
@app.route('/get_preferences', methods=['GET'])
def get_preferences():
    email = request.headers.get("netidemail")
    student = Student.query.filter_by(netid_email=email).first()
    return jsonify({'name': student.name, 'netid_email': student.netid_email, 'bio': student.bio, 'pfp_url': student.pfp_url, 'leetcode': student.leetcode, 'github': student.github})
  
  
#student table turn in to JSON 
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'name': student.name, 'netid_email': student.netid_email, 'bio': student.bio, 'pfp_url': student.pfp_url, 'leetcode': student.leetcode, 'github': student.github} for student in students])



#enroll table turn in to JSON 
@app.route('/enrolls', methods=['GET'])
def get_enroll():
    enroll_list = Enroll.query.all()
    return jsonify([{'netid_email': e.netid_email, 'course_number': e.course_number} for e in enroll_list])

#course table turn in to JSON 
@app.route('/courses', methods=['GET'])
def get_courses():
    Courses = Course.query.all()
    return jsonify([{'course_number': c.number, 'course_name': c.name} for c in Courses])

#major table turn in to JSON 
@app.route('/majors', methods=['GET'])
def get_majors():
    majors = Major.query.all()
    return jsonify([{'major': m.name, 'degree type': m.type_of_degree} for m in majors])

#Studies table turn in to JSON 
@app.route('/studies', methods=['GET'])
def get_studies():
    Studie = Studies.query.all()
    return jsonify([{'netid_email': st.netid_email, 'major_name': st.major_name, 'degree_type': st.degree_type } for st in Studie])



#search by the name
@app.route('/search', methods=['GET'])
def search_students():
    search_query = request.args.get('query', '') 
    matching_students = Student.query.filter(Student.name.ilike(f'%{search_query}%')).all()
    results = [{
        'netid_email': student.netid_email,
        'name': student.name,
        'bio': student.bio,
        'pfp_url': student.pfp_url,
        'leetcode': student.leetcode,
        'github': student.github
    } for student in matching_students]   
    return jsonify(results)

#search by the course number
@app.route('/search_by_course', methods=['GET'])
def search_by_course():

    course_number_query = request.args.get('course_number', '')
    enrollments = Enroll.query.filter(Enroll.course_number.ilike(f'%{course_number_query}%')).all()
    enrollments_list = [
        {'netid_email': enrollment.netid_email, 'course_number': enrollment.course_number}
        for enrollment in enrollments
    ]
    return jsonify(enrollments_list)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
