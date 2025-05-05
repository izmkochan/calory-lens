from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 👇ここにLINEのチャンネル情報を入力（6〜7行目）
CHANNEL_ACCESS_TOKEN = 'EvcHm8jeH0Ztd8pX9PN283wL0C6Gv0WAcdcxxNIzw1FInRtHqnxy+4Bnj0O2AN9AE3Rdj3R6aaljD4ArxOMeWFvS+zlxSyES4V9mf3q8IFFqgIWaFrIEJF10qWM3iI3PkPeHoCxqNo3F9OHmPeXzNQdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '40f8fdd323bb523d32d82714f4735379'

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
