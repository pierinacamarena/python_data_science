import sys

# list comprehension is [new_expression for item in iterable if condition]

# lambda function receives one argument,
# word and applies function, which is used as a condition


def generate_list_of_matching_length_words(s: str, length: int) -> list:
    """
    Generates a list of words from the input string that
    are longer than a specified length.

    Args:
    s (str): The input string from which words will be extracted.
    length (int): The threshold length

    Returns:
    list: A list containing words from the input string
    that have more than `length` characters.
    """
    return [
        word for word in s.split()
        if (lambda word: len(word) > length)(word)
    ]


def main():
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"

        single_str = sys.argv[1]
        length = sys.argv[2]

        # Convert to int
        length = int(length)

        words_list = generate_list_of_matching_length_words(single_str, length)
        print(words_list)

    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
