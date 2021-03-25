from dotenv import load_dotenv
load_dotenv()
import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

APPLICANT_DATA = {
  "ign": [],
  "age": [],
  "reason": []
}

@client.event
async def on_member_join(member):
 # APPLICANT_TABLE[member.id].append(APPLICANT_DATA)
  print('Member joined, sending application')
  if member.dm_channel:
    return

  await member.create_dm() 
  await member.dm_channel.send('IGN:')

@client.event
async def on_message(message):
  if message.author.id is client.user.id:
    return

  whitelist = client.get_channel(823123365279301643)
  if isinstance(message.channel, discord.channel.DMChannel):
    if APPLICANT_DATA["ign"] == []:
      APPLICANT_DATA["ign"].append(message.content)
      await message.channel.send('Hey! Welcome to Lasagn :tada:! Please read the rules in the rules channel, and fill out this bots questions!')
      await whitelist.send(message.content)  

#    print (APPLICANT_DATA.items())
    # for key, value in APPLICANT_DATA.items():
    #   print(key,value)
 

 # if message.channel is discord.DMchannel

client.run(os.getenv('TOKEN'))