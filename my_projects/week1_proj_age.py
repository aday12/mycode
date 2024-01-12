#! usr/bin/env python3

# add input validation
# -- stretch goals --
# reduce the amount of typing required
# add support for year if user doesnt know age
# improve output to dynamically calculate age/birth year/an interesting fact about that year

# this function asks the user for their age and based on their input classifies them as part of a generation and has a fun comment associated with it
def generation():
    while True:
        try:
    # this line sets user_age to the int of what the user inputs with blank spaces stripped from either side
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
                print("You're a Millennial. Where were you for Y2K?")
            elif user_age >= 11 and user_age <= 26:
                print("WHAT'S UP ZOOMER?!?!?!")
            elif user_age > 0 and 11 > user_age: # this line is an example of an alterative way to write similar logic to the other if/elif statements
                print("The future is yours Gen Alpha!")
            else:
                print("Hmmm seems like maybe you hadn't arrived yet")
        except TypeError:
            print("Please enter a number. For example: 42, 58, 15 etc.")
generation()



# this is the main function
def main():
    # fires teh generation function from above
    print(generation()) 
    # main only works if the user is inside of the main funciton
    if __name__ == " __main__":
        main()
