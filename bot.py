
import os

import discord

import openai

with open("chat.txt","r") as f:
  chat = f.read()

token = os.getenv("SECRET_KEY")

openai.api_key = os.getenv("API_KEY")

# taken from discord documentation
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        #print(f'Message from {message.author}: {message.content}')
        global chat
        chat += f"{message.author}: {message.content}\n"
      
        if self.user!= message.author:
          if self.user in message.mentions:  # just poke the bot by user  
              response = openai.Completion.create(
                model="gpt-3.5-turbo-instruct",
                prompt=f"{chat}\nRamGPT: ",
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
              )
            
              channel = message.channel
              message_send = response.choices[0].text     
              await channel.send(message_send)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)

