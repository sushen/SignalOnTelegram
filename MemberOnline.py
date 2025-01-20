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

# Create the userbot client
with Client("my_userbot", api_id, api_hash, phone_number="+8801553841687") as app:
    try:
        # Fetch user status (globally, not in a specific group)
        user = app.get_users(user_id)

        # You can use 'user.status' to check if they are online
        if user.status == "UserStatus.ONLINE":
            print(f"User ID {user_id} is online.")
        elif user.status == "offline":
            print(f"User ID {user_id} is offline.")
        else:
            print(f"User ID {user_id} status is: {user.status}")

    except Exception as e:
        print(f"An error occurred: {e}")
