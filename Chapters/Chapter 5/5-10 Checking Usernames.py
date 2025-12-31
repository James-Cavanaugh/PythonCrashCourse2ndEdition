current_users = ["jiimz", "crimson", "tuxx", "1michi1", "dreamer"]
lower_current_users = [user.lower() for user in current_users]
new_users = ["tuxx", "dreamer", "swift", "sleetso", "proxxy"]
for user in new_users:
    if user.lower() in lower_current_users:
        print("You will need to enter a new username")
    else:
        print("Your username is available")