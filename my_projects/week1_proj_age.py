#! usr/bin/env python3

# -- stretch goals --
# use file to output user's birth year and cool fact
# reduce the amount of typing required
# improve output to dynamically calculate age/birth year/an interesting fact about that year

# this function asks the user for their age and based on their input classifies them as part of a generation and has a fun comment associated with it
def name():
    while True:
        try:
            user_name=input("Hi! What's your name?\n>").strip().title()
            print(f"\nHi, {user_name}!")
            break
        except TypeError:
            print("\nPlease only input a valid name. For example: Aaron, Hutch, Michael Jordan, ajlkdjhfklajsdf")

def generation():
    while True:
        try:
    # this line sets user_age to the int of what the user inputs with blank spaces stripped from either side
            user_age=int(input("\nHow old are you? (As of 2023)\n>").strip())
            if user_age >= 123:
                print("\nYou're a member of the Lost Generation. That doesn't sound fun D:\n")
            elif user_age >= 96 and  user_age <= 122:
                print("\nYou're a member of the Greatest Generation, I salute you :D\n")
            elif user_age >= 77 and user_age <= 95:
                print("\nShhhhhhhhh, you're a member of the Silent Generation\n")
            elif user_age >= 59 and user_age <= 76:
                print("\nYOU'RE A BOOMER!!!!!!\n")
            elif user_age >= 43 and user_age <= 58:
                print("\nYou're a member of Gen X. AKA the Siltent Generation Part 2\n")
            elif user_age >= 27 and user_age <= 42:
                print("\nYou're a Millennial. Where were you for Y2K?\n")
            elif user_age >= 11 and user_age <= 26:
                print("\nWHAT'S UP ZOOMER?!?!?!\n")
            elif user_age > 0 and 11 > user_age: # this line is an example of an 
                # alterative way to write similar logic to the other if/elif statements
                print("\nThe future is yours Gen Alpha!\n")
            else:
                print("\nHmmm seems like maybe you hadn't arrived yet\n")
            break
        except TypeError:
            print("\nPlease enter a number. For example: 42, 58, 15 etc.")



# this is the main function
def main():
    # fires teh generation function from above
    name()
    generation()
    # main only works if the user is inside of the main funciton
if __name__ == "__main__":
    main()
