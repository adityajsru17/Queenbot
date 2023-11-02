from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from MukeshRobot import OWNER_ID, dispatcher
from MukeshRobot import pbot as client

Mukesh = "https://graph.org/file/bae8ca4a24a6902df2e0c.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Mukesh,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

╔═════ஜ۩۞۩ஜ════╗

 ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 [𝐐𝐔𝐄𝐄𝐍'𝐒 𝐒𝐀𝐊𝐇𝐈](https://t.me/𝐪𝐮𝐞𝐞𝐧_𝐬𝐚𝐤𝐡𝐢)♨️
  
╚═════ஜ۩۞۩ஜ════╝

**[𝗤𝗨𝗘𝗘𝗡](t.me/{dispatcher.bot.username}) sᴏᴜʀᴄᴇ ɪs ɴᴏᴛ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📍ᴏᴡɴᴇʀ📍",f"tg://user?id={OWNER_ID}"
                    ),
                    InlineKeyboardButton(
                        "📍ʀᴇᴘᴏ📍",
                        url="https://te.legra.ph/file/2e1ae025e30642b4efe9c.jpg",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "⚡Rᴇᴩᴏ⚡"
_help__ = """
 /repo  ʀᴇᴘᴏ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ʙᴀʙʏ
 /source sᴏʀʀʏ ʙᴜᴛ ʏᴏᴜ ᴄᴀɴ'ᴛ ɢᴇᴛ
"""
