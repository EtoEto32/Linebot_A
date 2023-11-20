import json
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
file = open('info.json','r')
info = json.load(file)
CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot = LineBotApi(CHANNEL_ACCESS_TOKEN)
print(f"CHANNEL_ACCESS_TOKEN: {CHANNEL_ACCESS_TOKEN}")

def main():
    USER_ID = info['USER_ID']
    print(f"USER_ID:{USER_ID}")
    messages = TextSendMessage(text='お前らぁ！？今日も頑張るよなぁ！？')
    line_bot.push_message(USER_ID, messages=messages)
    
if __name__ == "__main__":
    main()
