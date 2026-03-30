# Chapter3.py
# Chapter 3 – Surface Below

def play_chapter3():
    print("=== Chapter 3: Surface Below ===")
    print("Nova takes a shuttle from the lower deck down to the planet.")
    print("She lands near an old relay tower on the surface.")

    choice = input("Do you want to scan the tower first? (y/n): ").strip().lower()

    if choice == "y" or choice == "yes":
        print("Nova uses her scanner on the relay tower.")
        print("The scan shows a hidden entrance to an underground base.")
        saved_data = True
    else:
        print("Nova opens the tower manually and searches inside.")
        print("She finds coordinates to an underground base written in old logs.")
        saved_data = False

    print('Nova gets the coordinates to the underground base, "Heart of Erevos".')
    print("=== End of Chapter 3 ===")

    return saved_data
