#! usr/bin/env python3
def generation():
    user_age=int(input("How old are you? (As of 2023)\n>").strip())

    if user_age >= 123:
        print("You're a member of the Lost Generation. That doesn't sound fun D:")
    elif user_age >= 96 and  user_age <= 122:
        print("You're a member of the Greatest Generation, I salute you :D")
    elif user_age >= 77 and user_age <= 95:
        print("Shhhhhhhhh, you're a member of the Silent Generation")
    elif user_age >= 59 and user_age <= 76:
        print("YOU'RE A BOOMER!!!!!!")
    elif user_age >= 43 and user_age <= 58:
        print("You're a member of Gen X. AKA the Siltent Generation Part 2")
    elif user_age >= 27 and user_age <= 42:
        print("You're a Mellennial. Where were you for Y2K?")
    elif user_age >= 11 and user_age <= 26:
        print("WHAT'S UP ZOOMER?!?!?!")
    elif user_age > 0 and 11 > user_age:
        print("The future is yours Gen Alpha!")
    else:
        print("Hmmm seems like maybe you hadn't arrived yet")

generation()
