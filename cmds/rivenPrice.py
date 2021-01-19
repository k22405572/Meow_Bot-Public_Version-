import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import requests
import json

with open('dict/Weapons.json', 'r', encoding='utf8') as weapons:
  weapons = json.load(weapons)

with open('dict/attributes.json', 'r', encoding='utf8') as attrDict:
  attrDict = json.load(attrDict)

kuva_only = ["kuva_bramma", "kuva_chakkhurr","kuva_ayanga","kuva_shildeg"]
prime_only = ["euphona_prime","reaper_prime","dakra_prime"]

def replace(name):
  weapon = name
  weapon = weapon.replace(" ","_")   
  weapon = weapon.replace("_wraith","")
  weapon = weapon.replace("_vandal","")
  weapon = weapon.replace("prisma_","")
  weapon = weapon.replace("mara_","")
  weapon = weapon.replace("mk1-","")
  weapon = weapon.replace("telos_","")
  weapon = weapon.replace("synoid_","")
  weapon = weapon.replace("secura_","")
  weapon = weapon.replace("rakta_","")
  weapon = weapon.replace("sancti_","")
  weapon = weapon.replace("vaykor_","")
  if weapon != "dex_dakra":
    weapon = weapon.replace("dex_","")
  if weapon not in prime_only:
    weapon = weapon.replace("_prime","")
  if weapon not in kuva_only:
    weapon = weapon.replace("kuva_","")
  return(weapon)

class rivenPrice(Cog_Extension):
  @commands.command(name='riven',aliases=['紫卡','紫卡查詢'])
  async def rivenPrice(self,ctx,*args):
    msg = self.riven(' '.join(args))
    await ctx.send(msg)

  def riven(self,name):
    if name == "奶子":
      return("你到底是有多喜歡奶子啊")
    Chinese= name
    weapon = weapons.get(name, "Empty")
    if weapon == "Empty":
      weapon = name
    weapon = weapon.lower()
    weapon = replace(weapon)
   
    
    url = 'https://api.warframe.market/v1/auctions/search?type=riven&weapon_url_name=' + weapon + '&sort_by=price_asc'
    html = requests.get(url)
    weapon = weapon.replace("_"," ")
    if html.status_code != 200:
      return('查到...Ordis發生錯誤...API出錯！')
    else:
      rivenData = json.loads(html.text)
      rivenData = rivenData['payload']
      rivenData = rivenData['auctions']
      count = 0
      message = f'以下為{Chinese}紫卡的查詢結果（按價格由低至高順序）\n'
      for items in rivenData:
        if count < 3:
          owner = items['owner']
          if owner['status'] != 'offline':
            rivenItem = items['item']
            rivenName = rivenItem['name']
            message += f'```\n紫卡名稱:{Chinese} {rivenName}\n'
            ownerName = owner['ingame_name']
            message += f'賣家:{ownerName}\n'
            rank = rivenItem['mod_rank']
            rerolls = rivenItem['re_rolls']
            message += f'等級:{rank}\n'
            message += f'迴圈次數:{rerolls}\n'
            for attr in rivenItem['attributes']:
              attribute = attr['url_name']
              attribute = attrDict.get(attribute,attribute)
              value = attr['value']
              if attr['positive'] == True:
                message += f'正面詞條:{attribute} {value}\n'
              elif attr['positive'] == False:
                message += f'負面詞條:{attribute} {value}\n'
            if items['top_bid'] == 'None':
              top_bid = items['top_bid']
              message += f'目前競標:{top_bid}\n'
            else:
              starting_price = items['starting_price']
              buyout_price = items['buyout_price']
              if starting_price == buyout_price:
                message += f'價格:{buyout_price}\n'
              else:
                message += f'起標價格:{starting_price}\n'
                message += f'買斷價格:{buyout_price}\n'
            count += 1
            message += '```'
      return(message)

      
def setup(bot):
    bot.add_cog(rivenPrice(bot))