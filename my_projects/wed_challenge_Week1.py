#! /bin/user/env python3

def main():

    user_info=[]

    name = input("What is your name?").strip().capitalize()
    age = input("How old are you?").strip()
    movie = input("What's your favorite movie?").strip().capitalize()

    user_info.append(f"Hello, {name}!")
    user_info.append(f" You are: {age} years old")
    user_info.append(f" and your favorite movie is: {movie}.")


    print("".join(user_info))
main()
