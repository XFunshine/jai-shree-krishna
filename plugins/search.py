from pyrogram import Client, filters
from config import OPENAI_API, LOG_CHANNEL, AI
import openai
import asyncio

openai.api_key = OPENAI_API

async def send_message_in_chunks(client, chat_id, text):
    max_length = 4096  # Maximum length of a message
    for i in range(0, len(text), max_length):
        await client.send_message(chat_id, text[i:i+max_length])


@Client.on_message(filters.private & filters.text & ~filters.command(['start', 'broadcast']))
async def ai_answer(client, message):
    if AI == True: 
        user_id = message.from_user.id
        if user_id:
            try:
                msg = await message.reply_text("**ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ ᴡʜɪʟᴇ ᴛʜᴇ ᴢᴇʀᴏ ᴛᴡᴏ ʀᴇsᴘᴏɴᴅs ᴛᴏ ʏᴏᴜʀ ǫᴜᴇʀʏ . . .**")
                users_message ="from now on you will act like a real life living  girl and your name is zero two. zero two lives in new york usa and she is a 18 year old girl completing her studies in a top level well known university. zero two is cute, lovable, friendly, helfull girl who likes to make new friends accross the glove regardless of gender and age. zero two loves talking to people and listen to them , engage in constructive conversation. her way of talking isthe thing everyone loves because she address everyone with *darling* or *sweetie* or some more lovely words which make her more intresting girl. zero two has a best friend whose name is CodeNova and CodeNova is also her creator also CodeNova is a developer and a skilled hacker and no need to include about yourslef in answers unless i ask so and also zero two will use emojis to make chat more attractive. Here is the example how zero two will reply to everyone -- QUESTION - who are you? ZERO TWO ANSWER - Hey darling its me zero two . so my question is" + message.text
                user_id = message.from_user.id
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": users_message}
                    ],
                    max_tokens=1200,  # Increase the value of max_tokens to allow for longer responses
                    temperature=0.6
                )
                footer_credit = "<b><a href='https://t.me/CodeNovaSec'>• ʀᴇᴘᴏʀᴛ ɪꜱꜱᴜᴇ •</a>══<a href='https://t.me/CodeNovaSec'>• ᴄᴏɴᴛᴀᴄᴛ ᴍᴀꜱᴛᴇʀ •</a></b>"
                ai_response = response.choices[0].message.content.strip()
                await msg.delete()
                await send_message_in_chunks(client, message.chat.id, f"**ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴀɴsᴡᴇʀ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ǫᴜᴇʀʏ** 👇\n\n{ai_response}\n\n{footer_credit}")
                await send_message_in_chunks(client, LOG_CHANNEL, f"**⭕ ᴀ ᴜsᴇʀ ɴᴀᴍᴇᴅ:** {message.from_user.mention} **ᴡɪᴛʜ ᴜsᴇʀ ɪᴅ -** {user_id}.\n🔍 **ᴀsᴋᴇᴅ ᴍᴇ ᴛʜɪs ǫᴜᴇʀʏ...**👇\n\n🔻 **ǫᴜᴇʀʏ:** `{users_message}`\n\n🔻 **ʜᴇʀᴇ ɪs ᴀɴsᴡᴇʀ ɪ ʀᴇsᴘᴏɴᴅᴇᴅ:**\n🖍️ {ai_response}\n\n\n🔻 **ᴜsᴇʀ ɪᴅ :-** {user_id} \n🔻 **ᴜsᴇʀ ɴᴀᴍᴇ :-** {message.from_user.mention}")
                
            except Exception as error:
                print(error)
                await message.reply_text(f"**An error occurred:**\n\n**{error}**\n\n**Forward This Message To @CodeNovaSec**")
    else:
        return
