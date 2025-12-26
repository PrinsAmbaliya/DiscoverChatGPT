# application_id=1424731524133158963
# public_id=1986db463f56c87eb55b2a408522ae89035850cda5c95aaebfb6a5009647f864 
# token_id=MTQyNDczMTUyNDEzMzE1ODk2Mw.GJ9FIk.E2DWhzjtrxMO0r7gD5HR17XwCB2s7-O3XA-mbY

import discord
import os
import sys
from groq import Groq
from dotenv import load_dotenv

load_dotenv("token.evn")

token = os.getenv("DISCORD_TOKEN")
api_key = os.getenv("GROQ_API_KEY")
if not token or not api_key: sys.exit("Missing keys")

groq_client = Groq(api_key=api_key)
with open("requirmnet.txt","r") as f:
    memory=f.read()
memory = {}

class MyClient(discord.Client):
    async def on_ready(self):
        self.bot_user = self.user
        print(f'Logged on as {self.bot_user}!')

    async def on_message(self, message):
        if message.author == self.bot_user:
            return
        if message.content.lower() == 'ping':
            await message.channel.send('pong'); 
            return
        if not self.bot_user.mentioned_in(message): 
            return

        content = message.content.replace(f"<@{self.bot_user.id}>", "").strip()
        thinking = await message.channel.send("Thinking...")

        try:
            if content.lower().startswith("remember"):
                parts = content.split()
                if len(parts) >= 3: 
                    memory[parts[1]] = " ".join(parts[2:])
                await thinking.edit(content=f"Remembered {parts[1]} = {memory.get(parts[1],'')}")
            elif content.lower().startswith("what is"):
                expr = content.lower().replace("what is","").strip()
                key = expr.split()[-1]
                if key in memory:
                    await thinking.edit(content=memory[key])
                else:
                    try: 
                        await thinking.edit(content=str(eval(expr)))
                    except: 
                        await thinking.edit(content=f"I don't know {expr}")
            else:
                resp = groq_client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{
                        "role":"user",
                        "content":content}],
                    temperature=1, 
                    max_tokens=8192, 
                    top_p=1, 
                    stream=False
                ).choices[0].message.content
                if len(resp) > 2000:
                    await thinking.delete()
                    for i in range(0, len(resp), 2000):
                        await message.channel.send(resp[i:i+2000])
                else:
                    await thinking.edit(content=resp)
        except Exception as e:
            await thinking.edit(content=f"Error: {str(e)}")

intents = discord.Intents.default()
intents.message_content = True
MyClient(intents=intents).run(token)
