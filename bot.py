import os

import discord
from dotenv import load_dotenv
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# client是跟discord連接，intents是要求機器人的權限
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

# 調用event函式庫
@client.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {client.user}")

@client.event
# 當頻道有新訊息
async def on_message(message):
    # 排除機器人本身的訊息，避免無限循環
    if message.author == client.user:
        return
    # 新訊息包含Hello，回覆Hello, world!
    if message.content == "Hello":
        await message.channel.send("Hello, world!")
    elif message.content == "多空":
        response = requests.post('https://wn48av5xpb.execute-api.ap-northeast-1.amazonaws.com/dev/webhook', json={'message': message.content})
        response_json = response.json()
        print(response_json)
        await message.channel.send(response_json)

client.run(TOKEN)
