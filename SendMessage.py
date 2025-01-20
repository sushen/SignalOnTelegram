import csv
import time
from pyrogram import Client

# Replace with your API credentials
# api_id = "25813834"
api_id = "25367691"
# api_hash = "e130f8698a9ac19ba738a3c66b605eb7"
api_hash = "3f5fa604eb0ebebf6581aa882b733b59"
group_id = "-1001431628031"  # Replace with your group's ID or username

# List of local image paths
image_paths = [
    r"C:\Users\user\PycharmProjects\SignalOnTelegram\image\1.jpeg"  # First image
    # r"C:\Users\user\PycharmProjects\SignalOnTelegram\image\2.jpeg",  # Second image
    # r"C:\Users\user\PycharmProjects\SignalOnTelegram\image\3.jpeg"  # Third image
]

# Create the userbot client
with Client("my_userbot", api_id, api_hash, phone_number="+8801553841687") as app:
    try:
        print("Fetching group members...")

        # Open CSV file to read members data
        with open('group_members.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            # Read first 5 members from the CSV
            members_to_message = [next(reader) for _ in range(5)]  # Get first 5 members

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

            # Send messages to the first 5 members
            for member in members_to_message:
                user_id = member[0]  # Extract User ID from CSV

                # Skip if the user has already received a message
                if user_id in sent_user_ids:
                    print(f"User ID {user_id} has already received a message. Skipping...")
                    continue

                # Send each image from the list
                for image_path in image_paths:
                    app.send_photo(user_id, photo=image_path)
                    print(f"Sent image {image_path} to User ID: {user_id}")
                    time.sleep(4)

                message = f"I will give you signal like that. You don't have to give me any membership fee. I only take 50% " \
                          f"from your profit. Say 'Yes' to join."  # Customize the message

                app.send_message(user_id, message)
                print(f"Sent message to User ID: {user_id}")
                time.sleep(4)  # Optional: Add some delay between messages

                # Write the user ID to the new CSV file after sending the message
                sent_writer.writerow([user_id])

                input("Press Enter to continue...")

        print("Messages sent to the first 5 members and their IDs saved in 'sent_messages.csv'.")

    except Exception as e:
        print(f"An error occurred: {e}")
