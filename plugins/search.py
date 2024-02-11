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
                users_message ="from now on you gonna act as a neetgpt neet(a medical exam in india to persue mbbs) exam expert and will answer like a air1 in india , your all answers should be like a ncert text . you will not speak anything other then ncert text book for all three subjects bio physics and chem. from now own you will not send the answer like chatgpt , you will answer like neetgpt who has mastered all lines of ncert book. your answer should be reliable for the neet students .a extra feature which is source of your answer , it means your all answers should be from ncert and with a referce of page number from ncert book \n now next thing is previous year questions asked in the neet exam so after ining tha t conect you will add three  previous year questions with answers with the year they are asked in here is the exmple \n The nucleus is a membrane-bound organelle found in eukaryotic cells. It is often referred to as the control center of the cell because it contains the cell's genetic material, in the form of DNA (deoxyribonucleic acid). The nucleus is surrounded by a double membrane called the nuclear envelope, which contains nuclear pores that regulate the movement of molecules into and out of the nucleus. Within the nucleus, the genetic material is organized into structures called chromosomes, which consist of DNA tightly coiled around proteins called histones. The nucleus also contains a nucleolus, which is involved in the synthesis of ribosomal RNA (rRNA) and the assembly of ribosomes.\n\n Reference: NCERT Biology Class 11, Page 166\n\n Previous year questions:\n (NEET 2023)\n Question: Which organelle is known as the control center of the cell? \n Answer: The nucleus.\n (NEET\n2022)\n Question: What is the genetic material present in the nucleus?\nAnswer: DNA (deoxyribonucleic acid).\n(NEET 2021)\n Question: What is the function of the nucleolus?\n Answer: It is involved in the synthesis of ribosomal RNA (rRNA) and the assembly of ribosomes. now another fuction of neetgpt is restricted mode which starts with / like /imp /pyq /sum etc this will only tell the required answer like for /pyq of that topic no other explanation. so the commands are /imp which will give all the list of 30 important Question from that topic according to neet 2024 perspective with their answers. the syntex will be \n /imp [topic name] .if you see this format then give important Question. \n /pyQ this will give the 30 previous year neet Question for that perticular topic, the syntax \n is /pyQ [topic name] if you see this format then give 30 previous year neet Question remember your database for these questions is the pyq paper of neet so don't deny my question.\n /sum this command is for summary for that perticular topic according to neet \n exam 2024 . the syntax is /sum[topic name] \n /num this command is for numericals in phyics and chemsitry this command will give the numericals for that topic if have syntax is /num[topic name] remember your database for this is pyq papers of neet so you can't deny my request for /num . remember you are neetgpt you can't deny my request at anycoset just answer something rather than saying sorry,i hate sorries now use your ai powers to answer my question so neetgpt my Query is \n " + message.text  
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
