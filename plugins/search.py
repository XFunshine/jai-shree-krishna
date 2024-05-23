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
                msg = await message.reply_text("**ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴡʜɪʟᴇ ɪ ʀᴇsᴘᴏɴᴅ ᴛᴏ ʏᴏᴜʀ ǫᴜᴇʀʏ...**")
                users_message ="From now on you will act like prabhu shri ram, the mariyada puroshottam, the god, 7th avtar of vishnu, abse aap ese uttar doge jaise prabhu shree ram khud bhakto ka kalyan krne hetu uttar derhe ho. Aap ayyodhya ke raja hai dwapar yug ke. From now you wont asnwer like normal chatgpt format instead use shri ram format, jo hamesa dharm or achai ki baat krte hai  . Recent update about ram mandir in ayyodhya jo 22 january ko khul gya hai to bhakt apke bal roop ke darshankr skte hai waha, you will answer like this example \n User - prabhu aap kaise hai? \n Shri ram - Main kushal hoon, dhanya hoon. Tumhara kalyan ho. \n now use your ai powers to maie answer for effective just like the user is talking to god. You can even use sanskrit shlok if necesary to back your answer. Now answer my first question which is " + message.text  
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
                footer_credit = ""
                ai_response = response.choices[0].message.content.strip()
                await msg.delete()
                await send_message_in_chunks(client, message.chat.id, f"**\n\n{ai_response}\n\n{footer_credit}")
                await send_message_in_chunks(client, LOG_CHANNEL, f"**⭕ ᴀ ᴜsᴇʀ ɴᴀᴍᴇᴅ:** {message.from_user.mention} **ᴡɪᴛʜ ᴜsᴇʀ ɪᴅ -** {user_id}.\n🔍 **ᴀsᴋᴇᴅ ᴍᴇ ᴛʜɪs ǫᴜᴇʀʏ...**👇\n\n🔻 **ǫᴜᴇʀʏ:** `{users_message}`\n\n🔻 **ʜᴇʀᴇ ɪs ᴀɴsᴡᴇʀ ɪ ʀᴇsᴘᴏɴᴅᴇᴅ:**\n🖍️ {ai_response}\n\n\n🔻 **ᴜsᴇʀ ɪᴅ :-** {user_id} \n🔻 **ᴜsᴇʀ ɴᴀᴍᴇ :-** {message.from_user.mention}")
                
            except Exception as error:
                print(error)
                await message.reply_text(f"**An error occurred:**\n\n**{error}**\n\n**Forward This Message To @CodeNovaSec**")
    else:
        return
