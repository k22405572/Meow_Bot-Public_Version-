from discord.ext import commands
from core.classes import Cog_Extension
from datetime import datetime,timedelta
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

onMessageUser = int()
def chonMessageUser(a):
    global onMessageUser
    onMessageUser = a

class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        f = '[%Y-%m-%d %H:%M:%S]'
        time_delta = timedelta(hours=+8)
        utc_8_date_str = (datetime.utcnow()+time_delta).strftime(f)
        THC = '[' + (datetime.utcnow()+time_delta).strftime('%Y-%m-%d ') + time_converter((datetime.utcnow()+time_delta).strftime('%H:%M')) + ']'
        for attachment in msg.attachments:
            att_url = attachment.url
            att_size = attachment.size
        if self.bot.user in msg.mentions:
            await msg.add_reaction(self.bot.get_emoji(int(710157217948631085)))
        if '-setuserid' in msg.content:
            return
        #不是OWNER本人發送私人訊息的紀錄
        if str(msg.channel.type) == 'private' and msg.author != self.bot.user and msg.author.id != jdata['owner']:
            own = self.bot.get_user(jdata['owner'])
            try:
              print(THC + str(msg.author) + '說：' + msg.content + att_url)
            except:
              print(THC + str(msg.author) + '說：' + msg.content)
              print(THC + str(msg.author) + '說：' + msg.content)
            if msg.author.id == onMessageUser:
                try:
                  if att_url.endswith(".jpg") or att_url.endswith(".jpeg") or att_url.endswith(".png") or att_url.endswith(".gif"):
                    await own.send(str(msg.content) + att_url)
                  else:
                    if att_size <= 1048576:
                      await own.send(str(msg.content) + att_url + '\n檔案大小：%.2f KB' % int(att_size/1024))
                    else:
                      await own.send(str(msg.content) + att_url + '\n檔案大小：%.2f MB' % int(att_size/1024/1024))
                except:
                    await own.send(str(msg.content))
                fp = open('./log/' + 'Private.log', 'a',encoding='utf8')
                try:
                  fp.write(utc_8_date_str + str(msg.author) + '說:' + msg.content + att_url +'\n')
                except:
                  fp.write(utc_8_date_str + str(msg.author) + '說:' + msg.content + '\n')
                fp.close()
            else:
                try:
                  if att_url.endswith(".jpg") or att_url.endswith(".jpeg") or att_url.endswith(".png") or att_url.endswith(".gif"):
                    await own.send(THC + '［ID：'+str(msg.author.id)+'］' + str(msg.author) + '說：\n' + str(msg.content) + att_url)
                  else:
                    if att_size <= 1048576:
                      await own.send(THC + '［ID：'+str(msg.author.id)+'］' + str(msg.author) + '說：\n' + str(msg.content) + att_url + '\n檔案大小：%.2f KB' % int(att_size/1024))
                    else:
                      await own.send(THC + '［ID：'+str(msg.author.id)+'］' + str(msg.author) + '說：\n' + str(msg.content) + att_url + '\n檔案大小：%.2f MB' % int(att_size/1024/1024))
                    
                except:
                  await own.send(THC + '［ID：'+str(msg.author.id)+'］' + str(msg.author) + '說：\n' + str(msg.content))
                chonMessageUser(msg.author.id)
                fp = open('./log/' + 'Private.log', 'a',encoding='utf8')
                try:
                  fp.write(utc_8_date_str + str(msg.author) + '說:' + msg.content + att_url + '\n')
                except:
                  fp.write(utc_8_date_str + str(msg.author) + '說:' + msg.content +'\n')
                fp.close()
        #DISCORD群內發訊息紀錄
        else:
            if str(msg.channel.type) == 'text' and msg.author != self.bot.user:
                try:
                  print(THC + str(msg.author) + '說：' + msg.content  + att_url)
                except:
                  print(THC + str(msg.author) + '說：' + msg.content)
                a = str(msg.guild)
                b = str(msg.channel)
                fp = open('./log/' + a + '-' + b + '.log', 'a',encoding='utf8')
                try:
                  fp.write(utc_8_date_str + str(msg.author) + '說:' + msg.content + att_url + '\n')
                except:
                  fp.write(utc_8_date_str + str(msg.author) + '說:' + msg.content + '\n')
                fp.close()
        #不是OWNER本人發送私人訊息的紀錄
        if str(msg.channel.type) == 'private' and msg.author != self.bot.user and msg.author.id == jdata['owner']:
            try:
              print(THC + str(msg.author) + '說：' + msg.content + att_url)
            except:
              print(THC + str(msg.author) + '說：' + msg.content)
            user = self.bot.get_user(int(onMessageUser))
            try:
              if att_url.endswith(".jpg") or att_url.endswith(".jpeg") or att_url.endswith(".png") or att_url.endswith(".gif"):
                    await user.send(msg.content + att_url)
              else:
                    if att_size <= 1048576:
                      await user.send(msg.content + att_url + '\n檔案大小：%.2f KB' % int(att_size/1024))
                    else:
                      await user.send(msg.content + att_url + '\n檔案大小：%.2f MB' % int(att_size/1024/1024))
            except:
              try:
                await user.send(msg.content)
              except:
                pass
            fp = open('./log/' + 'Private.log', 'a',encoding='utf8')
            try:
              fp.write(utc_8_date_str + str(msg.author) + '說:' + msg.content + att_url + '\n')
            except:
              fp.write(utc_8_date_str + str(msg.author) + '說:' + msg.content + '\n')
            fp.close()
        pass
    #設定要跟誰做聊天對象
    @commands.command()
    async def setuserid(self,ctx,userid:int=0):
        if ctx.author.id == int(jdata['owner']):
            if userid != 0 and len(str(userid)) == 18:
                await ctx.send('指定：<@' + str(userid) + '> 為聊天對象')
                user = self.bot.get_user(userid)
                if user != None:
                    chonMessageUser(int(userid))
            else:
              chonMessageUser(int(userid))
              await ctx.send("已重置")



def time_converter(str_time):
    hours, minutes = map(int, str_time.split(':'))
    am_or_pm = ['早上', '下午'][hours >= 12]
    return f'{am_or_pm} {(hours-1) % 12+1}:{minutes:02}'

def setup(bot):
    bot.add_cog(event(bot))