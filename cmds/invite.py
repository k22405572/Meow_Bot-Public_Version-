import discord
from discord.ext import commands
import asyncio
from core.classes import Cog_Extension

luid = lchid = lstat = lmsgid = lmsg = 0

def new(a,b,c,d,e):
    global luid,lchid,lstat,lmsgid,lmsg
    luid = a
    lchid = b
    lmsgid = c
    lstat = d
    lmsg = e
    if lstat == 1:
        asyncio.run(delmsg())
    else:
        pass
    return luid,lchid,lstat,lmsgid,lmsg

async def delmsg():
    await asyncio.sleep(5)
    await lmsg.delete()
    new(0,0,0,0,0)

class invite(Cog_Extension):
    @commands.command(name='invite', aliases=['邀請'])
    async def invite(self,ctx,uuid):
        await ctx.message.delete()
        if lstat == 0:
            uid2 = uuid.split('>')
            uid = int((uid2[0])[-18:])
            member = ctx.guild.get_member(ctx.author.id)
            user = self.bot.get_user(int(uid))
            if str(type(member.voice.channel)) == str(discord.channel.VoiceChannel):
                if ctx.author in member.voice.channel.members:
                    msg = await ctx.send('<@'+str(user.id) + '>是否願意進入' + str(member.voice.channel.name) +'\n請在5秒內按下')
                    await msg.add_reaction('✅')
                    await msg.add_reaction('❎')
                    new(uid, member.voice.channel.id, msg.id, int('1'),msg)
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,pl):
        if pl.user_id == luid :
            print('userID OK')
            if pl.message_id == lmsgid:
                print('messageID OK')
                if str(pl.emoji) == '✅':
                    print('emoji OK')
                    if lstat == 1:
                        print('stat OK')
                        guild = self.bot.get_guild(pl.guild_id)
                        member = guild.get_member(pl.user_id)
                        channel = self.bot.get_channel(lchid)
                        if str(lmsg) == '1':
                            await lmsg.delete()
                        new(0,0,0,0,0)
                        await member.move_to(channel)
                else:
                    if str(lstat) == '1':
                        await lmsg.delete()
                    new(0,0,0,0,0)

def setup(bot):
    bot.add_cog(invite(bot))
