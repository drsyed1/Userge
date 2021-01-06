import os
import time
import datetime

import pyrogram
    
user_session_string = "BQCQX5yd3ipFkANBGiquKBfn851U9-i_rl9By2pDVU59RdgBayy8-sX5ape6oPisaQDpZCgBDHQwO1BkbP6IxecUrAOgcWnfNZGt_khgJqTZIsri5X4aYjXJKW0XETfQxMhYV4ZRYfjhE_Nle8jXKnw_pOifsQ9C0HhySsgvcs3Mxrup8fW4i07fxFjCMM2iN24G9xvC90jhUs8Nib7kkdwtid_-7jell2cge_I7CKDhA9W79NJLok755_maoI1GPG2hcWGTb6w3bqr43lHNC6rsM-LR_zmLBW0OkDTrO7xD1DDNtvhsvBAaBZReTI5-m2415F45GF7r6-19oqCkBpDJUbEaEQA"
bots = ["WhiteEyeRenameBot", "WhiteEyeURLUploaderBot", "WhiteEyeTelegraphBot", "WhiteEyeLinkToFileBot", "WhiteEyeSubtitleBot", "WhiteEyeYouTubeBot", "WhiteEyeForceSubscriberBot", "whiteeyegdrivebot", "WhiteEyeTagRemoverBot", "WhiteEyeUltraTonBot", "WhiteEyeDeleteAllBot", "WhiteEyeCompressorBot", "Miss_ArantxaBot"]
bot_owner = ("@Mr_StarLords")
update_channel = (-1001484903966)
status_message_id = (243)
api_id = ("2412622")
api_hash = ("fa25ca6c7d6723ea717eee08e6af6565")

user_client = pyrogram.Client(
    user_session_string, api_id=api_id, api_hash=api_hash)


@pyrogram.Client.on_message(pyrogram.filters.command(["checkstatus"])) # Reply on /checkstatus command
async def check_status(client, message):
    first_msg = "<b>Bots Status...</b>\n\n"
    msg = await message.reply_text(first_msg, parse_mode="html")
    bots = ["WhiteEyeRenameBot", "WhiteEyeURLUploaderBot", "WhiteEyeTelegraphBot", "WhiteEyeLinkToFileBot", "WhiteEyeSubtitleBot", "WhiteEyeYouTubeBot", "WhiteEyeForceSubscriberBot", "whiteeyegdrivebot", "WhiteEyeTagRemoverBot", "WhiteEyeUltraTonBot", "WhiteEyeDeleteAllBot", "WhiteEyeCompressorBot", "Miss_ArantxaBot"] #List of your bots
    
    for bot in bots:
        checking = f"<b>⭕️ {bot} Status : ♻️</b>\n\n"
        first_msg += checking
        await msg.edit_text(first_msg, parse_mode="html")
        send = user_client.send_message(bot, '/start')
        time.sleep(8) #You can change it if you need to increase Checking time.
        bot_msg = user_client.get_history(bot, 1)
    
        if send.message_id == bot_msg[0].message_id:
           nice = f"<b>⭕️ {bot} Status : ❌</b>\n\n"
        else:
       nice = f"<b>⭕️ {bot} Status : ✅</b>\n\n"
    
    first_msg = first_msg.replace(checking, nice)
    await msg.edit_text(first_msg,parse_mode="html")
    user_client.read_history(bot)

tz = timezone('Asia/Kolkata')
time_now  = datetime.utcnow().astimezone(tz=tz).strftime("%I:%M %p - %d %B %Y")
first_msg += f"<code>[Updated on : {time_now} IST]</code>"
await msg.edit_text(first_msg,parse_mode="html")
