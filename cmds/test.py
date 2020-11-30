import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import requests
import json


class test(Cog_Extension):
    #清除訊息
    @commands.command(name='test', aliases=['機器人測試', '測試'])
    async def t(self,ctx):
      await ctx.send("test")
      print("test")
    @commands.command(name='memtest')
    async def memtest(self,ctx,uid):
      guild = self.bot.get_guild(552875885070516235)
      member = guild.get_member(int(uid))
      await ctx.send(member)
      print(member)
    @commands.command()
    async def www(self,ctx,msg,em):
     if len(em)<2:
        await msg.add_reaction(em)
     else:
        emoji = self.bot.get_emoji(int(((em.split('>'))[0])[-18:]))
        await msg.add_reaction(emoji)

        
  
def setup(bot):
    bot.add_cog(test(bot))