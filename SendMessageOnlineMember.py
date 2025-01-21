import csv
import time
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

# List of local image paths
image_paths = [
    r"C:\Users\user\PycharmProjects\SignalOnTelegram\image\1.jpeg"  # First image
    # r"C:\Users\user\PycharmProjects\SignalOnTelegram\image\2.jpeg",  # Second image
    # r"C:\Users\user\PycharmProjects\SignalOnTelegram\image\3.jpeg"  # Third image
]

# Create the userbot client
with Client("my_userbot", api_id, api_hash, phone_number=phone_number) as app:
    try:
        print("Fetching group members...")

        # Open CSV file to read members data
        with open('group_members.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            # Read all members from the CSV
            members_to_message = [row for row in reader]  # Get all members

        # Open the 'sent_messages.csv' to check which users have already received messages
        sent_user_ids = set()
        try:
            with open('sent_messages.csv', mode='r', encoding='utf-8') as sent_file:
                sent_reader = csv.reader(sent_file)
                next(sent_reader)  # Skip the header row
                # Load all user IDs that have already received a message into a set
                sent_user_ids = {row[0] for row in sent_reader}
        except FileNotFoundError:
            # If the file doesn't exist yet, we simply continue without checking
            pass

        # Open a new CSV file to store the user IDs of those we sent messages to
        with open('sent_messages.csv', mode='a', newline='', encoding='utf-8') as sent_file:
            sent_writer = csv.writer(sent_file)
            # Check if the file is empty and write the header if needed
            if sent_file.tell() == 0:
                sent_writer.writerow(["User ID"])

            # Send messages to all members
            for index, member in enumerate(members_to_message, 1):
                user_id = member[0]  # Extract User ID from CSV

                # Skip if the user has already received a message
                if user_id in sent_user_ids:
                    print(f"{index}. User ID {user_id} has already received a message. Skipping...")
                    continue

                # Fetch the user's data and log the response
                user = app.get_users(user_id)
                # print(f"{index}. Full response for User ID {user_id}: {user}")


                # Check if user is online by looking at the status attribute
                if user.status and "ONLINE" in str(user.status).upper():
                    print(f"{index}. User ID {user_id} is online. Sending message...")

                    # Send each image from the list
                    for image_path in image_paths:
                        app.send_photo(user_id, photo=image_path)
                        print(f"{index}. Sent image {image_path} to User ID: {user_id}")
                        time.sleep(4)

                    message = f"I will give you signal like that. You don't have to give me any membership fee. I only take 50% " \
                              f"from your profit. Say 'Yes' to join."  # Customize the message

                    app.send_message(user_id, message)
                    print(f"{index}. Sent message to User ID: {user_id}")
                    time.sleep(4)  # Optional: Add some delay between messages

                    # input(f"{index} Stop:")

                else:
                    print(f"{index}. User ID {user_id} is not online. Skipping...")

                # Add a delay between requests to avoid flooding
                time.sleep(1)  # Adjust this delay based on your needs


        print("Messages sent to all members and their IDs saved in 'sent_messages.csv'.")
    except Exception as e:
        print(f"An error occurred: {e}")



