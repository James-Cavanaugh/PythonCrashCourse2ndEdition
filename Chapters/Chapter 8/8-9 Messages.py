messages_list = ["hey", "i", "just", "met", "you"]
sent_messages = []

def show_messages(messages):
    while messages:
        print(messages.pop(0))

show_messages(messages_list)