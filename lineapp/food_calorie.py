from linebot.models import FlexSendMessage


def handle_food_calorie(user_text: str) -> str:
    return "嘿嘿嘿嘿嘿嘿想查嗎"

# def handle_food_calorie(user_text: str) -> FlexSendMessage:
#     flex_content = {
#         "type": "bubble",
#         "body": {
#             "type": "box",
#             "layout": "vertical",
#             "spacing": "md",
#             "contents": [
#                 {
#                     "type": "text",
#                     "text": "請選擇食物種類",
#                     "weight": "bold",
#                     "size": "lg"
#                 },
#                 {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "spacing": "md",
#                     "contents": [
#                         {
#                             "type": "button",
#                             "style": "primary",
#                             "color": "#67C23A",
#                             "action": {
#                                 "type": "message",
#                                 "label": "素食",
#                                 "text": "素食"
#                             }
#                         },
#                         {
#                             "type": "button",
#                             "style": "primary",
#                             "color": "#F56C6C",
#                             "action": {
#                                 "type": "message",
#                                 "label": "葷食",
#                                 "text": "葷食"
#                             }
#                         }
#                     ]
#                 }
#             ]
#         }
#     }
#
#     return FlexSendMessage(alt_text="請選擇食物種類", contents=flex_content)