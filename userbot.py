from telethon import TelegramClient, events, sync, functions, types
from telethon.errors import rpcbaseerrors
import time
import os,sys
##''
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio, aiocron, datetime
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, User

#
import random
import time
import os, sys
import asyncio
import random
import wikipedia 
import requests
from collections import deque
from telethon.tl.types import ChannelParticipantsAdmins
import datetime
import os, sys
import time
#modules
from telethon.tl.functions.channels import JoinChannelRequest

from telethon import TelegramClient
from telethon import TelegramClient
from telethon.sessions import StringSession
import os
api_id = 15321012
api_hash = "833e6869c442004c6e56a0e16d7964fe"
#string = "test"

bot_token = "6413133247:AAHdlkqwh0Y40g6U1Nkq6bt5llaCYp5LpdU"
#modules

@client.on(events.NewMessage(pattern=".help"))
async def renotip(event):
	help = ["""🦊UzBot - юзербот для анимации
🦊программист: @virtual_programmer_n
🦊канал: нет
🕷 Модули 🕸 19
🖊 .type - текст анимации
😿 .sorry - красивые шрифте для sorry
😺 .thanks - красивые шрифте для спасибо
💀 .smile - анимация смайлики
🔫 .pisto - пистолет
🧩 .info - свой информация
🗿 .chats - все своих чати 
🧠 .brain - анимация мозг 
🌅 .pic - рандом картинки
🚔 .police - анимация сирена
🪄 .magic - анимация сердце
🤷‍♂ .what - анимация "что?"
🆗 .ok - большое текст "ок"
🙅‍♂ .no - большое текст "но"
⏩ .revnum - реверс 10-0 номеров
🤚 .hi - большое текст "hello"
❤️ .hearts - анимация сердце 2
🈳 .d - я не знал как его назвать 
🖕 .fuck - анимация fuck"""]
	for d in help:
		await event.edit(d)
		#new animation
@client.on(events.NewMessage(pattern=".police"))
async def renotip(event):
	police = ["""  🔴🔴🔴⬜⬜⬜🔵🔵🔵
 🔴🔴🔴⬜⬜⬜🔵🔵🔵
 🔴🔴🔴⬜⬜⬜🔵🔵🔵""", """ 🔵🔵🔵⬜⬜⬜🔴🔴🔴
🔵🔵🔵⬜⬜⬜🔴🔴🔴
🔵🔵🔵⬜⬜⬜🔴🔴🔴"""]
	time.sleep(0.1)
	for i in range(30):
		time.sleep(0.2)
		for d in police:
			time.sleep(0.2)
			await event.edit(d)
@client.on(events.NewMessage(pattern=".rebotip"))
async def renotip(event):
	renotip=["""Renotip+𝒩ℴ𝓏𝒶𝑒ENOTIP������������"","""🄱🄴🄺🅉🄾🄳+🄽🄾🅉🄰🄽🄸🄽""","""Renotip +🅽🅾️🆉🅰️🅽🅸🅽""","""I LOVE YOU❤️N"""]
	time.sleep(0.1)
	for a in renotip:
		time.sleep(0.7)
		await event.edit(a)						
@client.on(events.NewMessage(pattern=".magic"))
async def renotip(event):
	magic = ["""🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🧡🧡🤍🧡🧡🤍🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🤍🧡🧡🧡🧡🧡🤍🤍
🤍🤍🤍🧡🧡🧡🤍🤍🤍
🤍🤍🤍🤍🧡🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💛💛🤍💛💛🤍🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍🤍💛💛💛💛💛🤍🤍
🤍🤍🤍💛💛💛🤍🤍🤍
🤍🤍🤍🤍💛🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💚💚🤍💚💚🤍🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍🤍💚💚💚💚💚🤍🤍
🤍🤍🤍💚💚💚🤍🤍🤍
🤍🤍🤍🤍💚🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""","""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💙💙🤍💙💙🤍🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍🤍💙💙💙💙💙🤍🤍
🤍🤍🤍💙💙💙🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💜💜🤍💜💜🤍🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍🤍💜💜💜💜💜🤍🤍
🤍🤍🤍💜💜💜🤍🤍🤍
🤍🤍🤍🤍💜🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤎🤎🤍🤎🤎🤍🤍
🤍🤎🤎🤎🤎🤎🤎🤎🤍
🤍🤎🤎🤎🤎🤎🤎🤎🤍
🤍🤎🤎🤎🤎🤎🤎🤎🤍
🤍🤍🤎🤎🤎🤎🤎🤍🤍
🤍🤍🤍🤎🤎🤎🤍🤍🤍
🤍🤍🤍🤍🤎🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🖤🖤🤍🖤🖤🤍🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🤍💖💖💖💖💖🤍🤍
🤍🤍🤍💖💖💖🤍🤍🤍
🤍🤍🤍🤍💖🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💛💛🤍💜🖤🤍🤍
🤍💜💙💚🧡🖤💛💚🤍
🤍❤️💙🤎💚🖤💖❤️🤍
🤍💜🤎🤎💛💜🧡❤️🤍
🤍🤍🤎💜💙💜💜🤍🤍
🤍🤍🤍❤️❤️🧡🤍🤍🤍
🤍🤍🤍🤍🤎🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🧡🤎🤍💛💖🤍🤍
🤍💙🤎💖🧡🧡💛🧡🤍
🤍💚🧡💚💚💜💛💚🤍
🤍❤️❤️❤️💛🤎🤎🤎🤍
🤍🤍🧡💜🧡💜🖤🤍🤍
🤍🤍🤍🧡🤎🖤🤍🤍🤍
🤍🤍🤍🤍💖🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💙🖤🤍🧡💙🤍🤍
🤍🧡❤️🧡💛🖤🖤💖🤍
🤍🤎💙💙💙💜❤️🤎🤍
🤍💜💙💖❤️❤️💜💖🤍
🤍🤍💜💜💛💛💙🤍🤍
🤍🤍🤍🤎🖤🧡🤍🤍🤍
🤍🤍🤍🤍💖🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🧡💖🤍❤️🖤🤍🤍
🤍🤎💛💖🧡💜🖤💖🤍
🤍🖤❤️🧡💛💛🖤🖤🤍
🤍🖤❤️💛💜💛💖🖤🤍
🤍🤍🤎💚💜💛🤎🤍🤍
🤍🤍🤍❤️💛💜🤍🤍🤍
🤍🤍🤍🤍💛🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🧡💛🤍❤️🧡🤍🤍
🤍🖤❤️💚💖🧡💜🖤🤍
🤍🧡❤️💛💛🧡🖤💖🤍
🤍💛💙💛❤️🤎💜❤️🤍
🤍🤍💖🖤❤️💛❤️🤍🤍
🤍🤍🤍💚❤️❤️🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""","""
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🖤💖🤍❤️🖤🤍🤍
🤍🖤💙❤️💛💙💛🧡🤍
🤍❤️💙💛💛💖🤎💙🤍
🤍🖤💜🖤❤️💜💛💛🤍
🤍🤍💛💙💛💖💚🤍🤍
🤍🤍🤍💜🤎💚🤍🤍🤍
🤍🤍🤍🤍💜🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💙🤎🤍💖❤️🤍🤍
🤍💙❤️🤎💙💚🖤💚🤍
🤍🧡🧡🤎💙💜🤎💛🤍
🤍🤎💚🤎🖤💙💛💙🤍
🤍🤍🤎🧡🤎🧡💛🤍🤍
🤍🤍🤍💜💚💚🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""","""❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""","""❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""","""❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️🤍🤍""","""❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️""", """❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️""", """❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️""", """❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️""", """❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️""", """❤️❤️❤️❤️
❤️❤️❤️❤️
❤️❤️❤️❤️
❤️❤️❤️❤️""", """❤️❤️❤️
❤️❤️❤️
❤️❤️❤️""", """❤️❤️❤️
❤️❤️❤️
❤️❤️❤️""", """❤️❤️
❤️❤️""", """❤️❤️
❤️❤️""", """❤️""", """I """, """I ❤️""","""I ❤️ U!"""]
	time.sleep(0.1)
	for d in magic:
		time.sleep(0.2)
		await event.edit(d)
@client.on(events.NewMessage(pattern=".revnum"))
async def renotip(event):
	revnum = ["🔟", "9️⃣", "8️⃣", "7️⃣", "6️⃣", "5️⃣", "4️⃣", "3️⃣", "2️⃣", "1️⃣", "0️⃣", "🆘"]
	time.sleep(0.1)
	for d in revnum:
	       time.sleep(1.2)
	       await event.edit(d)
        
@client.on(events.NewMessage(pattern=".what"))
async def renotip(event):
	what = ["🤔🧐🤨🤔🧐🤨", "🧐🤨🤔🧐🤨🤔"]
	for i in range(30):
		time.sleep(0.1)
		for a in what:
			time.sleep(0.7)
			await event.edit(a)
@client.on(events.NewMessage(pattern=".smile"))
async def renotip(event):
	smile = ["😀", "😊", "😆", "😉", "😙", "🤫", "😁"]
	for i in range(30):
		time.sleep(0.1)
		for a in smile:
			time.sleep(0.7)
			await event.edit(a)
@client.on(events.NewMessage(pattern=".hi"))
async def renotip(event):
	hi = ["""╔┓┏╦━╦┓╔┓╔━━╗
║┗┛║┗╣┃║┃║X X║
║┏┓║┏╣┗╣┗╣╰╯║
╚┛┗╩━╩━╩━╩━━╝"""]
	time.sleep(0.1)
	for a in hi:
			time.sleep(0.7)
			await event.edit(a)
@client.on(events.NewMessage(pattern=".hearts"))
async def renotip(event):
	hearts = ["🤍", "🖤", "🤎", "💛", "🧡", "💙", "❤️"]
	for i in range(30):
		time.sleep(0.1)
		for a in hearts:
			time.sleep(0.7)
			await event.edit(a)
@client.on(events.NewMessage(pattern=".clock"))
async def renotip(event):
	clock = ["🕐🕐🕐", "🕑🕑🕑", "🕒🕒🕒", "🕓🕓🕓", "🕔🕔🕔", "🕧🕧🕧", "🕖🕖🕖", "🕗🕗🕗", "🕘🕘🕘", "🕙🕙🕙", "🕛🕛🕛"]
	time.sleep(0.1)
	for b in clock:
			time.sleep(0.7)
			await event.edit(b)
@client.on(events.NewMessage(pattern=".fuck"))
async def renotip(event):
	fuck = ["👋", "🤞", "🤏", "👎", "🤙", "🖕"]
	for i in range(6):
		time.sleep(0.1)
		for b in fuck:
			time.sleep(0.7)
			await event.edit(b)
@client.on(events.NewMessage(pattern=".ok"))
async def renotip(event):
	ok = ["""┏━┓ ┳┏━ 
┃┈┃ ┣┻┓ 
┗━┛ ┻┈┻ 
"""]
	for d in ok:
		await event.edit(d)
@client.on(events.NewMessage(pattern=".no"))
async def darknetUzb(event):
	no = ["""─█▄──█─█▀▀▀█
─█─█─█─█───█
─█──▀█─█▄▄▄█
"""]
	for d in no:
		await event.edit(d)
	

@client.on(events.NewMessage(pattern=".d"))
async def renotip(event):
	d = ["🏃", "🚶", "🧎", "🦹‍♂️", "🕴️", "🧘‍♂️"]
	time.sleep(0.7)
	for i in range(3):
		time.sleep(0.7)
		for b in d:
			time.sleep(0.7)
			await event.edit(b)
#end new
@client.on(events.NewMessage(pattern=".pisto"))
async def renotip(event):
    renotip = ["""░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄
░███████████████████████ 
░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ 
░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░
░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░
░░█▓▓▓▓▓▌░░░░░░░░░░
░▐█▓▓▓▓▓░░░░░░░░░░░
░▐██████▌░░░░░░░░░░"""]
    for d in renotip:
    	await event.edit(d)
@client.on(events.NewMessage(pattern=".brain"))
async def dark(event):
    brain = ["YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
         "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n   miyyangiz qovoq ekan)"]
    time.sleep(0.7)
    for i in range(3):
    	time.sleep(0.7)
    for a in brain:
    	time.sleep(0.7)
    	await event.edit(a)
    
    	
sorry = ["I'm Sorry （｡≧ _ ≦｡）","≦(._.)≧ : Sorry","o(´д｀o) : I'm Sorry Pleaze Forgive me","Sorry ヾ(_ _*)","(๑•́ㅿ•̀๑ ) ᔆᵒʳʳᵞ","Sorry:(づ-̩̩̩-̩̩̩_-̩̩̩-̩̩̩)づ","༒ᎦᎧᏒᏒⲨ☆ʝααи༒"]
@client.on(events.NewMessage(pattern=".sorry"))
async def sorryy(ult):
  s = random.choice(sorry)
  return await ult.edit(f"{s}")
  
thanks = ["⋆*⁎ ᎢℋᎪɳᏦ ᎩӫᏌ ⁎*⋆","ପ(๑•̀ᴗ•̀)* ॣ৳৸ᵃᵑᵏ Ꮍ৹੫ᵎ *","ᐝ୨୧ Ƭʜᵃℕҡ ყօϋ ୨୧ᐝ","ෆ⃛ෆ⃛ෆ⃛ ♡♡[τ̲̅н̲̅a̲̅и̲̅κ̲̅ ч̲̅o̲̅u̲̅]ᴗ͈ₒᴗ͈♡","ᵗᑋᵃᐢᵏ ᵞᵒᵘ ♡⃝⃜","τнänκ чöü♥","⠒̫⃝♡ᵗʱᵃᵑᵏઽ","Thanks : ✚⃞ ⸌̷̻( ᷇ॢ〰ॢ ᷆◍)⸌̷̻"]
@client.on(events.NewMessage(pattern=".thanks"))
async def sorryy(ult):
  s = random.choice(thanks)
  return await ult.edit(f"{s}")

@client.on(events.NewMessage(pattern=r"^\.info"))
async def reg(event):
        me = await client.get_me()
        await event.edit(f"User Informatsiyasi\nID: {str(me.id)}\nIsm: {str(me.first_name)}\nFamiliya: {str(me.last_name)}\nUsername: {str(me.username)}\nUzBot - userbot")
        print(event)
@client.on(events.NewMessage(pattern=r"\.chats"))
async def infoconv(event):
            async for dailog in client.iter_dialogs():
            	await event.reply(dailog.name + " has id " + str(dailog.id))
            	time.sleep(5)
            	
                 
@client.on(events.NewMessage(pattern=r"\.pic .",outgoing=True))

async def sendpic(event):
        command = event.raw_text.split(".pic")
        keyword = command[1]
        url = f"https://source.unsplash.com/1600x900/?hacker{keyword},{keyword}"
        r = requests.get(url)

        with open("temp.jpg","wb") as file:
            file.write(r.content)
        print("downloaded")

        to_id = event.to_id

        await client.send_file(to_id,"temp.jpg")
        

@client.on(events.NewMessage)
async def my_event_handler(event):
    if ".type" == event.raw_text[:5]:
        orig_text = event.raw_text.split(".type ", maxsplit=1)[1]
        text = orig_text
        pb = "" 
        typing_symbol = "|"

        while(pb != orig_text):
            try:
                await event.edit(pb + typing_symbol)
                time.sleep(0.05)
 
                pb += text[0]
                text = text[1:]
 
                await event.edit(pb)
                time.sleep(0.05)
 
            except Exception  as e:
                print(e)
    			
    			
 			
    			
    			
    			
client.start()
client.run_until_disconnected()