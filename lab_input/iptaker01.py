#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - display data to std out"""

# below is a function containing our code
def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter an IPv4 IP address:")
    
    # display the input back to the user. used a comma here to make userinput output any datatype instead of just a string
    print("You told me the IPv4 address is: ", user_input)
    
    # ask user for the vendor name
    user_input_2 = input("Your ISP is:")

    # confirm user input 2 is correct. concat w/ + here to only allow a string
    print("You said your ISP is:" + user_input_2)

# this calls main
main()

