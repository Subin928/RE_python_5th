from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.get("/data")  # get으로 코드 수정
def Data():
    print("getData", dict(request.args))
    return jsonify(ok=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#  * Serving Flask app '18_WIFI_03'
#  * Debug mode: off
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on all addresses (0.0.0.0)
#  * Running on http://127.0.0.1:5000
#  * Running on http://192.168.201.115:5000
# Press CTRL+C to quit
# getData {'temperature': '25', 'humidity': '60'}
# 192.168.201.115 - - [27/Jan/2026 11:37:30] "GET /data?temperature=25&humidity=60 HTTP/1.1" 200 -
# 192.168.201.115 - - [27/Jan/2026 11:37:30] "GET /favicon.ico HTTP/1.1" 404 -
