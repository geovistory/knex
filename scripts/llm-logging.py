from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)
ollama_server_url = "http://localhost:11434"  # URL of the Ollama server

@app.route('/<path:path>', methods=['POST', 'GET'])
def log_request(path):

    # INPUT LOGS
    print('===========================')
    print()               
    print('#########################################')
    print('################# INPUT #################')
    print('#########################################')
    if request.method == 'POST':
        print()
        print('>>>>>>>>>> TOOLS <<<<<<<<<<')
        print(json.dumps(request.json['tools'], indent=4))
        print()
        print('>>>>>>>>>> MESSAGES <<<<<<<<<<')
        messages = request.json['messages']
        for message in messages:
            print(message['role'].upper() + ':', message['content'])


    # Manually set the stream attribute to false for every request
    data = request.get_json()
    data['stream'] = False

    # Forward the request to the actual Ollama server
    response = requests.request(
        method=request.method,
        url=f"{ollama_server_url}/{path}",
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        json=data,
        cookies=request.cookies,
        allow_redirects=False)


    # OUTPUT LOGS
    print()   
    print()               
    print('##########################################')
    print('################# OUTPUT #################')
    print('##########################################')
    message = response.json()['message']
    if "tool_calls" in message.keys():
        print()
        print('>>>>>>>>>> TOOLS <<<<<<<<<<')
        print(json.dumps(message['tool_calls'], indent=4))
    print()
    print('>>>>>>>>>> MESSAGES <<<<<<<<<<')
    print(message['role'].upper() + ':', message['content'])
    print()      


    # Send response back to the client
    return (response.content, response.status_code, response.headers.items())


if __name__ == '__main__':
    app.run(port=5000)
