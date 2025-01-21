import csv
from pyrogram import Client

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Replace with your API credentials
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
group_id = os.getenv("GROUP_ID")  # Replace with your group's ID or username
phone_number = os.getenv("PHONE_NUMBER")

with Client("my_userbot", api_id, api_hash, phone_number=phone_number) as app:
    try:
        print("Fetching group members...")

        # Open CSV file to write members data
        with open('group_members.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write header row
            writer.writerow(["User ID", "Username", "Full Name"])

            # Fetch group members with pagination
            members = app.get_chat_members(group_id)

            for member in members:
                user_id = member.user.id
                username = member.user.username or "N/A"
                full_name = f"{member.user.first_name or ''} {member.user.last_name or ''}".strip()

                # Write member details to the CSV file
                writer.writerow([user_id, username, full_name])

        print("All group members have been saved to 'group_members.csv'.")

    except Exception as e:
        print(f"An error occurred: {e}")
