import discord
from discord.ext import commands
import os
import json
#import keep_alive
from datetime import datetime,timedelta
import asyncio
import requests

#os.system('pip install --upgrade pip')
#os.system('pip install opencc-python-reimplemented')
#os.system('pip install --upgrade discord.py')

keeptime = 10
keepstatus = 1

intents = discord.Intents.all()

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='-',intents = intents)

@bot.event
async def on_ready():
    bot.unload_extension(F'cmds.test')
    print(">> 目前版本：v2.2.8 <<")
    print(">> Meow_Bot is online <<")
    #while(1):
    #  requests.get("https://friendbot.meowxiaoxiang.repl.co")
    #  await asyncio.sleep(60)
    while(1):
        await asyncio.sleep(keeptime)
        #print(str(keepstatus))
        if keepstatus == 1:
            requests.get("http://127.0.0.1:8080/")

#----------------------------------------------------------------------------
bot.remove_command('help')
#help指令
@bot.group(name='help', aliases=['說明' , '機器人使用說明' , '幫助'])
async def help(ctx):
    await ctx.send('普通功能：\n```css\n'
    +str(jdata['command_prefix'])+'ping 顯示機器人的延遲\n'
    +str(jdata['command_prefix'])+'ccc [基礎近戰暴率 連擊數 額外暴率加成] 計算近戰塞急進猛突暴率\n'
    +str(jdata['command_prefix'])+'wws [基礎近戰觸發 連擊數 額外觸發加成] 計算近戰塞創口潰爛觸發\n'
    +str(jdata['command_prefix'])+'sayd [msg] 使機器人說話\n'
    +str(jdata['command_prefix'])+'member 顯示伺服器中所有人的狀態\n'
    +str(jdata['command_prefix'])+'online 顯示上線名單\n'
    +str(jdata['command_prefix'])+'offline 顯示離線名單\n'
    +str(jdata['command_prefix'])+'picture 隨機發送一張圖片\n'
    +str(jdata['command_prefix'])+'ms 踩地雷\n'
    +str(jdata['command_prefix'])+'sortie 突擊信息\n'
    +str(jdata['command_prefix'])+'POE 夜靈平原時間\n'
    +str(jdata['command_prefix'])+'Cambion 魔裔禁地時間\n'
    +str(jdata['command_prefix'])+'Orb 奧布山谷時間\n'
    +str(jdata['command_prefix'])+'Earth 地球時間\n'
    +str(jdata['command_prefix'])+'calc [數學算式]簡易的四則運算(支援: + - * / ( ) 小數 科學記號e=10^)中間不能有空格 不支援指數運算 \n'
    +str(jdata['command_prefix'])+'alias 顯示各個指令的別名\n'
    +str(jdata['command_prefix'])+'user 顯示個人訊息\n```僅限管理員的功能：\n```css\n'
    +str(jdata['command_prefix'])+'clear [num] 刪除指定數量的聊天內容\n'
    +'```')


@bot.command(name='alias', aliases=['別名'])
async def alias(ctx):
  await ctx.send('這些指令的別名：\n```css\n'
    +str(jdata['command_prefix'])+'help：[說明 , 機器人使用說明 , 幫助]\n'
    +str(jdata['command_prefix'])+'ping：[延遲 , 機器人延遲 , delay]\n'
    +str(jdata['command_prefix'])+'ccc：[急進猛突 , 急進 , 極盡]\n'
    +str(jdata['command_prefix'])+'wws：[創口潰爛 , 創口]\n'
    +str(jdata['command_prefix'])+'sayd：[說 , 機器人說]\n'
    +str(jdata['command_prefix'])+'member [顯示成員 , 成員]\n'
    +str(jdata['command_prefix'])+'online [顯示上線成員 , 上線 , 在線]\n'
    +str(jdata['command_prefix'])+'offline [顯示下線成員 , 下線 , 顯示離線成員 , 離線]\n'
    +str(jdata['command_prefix'])+'picture：[pic , 圖片]\n'
    +str(jdata['command_prefix'])+'ms：[踩地雷]\n'
    +str(jdata['command_prefix'])+'sortie：[突擊 , 突襲]\n'
    +str(jdata['command_prefix'])+'POE：[夜靈平原時間 , 希圖斯時間 , 希圖斯]\n'
    +str(jdata['command_prefix'])+'Cambion：[魔裔禁地時間 , 火衛二 , 火衛二時間]\n'
    +str(jdata['command_prefix'])+'Orb：[奧布山谷時間 , 福爾圖娜 , 福爾圖娜時間]\n'
    +str(jdata['command_prefix'])+'Earth：[地球時間 , 地球]\n'
    +str(jdata['command_prefix'])+'calc：[計算機 , 計算]\n'
    +str(jdata['command_prefix'])+'user：[使用者資訊 , 用戶資訊]\n'
    +str(jdata['command_prefix'])+'clear：[clean , 清除]\n```')
 
#-----------------------------------------------------------------------------
f = '[%Y-%m-%d %H:%M:%S]'
time_delta = timedelta(hours=+8)
utc_8_date_str = (datetime.utcnow()+time_delta).strftime(f)
#-----------------------------------------------------------------------------

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


@bot.command(name= 'load', aliases=['載入' , '載入模組' , '啟用'])
async def load(ctx, *value):
  if ctx.author.id == jdata['owner']:
    if value == ():
      await ctx.send("此處不可為空 請輸入組件名稱")
    else:
      try:
        extension = ' '.join(value)
        bot.load_extension(F'cmds.{extension}')
        await ctx.send(f'\n已加載：{extension}')
        print('\n---------------------------------\n' + utc_8_date_str + f'\n已加載 {extension}\n---------------------------------\n')
      except:
        await ctx.send("錯誤：組件載入失敗")
  else:
      await ctx.send("此功能只能給機器人擁有者使用！")


@bot.command(name= 'unload', aliases=['卸載' , '卸載模組' , '停用'])
async def unload(ctx, *value):
  if ctx.author.id == jdata['owner']:
    if value == ():
      await ctx.send("此處不可為空 請輸入組件名稱")
    else:
      try:
        extension = ' '.join(value)
        bot.unload_extension(F'cmds.{extension}')
        await ctx.send(f'\n已卸載：{extension}')
        print('\n---------------------------------\n' + utc_8_date_str + f'\n已卸載 {extension}\n---------------------------------\n')
      except:
        await ctx.send("錯誤：卸載失敗")
  else:
      await ctx.send("此功能只能給機器人擁有者使用！")


@bot.command(name= 'reload', aliases=['重載' , '重載模組' , '重新載入模組', '重新加載', '重啟'])
async def reload(ctx, *value):
  if ctx.author.id == jdata['owner']:
    if value == ():
      await ctx.send("此處不可為空 請輸入組件名稱")
    else:
      try:
        extension = ' '.join(value)
        bot.reload_extension(F'cmds.{extension}')
        await ctx.send(f'\n已重新載入：{extension}')
        print('\n---------------------------------\n' + utc_8_date_str + f'\n已重新載入 {extension}\n---------------------------------\n')
      except:
        await ctx.send("錯誤：組件重新載入失敗")
  else:
      await ctx.send("此功能只能給機器人擁有者使用！")

@bot.command()
async def keep(ctx,type,index):
    global keepstatus,keeptime
    if type == 'status':
        if index == '1':
            print('已啟用保持連線')
        elif index == '0':
            print('已關閉保持連線')
        else:
            print('請輸入1或0')
            return
        keepstatus = int(index)
    if type == 'time':
        if index.isdigit():
            keeptime = int(index)
        else:
            print('請輸入數字')

#機器人關閉系統--------------------------------------------   

@bot.command(name= 'disconnect', aliases=['disable' , 'shutdown' , '關閉機器人' , '關機' , '關閉'])
async def turn_off_bot(ctx):
  if ctx.message.author.id == jdata['owner']:
    print(utc_8_date_str + '機器人已關閉')
    await ctx.send(utc_8_date_str + '\n機器人已關閉') #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    await bot.close()
  else:
    await ctx.send('權限不足 本指令只提供給Meow_Bot擁有者 \n擁有者為 <@436866339731275787> [小翔]')

@bot.event
async def on_disconnect():
    requests.get("http://127.0.0.1:8080/")
    print('機器人已關閉')
#--------------------------------

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
       
if __name__ == "__main__":
    #keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])

