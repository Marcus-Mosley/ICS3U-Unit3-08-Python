#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on September 2020
# This program checks if a year is a leap year


def main():
    # This function checks if a year is a leap year

    # Input
    year = int(input("Please enter the year: "))
    print("")

    # Process & Output
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("The year {0} is a leap year (366 Days)!" .format(year))
            else:
                print("The year {0} is not a leap year (365 Days)!"
                      .format(year))
        else:
            print("The year {0} is a leap year (366 Days)!" .format(year))
    else:
        print("The year {0} is not a leap year (365 Days)!" .format(year))


if __name__ == "__main__":
    main()
