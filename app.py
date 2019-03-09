from flask import Flask, jsonify

UPLOAD_FOLDER = './tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024


@app.route("/status", methods=['GET'])
def status():
    return jsonify({"message": "success"})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0')
