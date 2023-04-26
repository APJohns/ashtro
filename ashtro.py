import discord
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class MyClient(discord.Client):
  # Get the astronomy pic of the day
  async def __apod(self, message):
    res = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={os.environ["NASA_KEY"]}')
    apod = res.json()
    title = apod['title']
    url = apod['hdurl'] if 'hdurl' in apod else apod['url']
    explanation = apod['explanation']
    await message.channel.send(title + '\n```\n' + explanation + '\n```\n' + url)

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    if message.content == '/apod':
      await self.__apod(message)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.environ['TOKEN'])