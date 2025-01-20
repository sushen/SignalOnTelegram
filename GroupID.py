from pyrogram import Client

api_id = "25813834"
api_hash = "e130f8698a9ac19ba738a3c66b605eb7"

with Client("my_userbot", api_id, api_hash, phone_number="+8801553841687") as app:
    chat = app.get_chat("-1001431628031")  # Replace with the group's @username or invite link
    print(f"Group ID: {chat.id}")
