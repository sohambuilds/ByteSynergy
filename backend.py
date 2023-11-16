from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def process_request():
    text = request.json['text']
    userId = request.json['userId']

    # Send request to Aeona3 API using provided credentials
    url = "https://aeona3.p.rapidapi.com/"
    querystring = {"text": text, "userId": userId}
    headers = {
        "X-RapidAPI-Key": "53491cea8emsh768b0fff762514bp166c52jsn7f2b78882d3c",
        "X-RapidAPI-Host": "aeona3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    aeona3Response = response.json()

    return jsonify({
        "message": aeona3Response['message']
    })

@app.route('/processRequest', methods=['POST'])
def process_request_endpoint():
    return process_request()

if __name__ == '__main__':
    app.run(debug=True)
