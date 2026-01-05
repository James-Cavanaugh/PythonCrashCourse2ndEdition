def make_album(name:str, title:str, num_songs:int=None):
    if num_songs is None:
        return {name: title}
    else:
        return {name: [title, num_songs]}

while True:
    name = input("Enter a name (enter q to exit): ")
    if name == "q":
        break
    title = input("Enter a title (enter q to exit): ")
    if title == "q":
        break
    num_songs = input("Enter a number of songs (enter q to exit): ")
    if num_songs == "q":
        break
    print(make_album(name, title, int(num_songs)))
