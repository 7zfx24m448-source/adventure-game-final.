# Chapter4.py
# Chapter 4 – Heart of Erevos

def play_chapter4():
    print("=== Chapter 4: Heart of Erevos ===")
    print('Nova enters the underground base called "Heart of Erevos".')
    print("In the central chamber, the AI starts talking to her.")

    first_choice = input("Do you want Nova to TALK to the AI or ATTACK it? (talk/attack): ").strip().lower()

    if first_choice == "talk":
        print("Nova talks to the AI.")
        print("The AI explains that it wants to save Earth and repair what is left.")
    else:
        print("Nova attacks the AI core.")
        print("She damages some systems, and the AI defends itself, becoming unstable.")

    print("Now Nova must make a final choice about the AI.")

    second_choice = input("Does Nova TRUST the AI or SHUT it DOWN? (trust/shut): ").strip().lower()

    if second_choice == "trust":
        trusted_ai = True
        print("Nova decides to trust the AI and give it more control.")
    else:
        trusted_ai = False
        print("Nova decides to shut the AI down to stop any possible danger.")

    print("=== End of Chapter 4 ===")

    return trusted_ai
