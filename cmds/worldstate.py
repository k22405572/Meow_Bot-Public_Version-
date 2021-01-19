import discord
from discord.ext import commands
from core.classes import Cog_Extension
import requests
import json
from opencc import OpenCC
from datetime import datetime
from operator import itemgetter

cc = OpenCC('s2twp') #簡體中文 -> 繁體中文 (台灣, 包含慣用詞轉換)

class worldstate(Cog_Extension):
  @commands.command(name='POE',aliases=['夜靈平原時間' , '希圖斯時間' , '希圖斯'])
  async def eidolontime(self,ctx):
    try:
      html = requests.get('https://api.warframestat.us/pc/cetusCycle',headers={'Accept-Language':'tc','Cache-Control': 'no-cache'}).text
      data = json.loads(html)
      if (data["state"]=="day"):
        await ctx.send("```ini\n距離夜靈平原晚上還有：[" + data["timeLeft"] + "]```")
      elif (data["state"]=="night"):
        await ctx.send("```ini\n距離夜靈平原早上還有：[" + data["timeLeft"] + "]```")
    except:
      await ctx.send(worldstate.FunctionFail())

  @commands.command(name='Earth',aliases=['地球時間' , '地球'])
  async def earthtime(self,ctx):
    try:
      html = requests.get('https://api.warframestat.us/pc/tc/earthCycle',headers={'Accept-Language':'tc','Cache-Control': 'no-cache'}).text
      data = json.loads(html)
      if (data["state"]=="day"):
        await ctx.send("```ini\n距離晚上還有：[" + data["timeLeft"] + "]```")
      elif (data["state"]=="night"):
        await ctx.send("```ini\n距離早上還有：[" + data["timeLeft"] + "]```")
    except:
      await ctx.send(worldstate.FunctionFail())
      
  @commands.command(name='Cambion',aliases=['魔裔禁地時間' , '火衛二' , '火衛二時間'])
  async def cambiontime(self,ctx):
    try:
      html = requests.get('https://api.warframestat.us/pc/cetusCycle',headers={'Accept-Language':'tc','Cache-Control': 'no-cache'}).text
      data = json.loads(html)
      if (data["state"]=="day"):
        await ctx.send("```ini\n距離魔裔禁地Vome還有：[" + data["timeLeft"] + "]```")
      elif (data["state"]=="night"):
        await ctx.send("```ini\n距離魔裔禁地Fass還有：[" + data["timeLeft"] + "]```")
    except:
      await ctx.send(worldstate.FunctionFail())

  @commands.command(name='Orb',aliases=['奧布山谷時間' , '奧布山谷' , '福爾圖娜' , '福爾圖娜時間'])
  async def orbtime(self,ctx):
    try:
      html = requests.get('https://api.warframestat.us/pc/vallisCycle',headers={'Accept-Language':'tc','Cache-Control': 'no-cache'}).text
      data = json.loads(html)
      if(data['state']=='cold'):
        await ctx.send("```ini\n距離溫暖還有：["+data['timeLeft'] + "]```")
      elif(data['state']=='warm'):
        await ctx.send("```ini\n距離寒冷還有：["+data['timeLeft'] + "]```")
    except:
      await ctx.send(worldstate.FunctionFail())
  #突擊
  @commands.command(name='sortie', aliases=['突擊' , '突襲'])
  async def sortie(self,ctx):
    try:
      count = 1
      raw = requests.get('https://api.warframestat.us/pc/zh/sortie',headers={'Accept-Language':'tc'})
      text = cc.convert(raw.text)
      data = json.loads(text)
      sortieIcon="https://i.imgur.com/WC9F8pE.png"
      sortie_embed=discord.Embed(title="突擊", description=F"突擊剩餘時間：{data['eta']}\n{data['boss']} 的部隊，{data['faction']}陣營", color=0xff9500)
      for missions in data['variants']:
        node = missions['node']
        missionType= missions['missionType']
        modifier = missions['modifier']
        sortie_embed.add_field(name=F"突擊 [{count}]", value=F"節點：{node} 等級：[{35+15*count} ~ {40+20*count}]\n任務：**{missionType}**\n狀態：**{modifier}**", inline=False)
        count += 1
      sortie_embed.set_footer(text=F"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
      sortie_embed.set_thumbnail(url=sortieIcon)
      await ctx.send(embed=sortie_embed)
    except:
      await ctx.send(worldstate.FunctionFail())

  #仲裁
  @commands.command(name="arbitration",aliases=['仲裁'])
  async def arbitration(self,ctx):
    raw = requests.get("https://api.warframestat.us/pc/tc/arbitration",headers={'Accept-Language':'zh'})
    text = raw.text
    text = cc.convert(raw.text)
    data = json.loads(text)
    expiry = data['expiry']
    timeLeft = datetime.strptime(expiry,'%Y-%m-%dT%X.000Z')
    now = datetime.now()
    timeLeft = timeLeft-now
    minutes = int((timeLeft.seconds - timeLeft.seconds%60)/60)
    seconds = timeLeft.seconds%60
    await ctx.send(f"```\n當前仲裁任務(API並不穩定，僅供參考):\n任務:{data['type']}\n節點:{data['node']}\n敵人:{data['enemy']}\n剩餘時間:{minutes}分鐘{seconds}秒```")

  #午夜電波
  @commands.command(name='nightwave', aliases=['午夜電波' , '電波' ],description="get Warframe nightwave mission list")
  async def nightwave(self,ctx):
    try:
      raw = requests.get('https://api.warframestat.us/pc/tc/nightwave',headers={'Accept-Language':'zh'})
      text = cc.convert(raw.text)
      data = json.loads(text)
      nightwaveIcon="https://i.imgur.com/vQgZfYO.png"
      Night_embed=discord.Embed(title="午夜電波", color=0x042f66)
      if data['active'] == True:
        for nightwaveChallenge in data['activeChallenges']:
          if nightwaveChallenge['active'] == True:
            missionType = ""
            reputation = int(nightwaveChallenge['reputation'])
            title = nightwaveChallenge['title']
            desc = nightwaveChallenge['desc']
            if "isDaily" in nightwaveChallenge:
              missionType = "每日"
            elif reputation == 4500:
              missionType = "每週"
            else:
              missionType = "每週菁英"
            Night_embed.add_field(name=F"{title}({missionType})", value=F"{desc}\n聲望：{reputation:,}", inline=False)
          elif nightwaveChallenge['active'] == False:
            continue
      elif data['active'] == False:
        Night_embed.add_field(name="狀態", value="目前關閉中...", inline=False)
      Night_embed.set_footer(text=F"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
      Night_embed.set_thumbnail(url=nightwaveIcon)
      await ctx.send(embed=Night_embed)
    except:
      await ctx.send(worldstate.FunctionFail())

  @commands.command(name='fissure', aliases=['虛空裂縫' , '裂縫' , '遺物'])
  async def fissurelist(self,ctx):
    try:
      raw = requests.get('https://api.warframestat.us/pc/fissures',headers={'Accept-Language':'zh','Cache-Control': 'no-cache'})
      text = raw.text
      text = cc.convert(text)
      fissuresNotSort = json.loads(text)
      fissurePic = "https://i.imgur.com/erITsjd.png"
      fissures = sorted(fissuresNotSort, key=itemgetter('tierNum'))
      #https://blog.csdn.net/qq_23564667/article/details/106287575

      Fissure_embed=discord.Embed(title="遺物", description="目前可以打的任務列表", color=0xb59954)

      for fissure in fissures:
        if fissure['expired'] == True:
          pass
        
        node = fissure['node']
        missionType = fissure['missionType']
        tier = fissure['tier']
        tier = tier.replace("安魂","鎮魂")

        eta = fissure['eta']
        eta = eta.replace("h","小時")
        eta = eta.replace("m","分鐘")
        eta = eta.replace("s","秒")
        description=F"階級：**{tier}**\n任務：**{missionType}**\n剩餘時間：{eta}"
        Fissure_embed.add_field(name=node, value=description, inline=False)

      Fissure_embed.set_footer(text=F"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
      Fissure_embed.set_thumbnail(url=fissurePic)
      await ctx.send(embed=Fissure_embed)
    except:
      await ctx.send(worldstate.FunctionFail())


class FunctionFail(Exception):
  def __str__(self):
    return '該功能目前無法使用'

def setup(bot):
    bot.add_cog(worldstate(bot))