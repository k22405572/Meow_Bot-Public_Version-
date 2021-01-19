from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class help(Cog_Extension):
    #help指令
    @commands.command(name='help', aliases=['說明' , '機器人使用說明' , '幫助'])
    async def help(self,ctx):
        await ctx.send('普通功能：\n```css\n'
        +str(jdata['command_prefix'])+'ping 顯示機器人的延遲\n'
        +str(jdata['command_prefix'])+'sayd [msg] 使機器人說話\n'
        +str(jdata['command_prefix'])+'calc [數學算式]簡易的四則運算(支援: + - * / ( ) 小數 科學記號e=10^)中間不能有空格 不支援指數運算 \n'
        +str(jdata['command_prefix'])+'alias 顯示各個指令的別名\n'
        +str(jdata['command_prefix'])+'user 顯示個人訊息\n'
        +'```'
        #--------------------WARFRAME-----------------------------
        +'WARFRAME：\n```css\n'
        +str(jdata['command_prefix'])+'ccc <基礎近戰暴率> <連擊數> <額外暴率加成> 計算近戰塞急進猛突暴率\n'
        +str(jdata['command_prefix'])+'wws <基礎近戰觸發> <連擊數> <額外觸發加成> 計算近戰塞創口潰爛觸發\n'
        +str(jdata['command_prefix'])+'toroid 查詢環形裝置在哪裡掉落\n'
        +str(jdata['command_prefix'])+'baro 查詢虛空商人剩餘時間或商品\n'
        +str(jdata['command_prefix'])+'riven 查詢Warframe.Market上的紫卡價格\n'
        +str(jdata['command_prefix'])+'wfm 查詢Warframe.Market上的物品價格\n'
        +str(jdata['command_prefix'])+'wiki [您要查詢的東西名稱]查詢wiki上的資訊\n'
        +'------------開放世界時間----------------\n'
        +str(jdata['command_prefix'])+'POE 夜靈平原時間\n'
        +str(jdata['command_prefix'])+'Cambion 魔裔禁地時間\n'
        +str(jdata['command_prefix'])+'Orb 奧布山谷時間\n'
        +str(jdata['command_prefix'])+'Earth 地球時間\n'
        +'------------查詢任務相關----------------\n'
        +str(jdata['command_prefix'])+'sortie 突擊信息\n'
        +str(jdata['command_prefix'])+'arbitration 仲裁信息\n'
        +str(jdata['command_prefix'])+'fissure 遺物裂縫信息\n'
        +str(jdata['command_prefix'])+'nightwave 午夜電波信息\n'
        +'---------------------------------------'
        +'```'
        +'僅限管理員的功能：\n```css\n'
        +str(jdata['command_prefix'])+'clear [num] 刪除指定數量的聊天內容\n'
        +str(jdata['command_prefix'])+'avatar [用戶ID] 顯示目標用戶頭貼\n'
        +str(jdata['command_prefix'])+'send [用戶ID] 私訊目標用戶(可私訊機器人使用)\n'
        +str(jdata['command_prefix'])+'sendch [頻道ID] 用機器人在頻道內說話(可私訊機器人使用)\n'
        +'```')

    @commands.command(name='alias', aliases=['別名'])
    async def alias(self,ctx):
        await ctx.send('普通功能：\n```css\n'
        +str(jdata['command_prefix'])+'ping [延遲 , 機器人延遲 , delay]\n'
        +str(jdata['command_prefix'])+'sayd [說 , 機器人說]\n'
        +str(jdata['command_prefix'])+'calc [計算機 , 計算]\n'
        +str(jdata['command_prefix'])+'alias [別名]\n'
        +str(jdata['command_prefix'])+'user [使用者資訊 , 用戶資訊]\n'
        +'```'
        #--------------------WARFRAME-----------------------------
        +'WARFRAME：\n```css\n'
        +str(jdata['command_prefix'])+'ccc [急進猛突 , 急進 , 極盡]\n'
        +str(jdata['command_prefix'])+'wws [創口潰爛 , 創口]\n'
        +str(jdata['command_prefix'])+'toroid [環形裝置] \n'
        +str(jdata['command_prefix'])+'baro =[奸商 , Baro]\n'
        +str(jdata['command_prefix'])+'riven [紫卡,紫卡查詢]\n'
        +str(jdata['command_prefix'])+'wfm [wm, 市場查詢]\n'
        +str(jdata['command_prefix'])+'wiki [wf維基]\n'
        +'------------開放世界時間----------------\n'
        +str(jdata['command_prefix'])+'POE [夜靈平原時間 , 希圖斯時間 , 希圖斯]\n'
        +str(jdata['command_prefix'])+'Cambion [魔裔禁地時間 , 火衛二 , 火衛二時間]\n'
        +str(jdata['command_prefix'])+'Orb [奧布山谷時間 , 奧布山谷 , 福爾圖娜 , 福爾圖娜時間]\n'
        +str(jdata['command_prefix'])+'Earth [地球時間 , 地球]\n'
        +'------------查詢任務相關----------------\n'
        +str(jdata['command_prefix'])+'sortie [突擊 , 突襲]\n'
        +str(jdata['command_prefix'])+'arbitration [仲裁]\n'
        +str(jdata['command_prefix'])+'fissure [虛空裂縫 , 裂縫 , 遺物]\n'
        +str(jdata['command_prefix'])+'nightwave [午夜電波 , 電波]\n'
        +'---------------------------------------'
        +'```'
        +'僅限管理員的功能：\n```css\n'
        +str(jdata['command_prefix'])+'clear [clean , 清除]\n'
        +str(jdata['command_prefix'])+'avatar [頭貼 , 頭像]\n'
        +str(jdata['command_prefix'])+'send [私訊]\n'
        +str(jdata['command_prefix'])+'sendch [發送至頻道]\n'
        +'```')
     
  
def setup(bot):
    bot.add_cog(help(bot))