from typing import Union
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton
from NOBITA import app
from NOBITA.utils import help_pannel
from NOBITA.utils.database import get_lang
from NOBITA.utils.decorators.language import LanguageStart, languageCB
from NOBITA.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers
from NOBITA.help.buttons import BUTTONS
from NOBITA.help.helper import Helper

#------------------------------------------------------------------------------------------------------------------------
# MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | MUSIC | 
#------------------------------------------------------------------------------------------------------------------------





@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))

@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=keyboard)
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboard)





#------------------------------------------------------------------------------------------------------------------------
# MANAGEMENT | MANAGEMENT | MANAGEMENT | MANAGEMENT | MANAGEMENT | MANAGEMENT | MANAGEMENT | MANAGEMENT | MANAGEMENT | 
#------------------------------------------------------------------------------------------------------------------------





@app.on_callback_query(filters.regex("MANAGEMENT_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_M, reply_markup=InlineKeyboardMarkup(BUTTONS.MBUTTON))
    
        
@app.on_callback_query(filters.regex('MANAGEMENT_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(
    [
    [
    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"MANAGEMENT_CP")
    ]
    ]
    )
    if cb == "MANAGEMENT":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)





#------------------------------------------------------------------------------------------------------------------------
# TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL | TOOL |
#------------------------------------------------------------------------------------------------------------------------





@app.on_callback_query(filters.regex("TOOL_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_B, reply_markup=InlineKeyboardMarkup(BUTTONS.BBUTTON))


@app.on_callback_query(filters.regex('TOOL_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(
    [
    [
    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"TOOL_CP")
    ]
    ]
    )
    if cb == "TOOL":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)






#------------------------------------------------------------------------------------------------------------------------
# MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP | MAIN HELP |
#------------------------------------------------------------------------------------------------------------------------





@app.on_callback_query(filters.regex("MAIN_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_NOBITA, reply_markup=InlineKeyboardMarkup(BUTTONS.SBUTTON))

        
@app.on_callback_query(filters.regex('MAIN_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(
    [
    [
    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"MAIN_CP")
    ]
    ]
    )
    if cb == "MAIN":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)




#------------------------------------------------------------------------------------------------------------------------
# PROMOTION | PROMOTION | PROMOTION | PROMOTION | PROMOTION | PROMOTION | PROMOTION | PROMOTION | PROMOTION | PROMOTION |
#------------------------------------------------------------------------------------------------------------------------


@app.on_callback_query(filters.regex("PROMOTION_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_PROMOTION, reply_markup=InlineKeyboardMarkup(BUTTONS.PBUTTON))

        
@app.on_callback_query(filters.regex('PROMOTION_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(
    [
    [
    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"PROMOTION_CP")
    ]
    ]
    )
    if cb == "PROMOTION":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)

        
        

#------------------------------------------------------------------------------------------------------------------------
# ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | ALL BOT'S | 
#------------------------------------------------------------------------------------------------------------------------



@app.on_callback_query(filters.regex("ALLBOT_CP") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_ALLBOT, reply_markup=InlineKeyboardMarkup(BUTTONS.ABUTTON))

        
@app.on_callback_query(filters.regex('ALLBOT_BACK'))      
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(
    [
    [
    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"ALLBOT_CP")
    ]
    ]
    )
    if cb == "ALLBOT":
        await CallbackQuery.edit_message_text(f"`something errors`",reply_markup=keyboard,parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
