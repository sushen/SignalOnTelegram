from pyrogram import Client

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Replace with your API credentials
# api_id = "25813834"
api_id = os.getenv("API_ID")
# api_hash = "e130f8698a9ac19ba738a3c66b605eb7"
api_hash = os.getenv("API_HASH")
group_id = os.getenv("GROUP_ID")  # Replace with your group's ID or username
phone_number = os.getenv("PHONE_NUMBER")

with Client("my_userbot", api_id, api_hash, phone_number=phone_number) as app:
    print("Fetching chats...")
    for dialog in app.get_dialogs():
        print(f"Chat: {dialog.chat.title}, ID: {dialog.chat.id}")
