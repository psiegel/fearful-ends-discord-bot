import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as', self.user)

  async def on_message(self, message):
    # don't respond to self
    if message.author == self.user:
      return

    if message.content == '!ping':
      await message.channel.send('pong')

client = MyClient()
client.run('OTQ1NjY2NjAzNzA4NzI3MzI2.YhTepw.ufjJDJV3Wa5aFS-fQFBS7pQOEIs')