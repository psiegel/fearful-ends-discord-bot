import discord
import json

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as', self.user)

  async def on_message(self, message):
    # don't respond to self
    if message.author == self.user:
      return

    if message.content == '!ping':
      await message.channel.send('pong')


f = open('auth.json')
auth = json.load(f)
f.close()

client = MyClient()
client.run(auth['token'])