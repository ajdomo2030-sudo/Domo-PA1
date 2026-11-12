git init
def display_playlist():
    songs = ["See you again", "Darling I", "she"]

    print("\n===== MY PLAYLIST =====")
    for number, song in enumerate(songs, start=1):
        print(f"{number}. {song}")
