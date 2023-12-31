#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python


# Use imports here
from colorama import Fore, Back, Style
from my_function import isPerfect

# Define functions here ...

maximum_number = 500


def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')

        # dividers = getDividers(i)
        # print('Number ' + str(i) + ' has dividers ' +str(dividers))


if __name__ == "__main__":
    main()