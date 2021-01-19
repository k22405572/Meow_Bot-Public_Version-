import discord
from discord.ext import commands
import os
import json
import keep_alive
from datetime import datetime,timedelta
import asyncio
import requests

#os.system('pip install --upgrade pip')
#os.system('pip install --upgrade discord.py')

intents = discord.Intents.all()

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='-',intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")
    while(1):
        await asyncio.sleep(10)
        requests.get("http://127.0.0.1:8080/")

#----------------------------------------------------------------------------
bot.remove_command('help') #移除原有的help選單 help選單放在common.py內
#-----------------------------------------------------------------------------
f = '[%Y-%m-%d %H:%M:%S]'
time_delta = timedelta(hours=+8)
utc_8_date_str = (datetime.utcnow()+time_delta).strftime(f) #時間戳記
#-----------------以下為機器人基本模組載入卸載列出下載功能區域建議不要隨意更改------------
#列出所有此機器人的Python模組 cmds 內的
@bot.command(name= 'listmod', aliases=['列出所有模組' , '列出模組'])
async def listmodel(ctx):
  modlist = []
  modindex = 0
  for modname in os.listdir('./cmds'):
      if modname.endswith('.py'):
          modlist.append(modindex)
          modlist.append(modname)
          modindex += 1
  modindex = 0
  msg = ''
  dou = 0
  for i in modlist:
      if dou == 0:
          dou+=1
      else:
          msg = msg + '[' + str(i)[:-3] +']'
          dou = 0
  await ctx.send(f'```ini\n此機器人目前擁有的所有模組：\n{msg}```')
#把模組的原始Python檔案下載
@bot.command(name= 'downloadmod', aliases=['下載模組' , '模組下載' , '下載mod' , 'mod下載'])
async def downloadmod(ctx, *args):
    if ctx.author.id == jdata['owner']:
        mod = ' '.join(args)
        if mod == ():
            await ctx.send(NullMod())
        else:
            try:
                fileurl = 'cmds/' + mod + '.py'
                print(fileurl+'\n')
                await asyncio.sleep(0.5)
                upfile = discord.File(F'{fileurl}')
                await ctx.send(file = upfile)
            except:
                await ctx.send('錯誤：無法下載模組')

@bot.command(name= 'load', aliases=['載入' , '載入模組' , '啟用'])
async def load(ctx, extension:str ='Null'):
  if ctx.author.id == jdata['owner']:
    if extension == 'Null':
      await ctx.send(NullMod())
    else:
      bot.load_extension(F'cmds.{extension}')
      await ctx.send(f'\n已加載：{extension}')
      print('\n---------------------------------\n' + utc_8_date_str + f'\n已加載 {extension}\n---------------------------------\n')
  else:
      await ctx.send(InsufficientPermissions())

@bot.command(name= 'unload', aliases=['卸載' , '卸載模組' , '停用'])
async def unload(ctx, extension:str='Null'):
  if ctx.author.id == jdata['owner']:
    if extension == 'Null':
      await ctx.send(NullMod())
    else:
      try:
        bot.unload_extension(F'cmds.{extension}')
        await ctx.send(f'\n已卸載：{extension}')
        print('\n---------------------------------\n' + utc_8_date_str + f'\n已卸載 {extension}\n---------------------------------\n')
      except:
        await ctx.send("錯誤：組件卸載失敗")
  else:
      await ctx.send(InsufficientPermissions())


@bot.command(name= 'reload', aliases=['重載' , '重載模組' , '重新載入模組', '重新加載', '重啟' , '重新載入'])
async def reload(ctx, extension:str ='Null'):
  if ctx.author.id == jdata['owner']:
    if extension == 'Null':
      await ctx.send(NullMod())
    else:
      bot.reload_extension(F'cmds.{extension}')
      await ctx.send(f'\n已重新載入：{extension}')
      print('\n---------------------------------\n' + utc_8_date_str + f'\n已重新載入 {extension}\n---------------------------------\n')
  else:
      await ctx.send(InsufficientPermissions())



#機器人關閉系統--------------------------------------------   

@bot.command(name= 'disconnect', aliases=['disable' , 'shutdown' , '關閉機器人' , '關機' , '關閉'])
async def turn_off_bot(ctx):
  if ctx.message.author.id == jdata['owner']:
    print(utc_8_date_str + '機器人已關閉')
    await ctx.send(utc_8_date_str + '\n機器人已關閉') #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    await bot.close()
  else:
    await ctx.send(InsufficientPermissions())

@bot.event
async def on_disconnect():
    requests.get("http://127.0.0.1:8080/")
    print('機器人已關閉')
#---------------------------------------------------------

class InsufficientPermissions(Exception):
  def __str__(self):
    return '權限不足 本指令只提供給機器人擁有者 \n擁有者為 <@' + jdata["owner"] + '>'
class NullMod(Exception):
  def __str__(self):
    return '此處不可為空 請輸入組件名稱'
    
#------------把cmd內的所有模組做載入--------------
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
       
if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])
    #bot.run(jdata['TOKEN_CRAB'])
