from linebot import (
    LineBotApi, WebhookHandler
)
import json
from linebot.models import RichMenu

from linebot.models import TextSendMessage

# 創造 Line bot api
line_bot_api = LineBotApi('nbE0Yqi3KGYDpWH579IgAtS1ggxub+PUUgy0tUvNlkKAfIoRdo4D2GOiaPOQgqA6wr47BQdZ/6S4C/uhLmphZ2EpCs7xHhRwVC2kzpmdwVIyAnWRxdxEw3JKJvl1uY64mLntrp2GqPwUJccqeEc4owdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('784899c6df4a550a6b1d11f2fb5ad363')

# 1. 拿設定檔去申請圖文選單

# 讀取JSON檔 (從秉鴻老師的Git直接co model來用)
# with open("rich_menu.json", "r", encoding="utf-8") as json_file:
#     rich_menu_json_object = json.load(json_file)
#
# # 將JSON格式做成RichMenu的變數
# rich_menu_config = RichMenu.new_from_json_dict(rich_menu_json_object)
# # line_bot_api 上傳至 line
# rich_menu_id = line_bot_api.create_rich_menu(rich_menu_config)
#
# print(rich_menu_id)
# # id: richmenu-78ad63efe03e98d87c0a596195d6f951

# 2. 把圖片傳給指定的選單id

# rich_menu_id = "richmenu-78ad63efe03e98d87c0a596195d6f951"
# with open("rich_menu.jpg", "rb") as image_file:
#     response = line_bot_api.set_rich_menu_image(
#         rich_menu_id=rich_menu_id,
#         content_type="image/jpeg",
#         content=image_file
#     )

# 3. 綁定用戶與圖文選單
#
# rich_menu_id = "richmenu-78ad63efe03e98d87c0a596195d6f951"
# line_bot_api.link_rich_menu_to_user(
#     user_id="Ua899229ef9500a14368b30bbac9efa10",
#     rich_menu_id=rich_menu_id
# )

# 4. 解除綁定
# line_bot_api.unlink_rich_menu_from_user(
#     user_id="Ua899229ef9500a14368b30bbac9efa10"
# )

# 5. 刪除圖文選單
rich_menu_id = "richmenu-78ad63efe03e98d87c0a596195d6f951"
line_bot_api.delete_rich_menu(rich_menu_id=rich_menu_id)
