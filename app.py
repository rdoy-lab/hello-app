from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Get the requester's IP address
    ip = request.remote_addr
    
    try:
        # Make request to ip-api.com to get ISP information
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        # Extract ISP information
        isp = data.get('isp', 'Unknown')
        
        return f"Hello app. Your IP is {ip} and your ISP is {isp}"
    except Exception as e:
        return f"Hello app. Your IP is {ip}. Unable to retrieve ISP information."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
