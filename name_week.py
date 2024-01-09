#!/usr/bin/env python3

def main():
    # ask user their name and store as var
    user_name = input("Enter your name:")
    # confirm user name
    print("Your name is: " + user_name.strip())
    # ask day of week
    today = input("\nWhat day is today?")
    # confirm day of week
    print("Today is: " + today.strip())
    # returns response
    print("\nHello, " + user_name.strip() + "! Happy " + 
            today.strip(), end="!\n")

main()
