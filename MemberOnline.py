from pyrogram import Client

# Replace with your API credentials
api_id = "25813834"
api_hash = "e130f8698a9ac19ba738a3c66b605eb7"
user_id = 6763991026  # Replace with the user ID you want to check

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
