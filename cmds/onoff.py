from discord.ext import commands
from core.classes import Cog_Extension

class onoff(Cog_Extension):
    @commands.command(name='member', aliases=['顯示成員' , '成員'])
    async def member(self,ctx):
        memberlist = ctx.guild.members
        onlinelist = []
        onlineidlist = []
        offlineidlist = []
        offlinelist = []
        msg = "========online========\n```css\n"
        for i in memberlist:
            if str(i.status) == "online":
                onlineidlist.append(i)
                onlinelist.append(i)
            else:
                offlinelist.append(i)
                offlineidlist.append(i)
        for onid in onlineidlist:
            msg =  msg + '-' + str(onid) + '\n'
        msg = msg + '```========offline========\n```css\n'
        for offid in offlineidlist:
            msg =  msg + '-' + str(offid) + '\n'
        msg = msg + '```'

        await ctx.send(msg)
        print('\n========online========\n')
        for i2 in onlinelist:
            print(i2)
        print('\n========offline========\n')
        for i3 in offlinelist:
            print(i3)
    @commands.command(name='online', aliases=['顯示上線成員' , '上線' , '在線'])
    async def online(self,ctx):
        memberlist = ctx.guild.members
        onlineidlist = []
        for i in memberlist:
            if str(i.status) == "online":
                onlineidlist.append(i)
        msg = '在線名單:\n```css\n'
        for i2 in onlineidlist:
            msg = msg + '-' + str(i2) + '\n'
        msg = msg + '```'
        await ctx.send(msg)
    @commands.command(name='offline', aliases=['顯示下線成員', '下線', '顯示離線成員', '離線'])
    async def offline(self,ctx):
        memberlist = ctx.guild.members
        offlineidlist = []
        for i in memberlist:
            if str(i.status) == "offline":
                offlineidlist.append(i)
        msg = '離線名單:\n```css\n'
        for i2 in offlineidlist:
            msg = msg + '-' + str(i2) + '\n'
        msg = msg + '```'
        await ctx.send(msg)
        

def setup(bot):
    bot.add_cog(onoff(bot))