import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file=open('info.json',"r")
info=json.load(file)

CHANNEL_ACCESS_TOKEN=info['CHANNEL_ACCESS_TOKEN']
# channel access tokenを読み込み

line_bot_api=LineBotApi(CHANNEL_ACCESS_TOKEN)
# linebotapiをインスタンス化

def main():
    USER_ID=info['USER_ID']
    # 誰に送るか、をここで明記したよ。
    messages=TextSendMessage(text='testです')
    line_bot_api.push_message(USER_ID,messages)
    # 引数に、「誰に」「なんのメッセージ」を記載

if __name__ =="__main__":
    main()