favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

should_take = ["jen", "edward", "james", "bowen"]
for name in should_take:
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll {name.title()}")
    else:
        print(f"You should take the poll {name.title()}")
