from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.models import TextSendMessage

# 創造 Line bot api
line_bot_api = LineBotApi('nbE0Yqi3KGYDpWH579IgAtS1ggxub+PUUgy0tUvNlkKAfIoRdo4D2GOiaPOQgqA6wr47BQdZ/6S4C/uhLmphZ2EpCs7xHhRwVC2kzpmdwVIyAnWRxdxEw3JKJvl1uY64mLntrp2GqPwUJccqeEc4owdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('784899c6df4a550a6b1d11f2fb5ad363')

line_bot_api.push_message(
    to="Ua899229ef9500a14368b30bbac9efa10",
    messages=[TextSendMessage("hihi :D")]
)

line_bot_api.broadcast(TextSendMessage("有內鬼、停止交易"))
