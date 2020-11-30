from discord.ext import commands
from core.classes import Cog_Extension
import os
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class admin(Cog_Extension):
    #清除訊息
    @commands.command(name='clear', aliases=['clean' , '清除'])
    async def clear(self,ctx,*value):
      if value == ():
        await ctx.send(jdata["command_prefix"] + "clear [num] 要刪除的量(行)")
      else:
        num = ' '.join(value)
        if ctx.message.author.id == ctx.guild.owner_id:
            await ctx.channel.purge(limit=int(num)+1)
            print(str(ctx.message.author)+' ---ID '+str(ctx.message.author.id)+'在 << '+str(ctx.channel.name)+' >> 頻道使用了clear指令刪除了'+str(num)+'個對話')
            if int(num)>=10:
              await ctx.send('https://tenor.com/view/explode-blast-blow-nuclear-boom-gif-15025770')
        else:
            await ctx.send('權限不足 本指令只提供給伺服器傭有者 \n本伺服器擁有者為 <@' + str(ctx.guild.owner_id) + '>')

    
    @commands.command(name='cmd', aliases=['終端機'])
    async def cmd(self,ctx,*,cmd):
        await ctx.message.delete()
        '''
        print(type(ctx.author.id))
        print(type(jdata['owner']))
        '''
        if ctx.author.id == jdata['owner']:
            os.system(cmd)


def setup(bot):
    bot.add_cog(admin(bot))