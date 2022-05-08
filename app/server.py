from flask import Flask, request, jsonify
import recognition

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Emmm</p>"

@app.route("/recog", methods=['POST'])
def recog():
    img = request.data
    rtn = recognition.handle(img)
    return jsonify({"result": rtn})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678)
