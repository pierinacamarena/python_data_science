import sys

def identify_odd_even(number: int) -> None:
    if (number % 2 == 0):
        print("I'm even")
    else:
        print("I'm odd")

def main():
    try:

        #Ensuring only one extra argument is given
        assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"

        #retriving argument
        argument = sys.argv[1]

        #attempt to convert to an int
        val = int(argument)

        #function that checks odd/even
        identify_odd_even(val)

    #printing errors
    except AssertionError as error:
        print(error)
    except ValueError:
        print("AssertionError: argument is not an integer")

if __name__ == "__main__":
    main()
