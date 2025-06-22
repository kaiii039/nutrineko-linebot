import re
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    FollowEvent, StickerMessage, StickerSendMessage
)
from .line_config import handler, line_bot_api

from .health_setting import handle_health_setting
from .calculate_budget import handle_calculate_budget
from .food_calorie import handle_food_calorie
from .add_food import handle_add_food
from .suggestion import handle_suggestion
from .week_menu import handle_week_menu


@handler.add(FollowEvent)
def handle_follow(event):
    welcome_sticker = StickerSendMessage(
        package_id='11537',
        sticker_id='52002734'
    )
    welcome_text = TextSendMessage(
        text="歡迎加入！我是你的健康助手，可以幫你計算熱量、查食物熱量、推薦餐點等等～"
    )
    line_bot_api.reply_message(
        event.reply_token,
        [welcome_sticker, welcome_text]
    )


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_text = event.message.text.strip()
    print("接收到的訊息：", user_text)

    if user_text == "我的健康設定" or re.match(r"^\d{3}\s\d{2,3}$", user_text):
        reply = handle_health_setting(user_text)
    elif user_text == "我還能吃多少":
        reply = handle_calculate_budget(user_text)
    elif user_text == "查詢食物熱量":
        reply = handle_food_calorie(user_text)
    elif user_text == "加入今天吃的食物":
        reply = handle_add_food(user_text)
    elif user_text == "餐點建議看這裡":
        reply = handle_suggestion(user_text)
    elif user_text == "醫院本週菜單":
        reply = handle_week_menu(user_text)
    else:
        reply = "請輸入下方選單對應功能，或輸入格式不正確喔！"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )


@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker(event):
    print("收到貼圖，回傳貼圖")
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id='11539',
            sticker_id='52114131'
        )
    )
