from pyrogram import Client

api_id = "25813834"
api_hash = "e130f8698a9ac19ba738a3c66b605eb7"

with Client("my_userbot", api_id, api_hash, phone_number="+8801553841687") as app:
    print("Fetching chats...")
    for dialog in app.get_dialogs():
        print(f"Chat: {dialog.chat.title}, ID: {dialog.chat.id}")
