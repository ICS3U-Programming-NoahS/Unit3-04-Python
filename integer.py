#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Oct. 18th, 2023
# This program asks the user to enter an integer
# and tells the user if it is positive, negative or just zero.


def main():
    # Get the user's number
    user_number = int(input("Enter an integer: "))

    # Check if user's number is negative, positive, or zero
    if user_number < 0:
        print("{} is negative.".format(user_number))
    elif user_number > 0:
        print("{} is positive.".format(user_number))
    else:
        print("{} is just zero!".format(user_number))


if __name__ == "__main__":
    main()
