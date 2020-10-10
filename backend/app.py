# render_template：参照するテンプレートを指定
# jsonify：json出力
from flask import Flask, render_template, jsonify

# CORS：Ajax通信するためのライブラリ
from flask_cors import CORS
from random import *

# static_folder：vueでビルドした静的ファイルのパスを指定
# template_folder：vueでビルドしたindex.htmlのパスを指定
app = Flask(__name__, static_folder = "./../frontend/dist/static", template_folder="./../frontend/dist")

app.config.from_object(__name__)

CORS(app)

# 任意のリクエストを受け取った時、index.htmlを参照
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch(path):
    return render_template("index.html")

# '/rand'が叩かれた時、乱数を生成
@app.route('/rand')
def random():
    response = {
        'randomNum': randint(1,100)
    }
    return jsonify(response)

@app.route('/data')
def get_data():
    topic_list = []
    with open('minkeiki_topic_rate.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            topic_list.append(row)
    topics = []
    for i in range(10):
    topics.append([x[i] for x in topic_list])
    response = {
    topics[0][0]: topics[0][1:],
    topics[1][0]: topics[1][1:],
    topics[2][0]: topics[2][1:],
    topics[3][0]: topics[3][1:],
    topics[4][0]: topics[4][1:],
    topics[5][0]: topics[5][1:],
    topics[6][0]: topics[6][1:],
    topics[7][0]: topics[7][1:],
    topics[8][0]: topics[8][1:],
    topics[9][0]: topics[9][1:],
    }

    return jsonify(response)

    

# app.run(host, port)：hostとportを指定してflaskサーバを起動
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)