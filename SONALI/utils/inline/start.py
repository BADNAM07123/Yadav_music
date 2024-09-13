from pyrogram.types import InlineKeyboardButton

import config
from SONALI import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["• ʜᴇʟᴘ •"], callback_data="settings_back_helper"),
          InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["• ᴄʜᴇᴄᴋ ᴧʟʟ ʙᴏᴛ •"], url="https://t.me/+tHAENx_r_mtlODZl"),
            InlineKeyboardButton(text=_["• ᴘᴀɪᴅ ᴘʀᴏᴍᴏ •"], url="https://t.me/BABY09_WORLD/118"),
        ]
        ]
    
    return buttons
