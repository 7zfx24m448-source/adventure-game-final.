from player import Player
from Chapter1 import play_chapter1
from Chapter2 import play_chapter2
from Chapter3 import play_chapter3
from Chapter4 import play_chapter4
from Chapter5 import play_chapter5

def main():
    print("Welcome to the Adventure Game: Erevos-9")
    name = input("Enter your player name: ").strip()
    if name == "":
        name = "Nova"

    player = Player(name)

    play_chapter1()
    play_chapter2()
    player.saved_data = play_chapter3()
    player.trusted_ai = play_chapter4()
    play_chapter5(player.trusted_ai, player.saved_data)

if __name__ == "__main__":
    main()
