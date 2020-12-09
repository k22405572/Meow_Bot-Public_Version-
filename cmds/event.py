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
        if ',setuserid' in msg.content:
            return
        if str(msg.channel.type) == 'private' and msg.author != self.bot.user and msg.author.id != jdata['owner']:
            own = self.bot.get_user(jdata['owner'])
            print(THC + str(msg.author) + '說:' + msg.content)
            if msg.author.id == onMessageUser:
                await own.send(str(msg.content))
                fp = open('./log/' + 'Private.log', 'a',encoding='utf8')
                fp.write(utc_8_date_str + str(msg.author) + '說：' + msg.content+'\n')
                fp.close()
            else:
                await own.send(THC + '［ID：'+str(msg.author.id)+'］' + str(msg.author) + '說：\n' + str(msg.content))
                chonMessageUser(msg.author.id)
                fp = open('./log/' + 'Private.log', 'a',encoding='utf8')
                fp.write(utc_8_date_str + str(msg.author) + '說：' + msg.content+'\n')
                fp.close()
        else:
            if str(msg.channel.type) == 'text' and msg.author != self.bot.user:
                print(THC + str(msg.author) + '說:' + msg.content)
                a = str(msg.guild)
                b = str(msg.channel)
                fp = open('./log/' + a + '-' + b + '.log', 'a',encoding='utf8')
                fp.write(utc_8_date_str + str(msg.author) + '說:' + msg.content+'\n')
                fp.close()

        if str(msg.channel.type) == 'private' and msg.author != self.bot.user and msg.author.id == jdata['owner']:
          try:
            print(THC + str(msg.author) + '說:' + msg.content)
            user = self.bot.get_user(int(onMessageUser))
            await user.send(msg.content)
            fp = open('./log/' + 'Private.log', 'a',encoding='utf8')
            fp.write(utc_8_date_str + str(msg.author) + '說：' + msg.content+'\n')
            fp.close()
          except:
            pass
        pass


def time_converter(str_time):
    hours, minutes = map(int, str_time.split(':'))
    am_or_pm = ['早上', '下午'][hours >= 12]
    return f'{am_or_pm} {(hours-1) % 12+1}:{minutes:02}'

def setup(bot):
    bot.add_cog(event(bot))