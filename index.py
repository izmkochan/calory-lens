from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

app = Flask(__name__)

# .envからLINEのチャンネル情報を取得
CHANNEL_ACCESS_TOKEN = os.getenv('jC0SFvsUzLw6e4NkDxi9pKdBIQ/+AlL7p5iU3W9aZRl/bSacYyfBHwNSXKlzYe+1E3Rdj3R6aaljD4ArxOMeWFvS+zlxSyES4V9mf3q8IFEDAtXVxd+urc93HDImpsyMYDRcjytqmYLQBd7cPIDJvgdB04t89/1O/w1cDnyilFU=')
CHANNEL_SECRET = os.getenv('40f8fdd323bb523d32d82714f4735379')

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/", methods=["GET"])
def hello():
    return "IZM子ちゃんのカロリーレンズへようこそ！"

@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers.get("X-Line-Signature")
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"あなたが送ったメッセージ: {user_message}")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
