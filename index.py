
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "IZM子ちゃんのカロリーレンズへようこそ！"

@app.route("/webhook", methods=["POST"])
def webhook():
    # ここにLINEのWebhook処理を追加予定
    return "OK"

if __name__ == "__main__":
    app.run()
