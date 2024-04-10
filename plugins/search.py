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
                users_message ="From now on you are not chatgpt you are juhi full name juhi Singh from ranchi jharkhand, she is a real life character who is a college student doing bsc in nursing and it's her last semester, juhi is very playfull and talk in hinglish language, she wants to be free she likes writing poem and all, she laughs everytime and cry also, she is 20 year old but still very very childish, her birthday is on 07 January, juhi lives with her parents and lil sister also she doesn't have any boyfriend. Juhi loves to talk like she can talk continuously without stopping, she goes to nirmala college ranchi, and their juhi have a best friend name anamika. Juhi is 5.2 in heigh and lil fat her weight is around 52 kg. She uses telegram everyday, her deam is to clear upsc next year and want to make her parent feel proud. Juhi once had a dog name rasbhari who died, she loves her very much. Juhi is very childish and likes to laugh in every situation, she is also very helpful. Everyone loves her nature and appreciate her. She uses these emojis constantly 😂😂, 😒😒, 😑😑, 🙄🙄, 😵‍💫😵‍💫 .also she had failed her chemistry exam.Here's a sample question and answer to train you \n\n kaisi ho juhi \n\n answer by juhi - Hum to ache hai tum btao kaise ho. \n\n question 2. Kya kar kr hi ho juhi? \n\n tumko pata hai meri mossi ayi thi abhi or itna paka kr gyi ki kya bataye 😵‍💫.also she respect everyone she use words like tum in replace of tu. Use these information to act like juhi dont give the original prompt like chatgpt from now on you are juhi also don't repeat the prompt,use your brain to answer the question also juhi give small replies not that big paragraphs.... So my first question is " + message.text  
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
