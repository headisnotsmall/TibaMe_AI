from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, ImageSendMessage,
    TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction,
    FlexSendMessage, BubbleContainer, ImageComponent,
    QuickReply, QuickReplyButton, LocationAction,
    ImageMessage, VideoMessage
)
import json
import rich_menu_demo
app = Flask(__name__)





@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=Truce)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# 告知 handler 若收到關注事件、則取個資並 print 出來
# 取得個資後利用 json 模組建檔，將python變數儲存成檔案，並用with存入指定檔案
# 回傳文字以讓用戶感受到回饋
# 傳送案件範本消息給用戶
# 生成範本訊息、並交還給line_bot_api
# template: Carousel, Button, Confirm, ImageCarousel
@handler.add(FollowEvent)
def handle_follow(event):
    user_profile = line_bot_api.get_profile(event.source.user_id)
    with open("namelist.txt", "a") as myfile:
        myfile.write(
            json.dumps(
                vars(user_profile)
            )
        )

        myfile.write("\r\n")

    # 建立文字消息
    follow_text_send_message = TextSendMessage("Gotcha!")

    # 透過 line_bot_api 把文字訊息交給 line
    # line_bot_api.reply_message(event.reply_token, follow_text_send_message)
    image_message = ImageSendMessage(
        original_content_url="https://images.plurk.com/4ukIDnqYl5okkXDeqvj5XP.png",
        preview_image_url="https://images.plurk.com/30gHSki8dVvFhyAhTqXGx.png"
    )

    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.pinimg.com/236x/ba/d8/44/bad844b8c603a0afa3e622c75bc5a32a--princess-disney-disney-fan.jpg',
            title='Who am I',
            text='select the correct answer',
            actions=[
                MessageAction(
                    label='Woody',  # 按鍵名稱
                    text='I guess Woody'  # 點擊後、以用戶發的文字
                ),
                # URIAction(
                #     label="Plurk",
                #     uri="http://www.plurk.com/headisnotsmall"
                # ),
                # URIAction(
                #     label="Call me maybe",  # 透過點擊方式打電話
                #     uri="tel://0929122033"  # url scheme line, 也能使用line的功能
                # ),
                URIAction(
                    label="picture",
                    uri="https://line.me/R/nv/camera/"
                ),
                # PostbackAction(
                #     label="ya",
                #     text="try something",
                #     data="specific"
                # )
            ]
        )
    )

    # 用 JSON 生成模板 讀取本地JSON檔案，用json.load
    with open("sendmessage.json", "r", encoding="utf-8") as jsonfile:
        json_object = json.load(jsonfile)

    template_message_from_json = TemplateSendMessage.new_from_json_dict(json_object)

    with open("flexmessage.json", "r", encoding="utf-8") as jsonfile2:
        json_object2 = json.load(jsonfile2)

    flex_message_from_json2 = FlexSendMessage.new_from_json_dict(json_object2)

    line_bot_api.reply_message(event.reply_token, [follow_text_send_message,
                                                   template_message_from_json,
                                                   flex_message_from_json2])


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    # reply_text_message = TextSendMessage(event.message.text)

    # 創造一個QuickReplyButton
    text_quickreply = QuickReplyButton(action=MessageAction(label="小馮怎麼叫", text="AAA"))
    location_quickreply = QuickReplyButton(action=LocationAction(label="where are you?"))

    # 創造一個QuickReplyButton array，放入剛剛的Button
    quick_reply_array = QuickReply(items=[text_quickreply, location_quickreply])

    reply_text_message = TextSendMessage(event.message.text, quick_reply=quick_reply_array)

    line_bot_api.reply_message(event.reply_token, reply_text_message)


# 告知 handler 收到的指令使用 postback event 進行後續操作
# 判斷 postback data、若為 specific 則取其個資
# @handler.add(PostbackAction)
# def handle_postback_event(event):
#     if event.postback.data == "specific":
#         user = line_bot_api.get_profile(event.source.user_id)
#         app.logger.info(user)

# 當用戶發送圖片消息、用文字消息回應他
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):

    # 用戶圖片消息id
    message_id = event.message.id

    # 變成文字消息
    image_id_text_send_message = TextSendMessage(text=message_id)

    # 將文字訊息傳回給用戶
    # 存圖片需要用二進位的方式存取，但content_file非二進制
    # 因此需要用iter_content()轉換格式、再寫入檔案
    line_bot_api.reply_message(event.reply_token, image_id_text_send_message)
    content_file = line_bot_api.get_message_content(message_id)
    with open(message_id + ".jpg", "wb") as photo:
        for chunk in content_file.iter_content():
            photo.write(chunk)


@handler.add(MessageEvent, message=VideoMessage)
def handle_video_message(event):

    video_content = line_bot_api.get_message_content(event.message.id)

    # 將文字訊息傳回給用戶
    # 存圖片需要用二進位的方式存取，但content_file非二進制
    # 因此需要用iter_content()轉換格式、再寫入檔案
    with open(event.message.id + ".mp4", "wb") as vediofile:
        for chunk in video_content.iter_content():
            vediofile.write(chunk)

    line_bot_api.reply_message(event.reply_token, TextSendMessage("影片已存到我的D槽"))


# print(user_profile)
# print(user_profile.user_id)
# print(user_profile.display_name)
# print(user_profile.status_message)
# print(user_profile.picture_url)


# 預設 handler 執行項目
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
