from flask import Flask, jsonify, request
import requests

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

# keys mady
#key = "3efe59a334msha059c985bfdfa0fp19b733jsn38325d8631fd"
#key = "c1ae7440ebmsh05213312eea3336p1ac589jsnd5e132631543"

#key yu
key = "247379b4damshfe39ac9626aab44p15ecfcjsn13ea3c96852c"

url_user = "https://twttrapi.p.rapidapi.com/get-user"
url_user_followers = "https://twttrapi.p.rapidapi.com/user-followers"

@app.route('/get-user-info', methods=['GET'])
def get_user_info():
    username = request.args.get('username')
    querystring = {"username": username}
    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
    }
    response = requests.get(url_user, headers=headers, params=querystring)
    return jsonify(response.json())

@app.route('/get-user-followers-info', methods=['GET'])
def get_user_followers_info():
    username = request.args.get('username')
    querystring = {"username": username, "count": "20"}
    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "twttrapi.p.rapidapi.com"
    }
    response = requests.get(url_user_followers, headers=headers, params=querystring)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
