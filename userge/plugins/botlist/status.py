#MrDayamZaidi

import os
import time
import pytz
import pyrogram
import asyncio
from datetime import datetime
from userge import userge, Message

UpdatesChannel = ("WhiteEyeBots")
Botsz = ["WhiteEyeRenameBot", "WhiteEyeURLUploaderBot", "WhiteEyeTelegraphBot", "WhiteEyeLinkToFileBot", "WhiteEyeSubtitleBot", "WhiteEyeYouTubeBot", "WhiteEyeForceSubscriberBot", "WhiteEyeGDrivebot", "WhiteEyeTagRemoverBot", "WhiteEyeDeleteAllBot", "WhiteEyeCompressorBot", "Miss_ArantxaBot", "WhiteEyeURLShortnerBot", "FilmsRequestBot"]

@userge.on_cmd("botlist", about={
    'header': "Pings All Defined Bots",
    'description': "<b>Ping and Updates The Status Of All Defined Bots In 'BOTSZ' var</b>\n\n"
                   "<b>Available Vars</b>:\n\n<i><code>UPDATES_CHANNEL</code> : Provide Your Channel Name With @"

                   "<code>BOTSZ</code> : Define All Your Bot's Username With Out @ And Seperate Each With ','\n\n"
})
async def bots(message: Message):
    first_msg = "<b>List Of All Bots And Working Status In @WhiteEyeBots</b>\n_______________________________</b>\n\n"
    reply = await message.reply_text(first_msg,parse_mode="html")
    Listed = Botsz
    for bot in Listed:
        checking = f"<b>☘️ @{bot} Status : Checking...♻️</b>\n\n"
        first_msg += checking
        await reply.edit_text(first_msg,parse_mode="html")
        snt = await userge.send_message(bot, '/start')
        time.sleep(5)
        msg = await userge.get_history(bot, 1)
        if snt.message_id == msg[0].message_id:
            nice = f"<b>☘️ @{bot} Status : ❌</b>\n\n"
        else:
            nice = f"<b>☘️ @{bot} Status : ✅</b>\n\n"
        first_msg = first_msg.replace(checking, nice)
        await reply.edit_text(first_msg,parse_mode="html")
        await userge.read_history(bot)
    tz = pytz.timezone('Asia/Kolkata')
    time_now  = datetime.utcnow().astimezone(tz=tz).strftime("%I:%M %p - %d %B %Y")
    first_msg += f"<b>[Last Checked And Updated On : {time_now}]</b>"
    await reply.edit_text(first_msg,parse_mode="html")


