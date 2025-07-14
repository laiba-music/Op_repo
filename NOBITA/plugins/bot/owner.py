from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from NOBITA import app
from config import BOT_USERNAME
from NOBITA.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬───────────────────⦿
│├───────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - ʀɪsʜᴜ sᴀɴᴀᴛᴀɴɪ
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - ʀɪsʜᴜ ʀᴀᴊᴘᴜᴛ
│├───────────────────╯
├┼───────────────────⦿
├┤~ @NOBITA_MUSIC_SUPPORT
├┤~ @YOUR_NOBITA_001
├┤~ @NOBITA_MUSIC_ROBOT
├┼──────────────────────────⦿
│├──────────────────────────╮
│├OWNER│ @ll_NOBITA_DEFAULTERS_ll
│├──────────────────────────╯
└┴──────────────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝚴 𝐎 𝐁 𝚰 𝐓 𝚲", url=f"https://t.me/ll_NOBITA_DEFAULTERS_ll")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/+wPjAlUcObehiZDM1"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://t.me/NOBITA_MUSIC_SUPPORT"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/NOBITA_MUSIC_SUPPORT"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/NOBITA_MUSIC_ROBOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/tcz7s6.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
