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
    await m.reply_photo(f"https://te.legra.ph/file/1185ee6df11c7371254a1.jpg",
        caption="*Jᴀɪ sʜʀᴇᴇ ʀᴀᴍ** 👋\n\n** I ᴀᴍ sʜʀᴇᴇ Rᴀᴍ ɢᴘᴛ **\n\n **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[𝗙𝘂𝗻𝘀𝗵𝗶𝗻𝗲](https://t.me/A_r_e_a_5_1)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('💝ᴅᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/a_r_e_a_5_1')
                    ],  
                
                ]
            )
        )
  
