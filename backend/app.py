from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests


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

# Middleware to log each request
@app.before_request
def log_request_info():
    print(f'Headers: {request.headers}')
    print(f'Body: {request.get_data()}')


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
@app.route('/reateuser', methods=['POST'])
def createuser():
    student_data = {
        'netid_email': request.args.get("netid_email"),
        'name': request.args.get("name"),
        'github': request.args.get("github"),
        'leetcode': request.args.get("leetcode"),
        'bio': request.args.get("bio"),
        'pfp_url': request.args.get("pfp_url"),
    }

    # If the user doesn't exist, insert a new record
    new_student = Student(**student_data)
    db.session.add(new_student)

    db.session.commit()
    db.session.close()


    return jsonify({'status': 'User saved'}), 201


# leetcode endpoint  
@app.route('/leetcode/<username>', methods=['GET'])
def get_leetcode_user(username):
    url = f'https://leetcodestats.cyclic.app/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'User not found'}), 404



# Endpoint to add a new user to the database
@app.route('/add_user', methods=['GET'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], major=data['major'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully!'}), 201


# Endpoint to search user based on email
@app.route('/user/<int:user_email>', methods=['GET'])
def get_user(user_email):
    user = User.query.get(user_email)
    if user:
        return jsonify({'UIN': user.email, 'name': user.name, 'major': user.major})
    else:
        return jsonify({'error': 'User not found'}), 404
    



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
