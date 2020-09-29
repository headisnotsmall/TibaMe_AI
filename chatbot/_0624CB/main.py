from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('nbE0Yqi3KGYDpWH579IgAtS1ggxub+PUUgy0tUvNlkKAfIoRdo4D2GOiaPOQgqA6wr47BQdZ/6S4C/uhLmphZ2EpCs7xHhRwVC2kzpmdwVIyAnWRxdxEw3JKJvl1uY64mLntrp2GqPwUJccqeEc4owdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('784899c6df4a550a6b1d11f2fb5ad363')

# 1. 驗證消息準確性
# 2. 轉發給相關部門
# 3. 處理不合規訊息

@app.route("/callback", methods=['POST'])
def callback():
    # don't know don't care
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print anything you get
    app.logger.info("Request body: " + body)
    print(body)

    # handle webhook body
    try:
        # let body and signature 確認消息的合法性
        # 另一用途 >>> 轉發給後續的業務邏輯
        handler.handle(body, signature)
        # 若不合法、執行以下處理
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# 客戶自製邏輯
# handler 收到文字消息時、執行以下def
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # event 指用戶傳來的消息
    # 請line_bot_api回復傳來的訊息
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run(host='0.0.0.0')



# '''
#
# 啟動flask server
#
# flask starter example
#
# '''
#
# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return '"Hello World!"'
#
# '''
#
# 準備一個路徑 (URN)
# 此路徑為lbh
# 用戶訪問此路徑的時候 回傳______
#
# '''
#
# @app.route('/lbh')
# def hello_lbh():
#     return "lishilekuasashiu"
#
# @app.route('/simulate-ai')
# def simulate_ai():
#     # ai
#     calResult = 1 + 1
#     return str (calResult)
#
# import requests
# @app.route("/crawler")
# def crawsomething():
#     crawler = requests.get("https://www.ptt.cc/bbs/PlayStation/M.1592886571.A.DB0.html")
#     return crawler.text
#
# app.run(host='0.0.0.0')