from discord.ext import commands
from core.classes import Cog_Extension
import os
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class admin(Cog_Extension):
    #清除訊息
    @commands.command(name='clear', aliases=['clean' , '清除'])
    async def clear(self,ctx,num:int=0):
      if num == 0:
        await ctx.send(jdata["command_prefix"] + "clear [num] 要刪除的量(行)")
      else:
        try:
          if ctx.message.author.id == ctx.guild.owner_id:
              await ctx.channel.purge(limit=int(num)+1)
              print(str(ctx.message.author)+' ---ID '+str(ctx.message.author.id)+'在 << '+str(ctx.channel.name)+' >> 頻道使用了clear指令刪除了'+str(num)+'個對話')
              if int(num)>=10:
                await ctx.send('https://tenor.com/view/explode-blast-blow-nuclear-boom-gif-15025770')
          else:
              await ctx.send('權限不足 本指令只提供給伺服器傭有者 \n本伺服器擁有者為 <@' + str(ctx.guild.owner_id) + '>')
        except:
          await ctx.send('請勿在私人頻道使用此功能')
          print('請勿在私人頻道使用這功能')
    
    @commands.command(name= 'avatar', aliases=['頭貼' , '頭像'])
    async def avatar(self,ctx,userid:str='0'):
        if ctx.message.author.id == jdata['owner']:
            uid2 = userid.split('>')
            uid = int((uid2[0])[-18:])
            user = self.bot.get_user(int(uid))
            if user == None:
                await ctx.send('找不到指定用戶')
            else:
                asset = user.avatar_url
                await ctx.send(str(asset))
        else:
          await ctx.send('權限不足')

    @commands.command(name= 'sendch', aliases=['發送至頻道'])
    async def sendch(self,ctx,chid,*,msg):
        if ctx.author.id == jdata['owner']:
            ch = self.bot.get_channel(int(chid))
            await ch.send(msg)
        else:
            await ctx.send(f'權限不足 本指令只提供給機器人擁有者 \n擁有者為 <@{jdata["owner"]}>')
            
    
    @commands.command(name= 'send', aliases=['私訊'])
    async def send(self,ctx,userid,*,msg):
        if ctx.author.id == jdata['owner']:
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
        else:
            await ctx.send(f'權限不足 本指令只提供給機器人擁有者 \n擁有者為 <@{jdata["owner"]}>')
    

def setup(bot):
    bot.add_cog(admin(bot))