from discord.ext import commands
from core.classes import Cog_Extension
import requests
import json
import opencc

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
      await ctx.send("該功能目前無法使用")

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
      await ctx.send("該功能目前無法使用")
      
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
      await ctx.send("該功能目前無法使用")

  @commands.command(name='Orb',aliases=['奧布山谷時間' , '福爾圖娜' , '福爾圖娜時間'])
  async def orbtime(self,ctx):
    try:
      html = requests.get('https://api.warframestat.us/pc/vallisCycle',headers={'Accept-Language':'tc','Cache-Control': 'no-cache'}).text
      data = json.loads(html)
      if(data['state']=='cold'):
        await ctx.send("```ini\n距離溫暖還有：["+data['timeLeft'] + "]```")
      elif(data['state']=='warm'):
        await ctx.send("```ini\n距離寒冷還有：["+data['timeLeft'] + "]```")
    except:
      await ctx.send("該功能目前無法使用")

    #突擊
  @commands.command(name='Sortie',aliases=['突擊' , '突襲'])
  async def sortie(self,ctx):
    try:
      cc = opencc.OpenCC('s2t')
      count = 1
      html_sortie = requests.get('https://api.warframestat.us/pc/zh/sortie',headers={'Accept-Language':'tc','Cache-Control': 'no-cache'})
      data_sortie = json.loads(html_sortie.text)
      await ctx.send(f"```fix\n突擊剩餘時間：{data_sortie['eta']}\n{data_sortie['boss']} 的部隊，{data_sortie['faction']}陣營```")
      for missions in data_sortie['variants']:
        node = cc.convert(missions['node'])
        missionType= cc.convert(missions['missionType'])
        modifier = cc.convert(missions['modifier'])
        await ctx.send(f'```ini\n突擊 [{count}]\n節點：{node} 等級：[{35+15*count} ~ {40+20*count}]\n任務：{missionType}\n狀態：{modifier}```')
        count += 1
    except:
      await ctx.send("該功能目前無法使用")

def setup(bot):
    bot.add_cog(worldstate(bot))