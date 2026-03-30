# Asylbek Murzakulov
# Chapter1.py
# Chapter 1 – The Signal

def play_chapter1():
    print("=== Chapter 1: The Signal ===")
    print("Nova is working on the space station Erevos-9.")
    print("She hears a strange signal calling her name.")

    choice = input("Do you want to investigate the signal? (y/n): ").strip().lower()

    if choice == "y" or choice == "yes":
        print("Nova opens the console and sees strange data on the screen.")
    else:
        print("Nova tries to ignore the signal,")
        print("but an alarm starts ringing and forces her back to the console.")

    print("Nova decides to find where the signal is coming from.")
    print("=== End of Chapter 1 ===")
