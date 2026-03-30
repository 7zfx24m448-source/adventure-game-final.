# Chapter5.py
# Chapter 5 – Rebirth or Ruin

def play_chapter5(trusted_ai, saved_data):
    print("=== Chapter 5: Rebirth or Ruin ===")
    print("The final outcome depends on Nova's choices.")

    if trusted_ai:
        print("Nova trusted the AI.")
        print("The AI uses the station and the underground base to help fix Earth's systems.")
        print("The station survives, and slowly the planet begins to recover.")
    else:
        print("Nova shut down the AI.")
        print("Without the AI, the systems begin to fail.")
        print("The station and the planet remain badly damaged.")

    print()

    if saved_data:
        print("Because Nova collected enough data earlier,")
        print("humans keep important knowledge for the future.")
    else:
        print("Nova did not save much data earlier.")
        print("A lot of knowledge is lost with the AI and the old systems.")

    print("=== End of Game ===")
