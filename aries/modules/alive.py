from telethon import Button

from aries import telethn as tbot
from aries.events import register

PHOTO = "https://telegra.ph/file/34d0fad97f53b4c0de15b.jpg"


@register(pattern=("/alive|/ALIVE"))
async def awake(event):
    event.sender.first_name
    ARIES = "**Hello im Ken Kaneki** \n\n"
    ARIES += "**ALL SYSTEM WORKING PROPERLY**\n\n"
    ARIES += "  ⌊ **Python :** __3.9.7__ ⌉\n\n"
    ARIES += "  ⌊ **Pyrogram :** __1.2.9__ ⌉\n\n"
    ARIES += "  ⌊ **MongoDB :** __2.5.1__ ⌉\n\n"
    ARIES += "  ⌊ **Platform :** __linux__ ⌉\n\n"
    ARIES += "  ⌊ **My Lord** : [Aftrr](https://t.me/Invincible_itAchi) ☠⌉\n\n"
    ARIES += "  ⌊ **Ken kaneki** ⌉\n\n"
    ARIES += "  ⌊ **TELETHON : 6.6.6 Latest** ⌉\n\n"
    ARIES += " |||| || ||| |||| || |||||| ||||| || || ||"
    BUTTON = [
        [
            Button.url("Support", "https://t.me/Ft999_eXe"),
            Button.url("Owner", "https://t.me/Invincible_itAchi"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=ARIES, buttons=BUTTON)


__mod_name__ = "Alive"
