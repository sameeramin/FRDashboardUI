from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route('/form', methods=['POST', 'GET'])
def form():
    uid = request.form['uid']
    print(uid)
    return jsonify({'status' : 'Done'})

if __name__ == '__main__':
    app.run()
