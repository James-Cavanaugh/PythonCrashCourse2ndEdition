# 8-10 Sending Messages

messages_list = ["hey", "i", "just", "met", "you"]
sent_messages = []

def show_messages(messages):
    while messages:
        print(messages[0])
        sent_messages.append(messages.pop(0))

show_messages(messages_list[:])
print(messages_list)
print(sent_messages)