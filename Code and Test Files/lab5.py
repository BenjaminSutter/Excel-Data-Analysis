"""
Name: Ben Sutter
Date: November 3rd, 2020
Class: SDEV 300
Purpose: A program that reads columns from a file and shows their count, mean, min, max,
standard deviation, and prints a histogram representing the data.
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt


def round_and_format(number):
    """If number is int, typecast it to int. If it is a float then round to 2 decimal places.
    Return number as string for easier printing."""
    if str(abs(number)).isdigit():
        return str(f"{number:,d}")
    return str('{:,.2f}'.format(number))


def print_statistics(file, column):
    """Takes file name and column as parameters. Prints count, mean, min, max, and standard dev.
    Also prints histogram"""
    print("Count: " + round_and_format(file[column].count())
          + "\nMean: " + round_and_format(file[column].mean(axis=0))
          + "\nMin: " + round_and_format(file[column].min(axis=0))
          + "\nMax: " + round_and_format(file[column].max(axis=0))
          + "\nStandard Deviation: " + round_and_format(file[column].std(axis=0))
          + "\nThe Histogram of this column is now displayed. \n")
    # If count is less than 1000 (population file) make bins 100 so things are somewhat visible
    if file[column].count() < 1000:
        num_of_bins = 100
        # Turns off scientific notation
        plt.ticklabel_format(style='plain', useOffset=False)
    else:
        num_of_bins = 20
    plt.suptitle(column)  # Set title of the graph
    file[column].plot(kind='hist', bins=num_of_bins)  # Create a histogram based off of column
    plt.show()  # Show the histogram


# Creates a panda dataframe from the opulation file with the three needed columns
pop_file = pd.read_csv("PopChange.csv", usecols=["Pop Apr 1", "Pop Jul 1", "Change Pop"])
# Creates a panda dataframe from the housing file with the five needed columns
housing_file = pd.read_csv("Housing.csv", usecols=["AGE", "BEDRMS", "BUILT", "ROOMS", "UTILITY"])

# Saving the string for file choices (and exit)
FILE_CHOICES = ("\nSelect the file you want to analyze:"
                "\n1. Population Data"
                "\n2. Housing Data"
                "\n3. Exit the Program\n")

# Saving the string for interaction options with the population file
POPULATION_OPTIONS = ("Select the Column you want to analyze:"
                      "\na. Pop Apr 1"
                      "\nb. Pop Jul 1"
                      "\nc. Change Pop"
                      "\nd. Exit population data\n")

# Saving the string for interaction options with the housing file
HOUSING_OPTIONS = ("\nSelect the Column you want to analyze:"
                   "\na. AGE"
                   "\nb. BEDROOMS"
                   "\nc. BUILT"
                   "\nd. ROOMS"
                   "\ne. UTILITY"
                   "\nf. Exit housing data\n")

file_selection = input("Welcome to the program!" + FILE_CHOICES)
while file_selection != "3":

    # While input is an invalid selection, loop til selection is valid.
    while file_selection not in ("1", "2", "3"):
        file_selection = input("Please select a valid option (1-3): ")

    if file_selection == "1":
        print("You have entered population data. ")
        # Holds the value to track user choices in the population file menu
        column_selection = input(POPULATION_OPTIONS)

        while column_selection.lower() != "d":
            # While input is an invalid selection, loop til selection is valid.
            while column_selection.lower() not in ("a", "b", "c", "d"):
                column_selection = input("Please select a valid option (a, b, c, or d): ")

            # Prints Apr 1 statistics from population file and Pop Apr 1 column
            if column_selection.lower() == "a":
                print("You selected Pop Apr 1")
                print_statistics(pop_file, 'Pop Apr 1')

            # Prints Jul 1 statistics from population file and Pop Jul 1 column
            elif column_selection.lower() == "b":
                print("You selected Pop Jul 1")
                print_statistics(pop_file, 'Pop Jul 1')

            # Prints Change Pop statistics from population file and Change Pop column
            elif column_selection.lower() == "c":
                print("You selected Change Pop")
                print_statistics(pop_file, 'Change Pop')

            # If selection is not d (exit) then reset choice
            if column_selection.lower() != "d":
                column_selection = input(POPULATION_OPTIONS)

        # Selection is d so notify user they exited
        print("You selected to exit population data")

    elif file_selection == "2":
        print("You have entered Housing Data.")
        # Holds the value to track user choices in the housing file menu
        column_selection = input(HOUSING_OPTIONS)
        while column_selection.lower() != "f":
            # While input is an invalid selection, loop til selection is valid.
            while column_selection.lower() not in ("a", "b", "c", "d", "e", "f"):
                column_selection = input("Please select a valid option (a, b, c, d, e, or f): ")

            # Prints AGE statistics from housing file and AGE column
            if column_selection.lower() == "a":
                print("You selected AGE")
                print_statistics(housing_file, 'AGE')

            # Prints BEDRMS statistics from housing file and BEDRMS column
            elif column_selection.lower() == "b":
                print("You selected BEDRMS")
                print_statistics(housing_file, 'BEDRMS')

            # Prints BUILT statistics from housing file and BUILT column
            elif column_selection.lower() == "c":
                print("You selected BUILT")
                print_statistics(housing_file, 'BUILT')

            # Prints ROOMS statistics from housing file and ROOMS column
            elif column_selection.lower() == "d":
                print("You selected ROOMS")
                print_statistics(housing_file, 'ROOMS')

            # Prints ROOMS statistics from housing file and ROOMS column
            elif column_selection.lower() == "e":
                print("You selected UTILITY")
                print_statistics(housing_file, 'UTILITY')

            # If selection is not f (exit) then reset choice
            if column_selection.lower() != "f":
                column_selection = input(HOUSING_OPTIONS)

        # Selection is f so notify user they exited
        print("You selected to exit housing data")

    # End of yes selection so reset choice
    if file_selection != "3":
        file_selection = input(FILE_CHOICES)

# The while loop has ended because option 3 was selected so thank the user and exit
print("Thank you for using the program, have a nice day!")
sys.exit()
