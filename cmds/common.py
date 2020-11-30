from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
from random import randint
import requests
import opencc


with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

try:
  html_eidolon = requests.get('https://api.warframestat.us/pc/cetusCycle')
  if html_eidolon.status_code != 200:
    print("API出錯！")
  else:
    data_eidolon = json.loads(html_eidolon.text)
  #-------------------------------------------------------------------------
  html_vallis = requests.get('https://api.warframestat.us/pc/vallisCycle')
  if html_vallis.status_code != 200:
    print("API出錯！")
  else:
    data_vallis = json.loads(html_vallis.text)
  #-------------------------------------------------------------------------
  html_earth = requests.get('https://api.warframestat.us/pc/tc/earthCycle')
  if html_vallis.status_code != 200:
    print("API出錯！")
  else:
    data_earth = json.loads(html_earth.text)
  #-------------------------------------------------------------------------
  html_cambion = requests.get('https://api.warframestat.us/pc/cambionCycle')
  if html_vallis.status_code != 200:
    print("API出錯！")
  else:
    data_cambion = json.loads(html_cambion.text)
except:
  print("來源失效")

class Common(Cog_Extension):
    #ping
    @commands.command(name= 'ping', aliases=['延遲' , '機器人延遲' , 'delay'])
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} 毫秒 (ms)')

    #隨機傳送圖片網址
    @commands.command(name= 'picture', aliases=['pic' , '圖片'])
    async def picture(self,ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)
    #查詢user資訊
    @commands.command(name= 'user', aliases=['使用者資訊' , '用戶資訊'])
    async def user(self,ctx):
        arg = ctx.message.channel
        args = str(arg).split(' ')
        CMD = 'Direct Message with'
        CMDs = CMD.split(' ')
        msg = 'Author:'+str(ctx.message.author)+'\nAuthor ID:'+ str(ctx.message.author.id)+'\nChannel:'+str(ctx.message.channel)+'\nChannel ID:'+str(ctx.message.channel.id)
        if CMDs[0] == args[0] and CMDs[1] == args[1] and CMDs[2] == args[2]:
            print('私人訊息')
            await ctx.send(msg)
        else:
            print('群組訊息')
            msg = msg +'\nGuild.owner:'+str(ctx.guild.owner) +'\nGuild.owner_id:' +str(ctx.guild.owner_id)+'\nGuild.name:' +str(ctx.guild.name)
            await ctx.send(msg)
    #說
    @commands.command(name= 'sayd', aliases=['說' , '機器人說'])
    async def sayd(self,ctx,*value):
      if value == ():
        await ctx.send("sayd [msg]")
      else:
        msg = ' '.join(value)
        await ctx.message.delete()
        await ctx.send(msg)
        
    @commands.command()
    async def emmsg(self,ctx,msgid,em):
        msg = await ctx.message.channel.fetch_message(int(msgid))
        print(msg.content)
        await ctx.message.delete()
        if len(em)<18:
            await msg.add_reaction(em)
        else:
            emoji = self.bot.get_emoji(int(((em.split('>'))[0])[-18:]))
            await msg.add_reaction(emoji)
        
    #近戰有塞急進猛突12x下的暴擊機率計算器
    @commands.command(name='ccc', aliases=['急進猛突' , '急進' , '極盡'])
    async def ccc(self,ctx,*,num):
      try:
        i1, i2, i3 = num.split(' ')
        if int(i2) <= 13:
          sum= float(i1) * ( 100 + 60 * ( float(i2) - 1 ) + float(i3) )  / 100
          #總暴率=基礎暴率× (1 + 急進猛突的加成 × (連擊倍率-1)+其他暴擊加成)
          await ctx.send('近戰總爆擊機率：' + str(sum) + '%')
        else:
          await ctx.send('連擊最高只有到 13x 啦')
      except:
        await ctx.send(jdata['command_prefix']+'ccc [基礎近戰暴率 連擊數 額外暴率加成]')
    #----------------------------------
    #近戰有塞創口潰爛12x下的觸發機率計算器    
    @commands.command(name= 'wws', aliases=['創口潰爛' , '創口'])
    async def wws(self,ctx,*,num):
      try:
        i1, i2, i3 = num.split(' ')
        if int(i2) <= 13:
          sum= float(i1) * ( 100 + 40 * ( float(i2) - 1 ) + float(i3) )  / 100
          #總觸發=基礎觸發× (1 + 觸發加成 × (連擊倍率-1)+其他觸發加成)
          await ctx.send('近戰總觸發機率：' + str(sum) + '%')
        else:
          await ctx.send('連擊最高只有到13x啦')
      except:
        await ctx.send(jdata['command_prefix']+'wws [基礎近戰觸發 連擊數 額外觸發加成]')


    @commands.command(name= 'sendch', aliases=['發送至頻道'])
    async def sendch(self,ctx,chid,*,msg):
        ch = self.bot.get_channel(int(chid))
        await ch.send(msg)
    
    @commands.command(name= 'send', aliases=['私訊'])
    async def send(self,ctx,userid,*,msg):
        if '!' in userid:
            user = str(userid).split('!')
        else:
            user = str(userid).split('@')
        if str.isdigit(user[0]):
            user2 = self.bot.get_user(int(userid))
            await user2.send(msg)
        else:
            user1 = str(user[1]).split('>')
            user2 = self.bot.get_user(int(user1[0]))
            await user2.send(msg)
    #環形裝置
    @commands.command()
    async def 環形裝置(self,ctx):
      await ctx.send(f'```維加環形裝置→太空站          & 微蟎蛛型機\n告達環形裝置→昇華實驗室      & 賽托蛛型機(瓦內蜘蛛)\n索拉環形裝置→潤盈寺          & 凱塔蛛型機\n聖油環形裝置→利潤收割者圓蛛\n天藍環形裝置→剝削者圓蛛```')
    #香蕉君
    @commands.command(name= 'Milos', aliases=['香蕉君' , '象徵自由的男人'])
    async def Milos(self,ctx):
      #await ctx.channel.purge(limit=1)
      await ctx.send(self.bot.get_emoji(int(710157217948631085)))
    #突擊
    @commands.command(name='Sortie',aliases=['突擊' , '突襲'])
    async def sortie(self,ctx):
      try:
        cc = opencc.OpenCC('s2t')
        count = 1
        html_sortie = requests.get('https://api.warframestat.us/pc/zh/sortie',headers={'Accept-Language':'tc'})
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

    @commands.command(name='worldstate',aliases=['開放世界時間' , '平原時間' , 'WF時間' , 'openworldstate'])
    async def WFworldtime(self,ctx):
      try:
        if (data_eidolon["state"]=="day"):
          await ctx.send("距離[夜靈平原]晚上還有：" + data_eidolon["timeLeft"])
        elif (data_eidolon["state"]=="night"):
          await ctx.send("距離[夜靈平原]早上還有：" + data_eidolon["timeLeft"])
        if (data_earth["state"]=="day"):
          await ctx.send("距離[地球Earth]晚上還有：" + data_earth["timeLeft"])
        elif (data_earth["state"]=="night"):
          await ctx.send("距離[地球Earth]早上還有：" + data_earth["timeLeft"])
        if (data_vallis["state"]=="warm"):
          await ctx.send("距離[奧布山谷]寒冷還有：" + data_vallis["timeLeft"])
        elif (data_vallis["state"]=="cold"):
          await ctx.send("距離[奧布山谷]溫暖還有：" + data_vallis["timeLeft"])
        if (data_cambion["active"]=="fass"):
          await ctx.send("距離[魔裔禁地]Vome還有：" + data_eidolon["timeLeft"])
        elif (data_cambion["active"]=="vome"):
          await ctx.send("距離[魔裔禁地]Fass還有：" + data_eidolon["timeLeft"])
      except:
        await ctx.send("該功能目前無法使用")
   
    @commands.command(name='ms', aliases=['踩地雷'])
    async def minesweeper(self, ctx, width: int = 10, height: int = 10, difficulty: int = 30):
      grid = tuple([['' for i in range(width)] for j in range(height)])
      num = ('0⃣','1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣')
      msg = ''

      if not (1 <= difficulty <= 100):
        await ctx.send("Please enter difficulty in terms of percentage (1-100).")
        return
      if width <= 0 or height <= 0:
        await ctx.send("Invalid width or height value.")
        return
      if width * height > 198:
        return await ctx.channel.send("Your grid size is too big.")
        return
      if width * height <= 4:
        await ctx.send("Your grid size is too small.")
        return
      
      # set bombs in random location
      for y in range(0, height):
        for x in range(0, width):
          if randint(0, 100) <= difficulty:
            grid[y][x] = '💣'

      # now set the number emojis
      for y in range(0, height):
        for x in range(0, width):
          if grid[y][x] != '💣':
            grid[y][x] = num[sum((
              grid[y-1][x-1]=='💣' if y-1>=0 and x-1>=0 else False,
              grid[y-1][x]=='💣' if y-1>=0 else False,
              grid[y-1][x+1]=='💣' if y-1>=0 and x+1<width else False,
              grid[y][x-1]=='💣' if x-1>=0 else False,
              grid[y][x+1]=='💣' if x+1<width else False,
              grid[y+1][x-1]=='💣' if y+1<height and x-1>=0 else False,
              grid[y+1][x]=='💣' if y+1<height else False,
              grid[y+1][x+1]=='💣' if y+1<height and x+1<width else False
            ))]
      await ctx.send(grid[y][x])

      # generate message
      for i in grid:
        for tile in i:
          msg += '||' + tile + '|| '
        msg += '\n'
      await ctx.send(msg)

  
    
def setup(bot):
    bot.add_cog(Common(bot))