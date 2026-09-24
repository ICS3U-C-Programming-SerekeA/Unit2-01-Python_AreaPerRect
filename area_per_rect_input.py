#!/usr/bin/env python3
# Created By: Sereke Asfeday
# Date: Sep. 24th, 2026
# This program asks the user for the length and width
# a rectangele, calculates and diplays the area and perimeter
# .back to the user with proper units.


def main():
    # get the legth from user and convert to an integer
    length = int(input("Enter length of the rectangle (cm): "))

    # get the width from user and convert to an integer
    width = int(input("Enter width of the rectangle (cm): "))

    # calculate the area and perimeter of rectangle
    area = length * width
    perimeter = 2 * (length + width)
    print("The perimeter is: {}cm".format(perimeter))

    # display the area to the user with proper units.
    print("The area is: {}cm²".format(area))


if __name__ == "__main__":
    main()
