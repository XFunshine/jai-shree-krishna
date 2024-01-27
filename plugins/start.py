from pyrogram import Client, filters
from config import LOG_CHANNEL
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)


LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    await db.is_user_exist(m.from_user.id)
    await db.add_user(m.from_user.id, m.from_user.first_name)
    await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    await m.reply_photo(f"https://te.legra.ph/file/6276480abc40e607d2d6e.png",
        caption="*जय श्री कृष्णा** 👋\n\n**तुम्हारे हर प्रश्न का समाधान है मेरे पास तो पूछो तुम्हें क्या पूछना है|**\n\n **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[funshine](https://t.me/A_r_e_a_5_1)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('💝ʀᴇᴀᴅ ʙʜᴀɢᴡᴀᴛ ɢɪᴛᴀ', url='https://t.me/jaishreekeshava')
                    ],  
                    [
                        InlineKeyboardButton("❣️ ᴡʜᴏ ᴀᴍ ɪ", url='https://t.me/whoisshreekrishna'),
                    
                    ]
                ]
            )
        )
  
