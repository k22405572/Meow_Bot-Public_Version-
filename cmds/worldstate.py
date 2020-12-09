from discord.ext import commands
from core.classes import Cog_Extension
import requests
import json
import chinese_converter
from datetime import datetime


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
      await ctx.send(worldstate.FunctionFail())

    #突擊
  @commands.command(name='Sortie',aliases=['突擊' , '突襲'])
  async def sortie(self,ctx):
    try:
      count = 1
      html_sortie = requests.get('https://api.warframestat.us/pc/zh/sortie',headers={'Accept-Language':'tc','Cache-Control': 'no-cache'})
      data_sortie = json.loads(html_sortie.text)
      await ctx.send(f"```fix\n突擊剩餘時間：{data_sortie['eta']}\n{data_sortie['boss']} 的部隊，{data_sortie['faction']}陣營```")
      for missions in data_sortie['variants']:
        node = chinese_converter.to_traditional(['node'])
        missionType= chinese_converter.to_traditional(missions['missionType'])
        modifier = chinese_converter.to_traditional(missions['modifier'])
        await ctx.send(f'```ini\n突擊 [{count}]\n節點：{node} 等級：[{35+15*count} ~ {40+20*count}]\n任務：{missionType}\n狀態：{modifier}```')
        count += 1
    except:
      await ctx.send(worldstate.FunctionFail())

  @commands.command(name="Arbitration",aliases=['仲裁'])
  async def arbitration(self,ctx):
    raw = requests.get("https://api.warframestat.us/pc/tc/arbitration",headers={'Accept-Language':'zh'})
    text = raw.text
    text = chinese_converter.to_traditional(text)
    data = json.loads(text)
    expiry = data['expiry']
    timeLeft = datetime.strptime(expiry,'%Y-%m-%dT%X.000Z')
    now = datetime.now()
    timeLeft = timeLeft-now
    minutes = int((timeLeft.seconds - timeLeft.seconds%60)/60)
    seconds = timeLeft.seconds%60
    await ctx.send(f"```\n當前仲裁任務(API並不穩定，僅供參考):\n任務:{data['type']}\n節點:{data['node']}\n敵人:{data['enemy']}\n剩餘時間:{minutes}分鐘{seconds}秒```")

class FunctionFail(Exception):
  def __str__(self):
    return '該功能目前無法使用'

def setup(bot):
    bot.add_cog(worldstate(bot))