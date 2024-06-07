

import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from STARXMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["ميوزك", "الميوزك", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://telegra.ph/file/814dd1f4e602e5049202b.jpg",
        caption=f"""مرحبا بك عزيزي في اوامر بوت الميوزك 🎸 ⋅\n- اسمك : {message.from_user.mention} 💘 ⋅\n- عليك استخدام الازرار بالاسفل لتصفح اوامر الميوزك 🎸 ⋅ \n\n• ⌯ 𝚂𝙾𝚞𝚁𝙲𝙴 𝚂𝚃𝙰𝚁 ⌯ • </b>""",
        reply_markup=InlineKeyboardMarkup(
            [https://telegra.ph/file/0f312fc46fead5bf7afc7.jpg
                [
                    InlineKeyboardButton(
                        "• ⌯ اوامر التشغيل ⌯ •", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "• ⌯ اوامر القناة ⌯ •", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "• ⌯ اوامر الادمن ⌯ •", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "• ⌯ اوامر المطور ⌯ •", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "𝚂𝙾𝚞𝚁𝙲𝙴 𝚂𝚃𝙰𝚁", url="https://t.me/SOURCE_S_TAR"),
                ],
            ]
        ),
    )
      

