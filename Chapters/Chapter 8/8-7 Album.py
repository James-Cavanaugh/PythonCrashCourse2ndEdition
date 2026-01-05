def make_album(name:str, title:str, num_songs:int=None):
    if num_songs is None:
        return {name: title}
    else:
        return {name: [title, num_songs]}


print(make_album("Michael Jackson", "Thriller"))
print(make_album("Michael Jackson", "Bad"))
print(make_album("Michael Jackson", "Off the Wall"))
print(make_album("Michael Jackson", "Dangerous", 14))