from pyrogram import Client
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Replace with your API credentials
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
user_id = 6763991026  # Replace with the user ID you want to check
phone_number = os.getenv("PHONE_NUMBER")

# Create the userbot client
with Client("my_userbot", api_id, api_hash, phone_number=phone_number) as app:
    try:
        # Fetch user details
        user = app.get_users(user_id)

        # Check if the user has a status
        if user.status:
            # Convert the status to a string for matching
            status_str = str(user.status)

            # Handle online and offline statuses
            if "ONLINE" in status_str:
                print(f"User ID {user_id} is online.")
            elif "OFFLINE" in status_str:
                print(f"User ID {user_id} is offline.")
            else:
                print(f"User ID {user_id} has an unhandled status: {status_str}")
        else:
            print(f"User ID {user_id} does not have a status attribute.")

    except Exception as e:
        print(f"An error occurred: {e}")
