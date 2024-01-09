#!~/mycode/name_week.py

def main():
    # ask user their name and store as var
    user_name = input("Enter your name:")
    # confirm user name
    print("Your name is: " + user_name.strip())
    # ask day of week
    today = input("What day is today?")
    # confirm day of week
    print("Today is: " + today.strip())
    # returns response
    print("Hello, " + user_name.strip() + "! Happy " + 
            today.strip(), end="!\n")

main()
