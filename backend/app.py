from flask import Flask, jsonify, request
import requests 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello from Flask!</h1>'

#github endpoint
 
@app.route('/github/<username>', methods=['GET'])
def get_github_user(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'User not found'}), 404
# leetcode endpoint  
@app.route('/leetcode/<username>', methods=['GET'])
def get_leetcode_user(username):
    url = f'https://api.leetcode.com/user/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'User not found'}), 404




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')

    