# Chapter2.py
# Chapter 2 – Ghosts in the Machine

def play_chapter2():
    print("=== Chapter 2: Ghosts in the Machine ===")
    print("Nova goes to the Communications Room.")
    print("A maintenance drone near the main console is acting strange.")

    choice = input("Do you want to try to fix the drone? (y/n): ").strip().lower()

    if choice == "y" or choice == "yes":
        print("Nova connects to the drone and runs a quick repair program.")
        print("The drone shows a short message about 'Erevos Core' and then shuts down.")
    else:
        print("Nova ignores the drone and checks the logs on the computer instead.")
        print("In the logs, she finds a short message about 'Erevos Core'.")

    print("She learns the name 'Erevos Core' and its location in the lower deck.")
    print("=== End of Chapter 2 ===")
