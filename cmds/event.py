from discord.ext import commands
from core.classes import Cog_Extension
from datetime import datetime,timedelta
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class event(Cog_Extension):
  @commands.Cog.listener()
  async def on_message(self,msg):
    f = '[%Y-%m-%d %H:%M:%S]'
    time_delta = timedelta(hours=+8)
    utc_8_date_str = (datetime.utcnow()+time_delta).strftime(f)
    if self.bot.user in msg.mentions:
        await msg.add_reaction(self.bot.get_emoji(int( 請提入你想讓它顯示的表情符號ID [當機器人被標的時候] )))
    if str(msg.channel.type) == 'private' and msg.author != self.bot.user:
        print(utc_8_date_str + str(msg.author) + '說:' + msg.content)
        own = self.bot.get_user(int(jdata['owner']))
        fp = open('./log/' + 'Private.log', 'a',encoding='utf8')
        fp.write(utc_8_date_str + str(msg.author) + '說：' + msg.content+'\n')
        fp.close()
    else:
        if str(msg.channel.type) == 'text' and msg.author != self.bot.user:
            print(utc_8_date_str + str(msg.author) + '說:' + msg.content)
            a = str(msg.guild)
            b = str(msg.channel)
            fp = open('./log/' + a + '-' + b + '.log', 'a',encoding='utf8')
            fp.write(utc_8_date_str + str(msg.author) + '說:' + msg.content+'\n')
            fp.close()
    pass


def setup(bot):
    bot.add_cog(event(bot))