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
import os
import re
import bathcleaning as bc
import easteregg as ee
import adjust

app = Flask(__name__)

# get environment variable
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    info = ''

    if re.search('今日|きょう|きょお|きょー', text):
        bc.init()
        bc.updateGroup()
        info = bc.getReply()
    elif re.search('明日|あした|芦田愛菜|あしだまな', text):
        info = '実装がめんどくさいので明日のグループは見れません'
    elif re.search('猫|ねこ|キャット|cat|cats', text):
        info = ee.cat()
    elif re.search('プリキュア|ぷりきゅあ', text):
        info = ee.pretty_cure()
    elif re.search('おみくじ', text):
        info = ee.omikuji()
    elif re.search(adjust.rePASSWORD, text):
        # for adjust
        if re.search(adjust.reADVANCE, text):
            adjust.advance()
        if re.search(adjust.reRETREAT, text):
            adjust.retreat()
        return
    else:
        info = '今日のグループを知りたい場合は「今日」と送信してください'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=info)
    )


if __name__ == "__main__":
    #  app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
