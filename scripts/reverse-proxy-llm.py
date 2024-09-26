from flask import Flask, request, jsonify
import requests, json, os

app = Flask(__name__)
ollama_server_url = "http://localhost:11434"  # URL of the Ollama server
input_logs_path = './llm-inputs.log'
output_logs_path = './llm-outputs.log'

# Clean existing input/output files
if os.path.exists(input_logs_path): os.remove(input_logs_path)
if os.path.exists(output_logs_path): os.remove(output_logs_path)

# Create outputs logs
f = open(input_logs_path, 'w')
f.close()
f = open(output_logs_path, 'w')
f.close()


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
            text = message['role'].upper() + ': ' + message['content']
            print(text)
            f = open(input_logs_path, 'a')
            f.write(text + '\n\n')
            f.close()


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
    text = message['role'].upper() + ': ' + message['content']
    print(text)
    f = open(output_logs_path, 'a')
    f.write(text + '\n\n')
    f.close()
    print()      


    # Send response back to the client
    return (response.content, response.status_code, response.headers.items())


if __name__ == '__main__':
    app.run(port=5000)
