import sys


def identify_odd_even(number: int) -> None:
    if (number % 2 == 0):
        print("I'm even")
    else:
        print("I'm odd")


def main():
    try:
        if len(sys.argv) < 2:
            # If not, prompt the user for input
            number_to_analyze = input("What is the number you wish to check? ")
            # Convert to int
            val = int(number_to_analyze)
        else:
            # Retrieving argument and ensuring only one extra argument is given
            assert len(sys.argv) == 2, "more than one argument is provided"
            number_to_analyze = sys.argv[1]
            # Convert to int
            val = int(number_to_analyze)

        # Function that checks odd/even
        identify_odd_even(val)

    except AssertionError as error:
        print(error)
    except ValueError:
        print("Error: The argument is not an integer")


if __name__ == "__main__":
    main()
