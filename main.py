mport discord
import requests
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv('.env')
TOKEN= os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True

# Edit these!
kmcode = commands.Bot(command_prefix = "!", intents=intents)
#اي دي تشانيل ترحيب
kmchannel_id = 815917819543158824
#اي دي سيرفر 
kmguild_id = 804827461644189726
#لا تلعب بذي 
path = "kmwelcome.png"
#اسم صورة الترحيب 
kmbccname = "Untitled-2.jpg"
#حجم صورة الافاتار 
size = 299
#الالوان النص بصيغة RGB
kr = 87
kb = 179
kg = 227
#احداثيات النص 
t1 = 343
t2 = 481
#حجم الخط 
fs = 87#حجم الخط 
#احداثيات الصورة
p1 = 59
p2 = 58
#كيف تجيبوهم تابعو 
#اول شي نجيب صورة ترحيب 
#نفتحها بالفوتوشوب
#هسا لون الخط
#ببدك لون بصيغة RPG مش HEX 
###############
#KINGMAN INTRO#
###############
kmactivity = 'Welcomer Bot' #Bot Activity By Kingman
kingman_intro = """


     ██╗  ██╗██╗███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
     ██║ ██╔╝██║████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
     █████╔╝ ██║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
     ██╔═██╗ ██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
     ██║  ██╗██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
   ============================================================
   Kingman Welcomer Bot | KMCodes
   =============================================================
   Support server : https://discord.gg/JDCk6FWFqq
   =============================================================
   GitHub : https://github.com/MeKINGMAN
   =============================================================
   Phone Number : +962792914245
   =============================================================
"""
@kmcode.event
async def on_ready():
    await kmcode.change_presence(activity=discord.Game(name=kmactivity))
    print('Kingman Welcomer Login as')
    print(kmcode.user.name)
    print(kmcode.user.id)
    print(discord.__version__)
    print('------')
    print(kingman_intro)
    print('Servers connected to:')
    for guild in kmcode.guilds:
     print(guild.name)
     print ('--------')
     

x = kmcode.get_channel(kmchannel_id)
@kmcode.command()
async def welcome(ctx):
  print("Welcomer Working #1")

  with requests.get(ctx.message.author.avatar_url) as r:
    img_data = r.content
  with open('kmprofile.jpg', 'wb') as handler:
    handler.write(img_data)
  km1 = Image.open(kmbccname)
  km2 = Image.open("kmprofile.jpg")
  draw = ImageDraw.Draw(km1)
  guild = kmcode.get_guild(kmguild_id)
  font = ImageFont.truetype("TektonPro-Bold.otf",fs)
  draw.text((t1, t2),f"{ctx.author.name}",(kr, kb, kg),font=font)
  #draw.text((tt1, tt2),f"Welcome to server",(kr, kb, kg),font=font2)
  km2 = km2.resize((size, size), resample=0)
  kmmask = Image.new("L", km2.size, 0)
  draw = ImageDraw.Draw(kmmask)
  draw.ellipse((0, 0, size, size), fill=255)
  kmmask.save('kmask1.png', quality=95)  
  kmback = km1.copy()
  kmback.paste(km2, (p1, p2), kmmask)#حجم الصورة
  kmback.save('kmwelcome.png', quality=95)
  f = discord.File(path, filename="kmwelcome.png")
  
  

  await kmcode.get_channel(kmchannel_id).send(file=discord.File('kmwelcome.png'))
  await kmcode.get_channel(kmchannel_id).send(f"""
  **  Mr.  {ctx.author.mention}**
  ** YourNumber {guild.member_count}  **
  ** l Read Rule in  [ <#815917821585784895> ] **
""")

  print("Welcomer Working #2")

kmcode.remove_command('help')
@kmcode.event
async def on_member_join(member):
    with requests.get(member.avatar_url) as r:
        img_data = r.content
    with open('kmprofile.jpg', 'wb') as handler:
        handler.write(img_data)
    km1 = Image.open(kmbccname)
    km2 = Image.open("kmprofile.jpg")
    draw = ImageDraw.Draw(km1)
    font = ImageFont.truetype("TektonPro-Bold.otf",fs)
    guild = kmcode.get_guild(kmguild_id)
    draw.text((t1, t2),f"{member.name}",(kr, kb, kg),font=font)
    km2 = km2.resize((size, size), resample=0)
    kmmask = Image.new("L", km2.size, 0)
    draw = ImageDraw.Draw(kmmask)
    draw.ellipse((0, 0, size, size), fill=255)
    kmmask.save('kmask1.png', quality=95)
    kmback = km1.copy()
    kmback.paste(km2, (p1, p2), kmmask)
    kmback.save('kmwelcome.png', quality=95)
    f = discord.File(path, filename="kmwelcome.png")
    await kmcode.get_channel(kmchannel_id).send(file=discord.File('kmwelcome.png'))
    await kmcode.get_channel(kmchannel_id).send(f"""
**  Mr.  {member.mention} **
** YourNumber {guild.member_count}  **
** Read Rule in  [ <#815917821585784895> ]**
""")

kmcode.run(TOKEN)