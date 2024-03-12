import sys

def cypher_to_morse_code(s: str) -> str:
    # Dictionary representing the morse code chart
    NESTED_MORSE = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ' ':'/'}
    
    s = s.upper()
    # result_string = 'separator'.join(transform_function(item) for item in iterable if condition(item))
    morse_string = ''.join(NESTED_MORSE[char] for char in s if char in NESTED_MORSE)

    return morse_string

def is_space_or_alnum(s: str) -> bool:
    return all(char.isalnum() or char.isspace() for char in s)

def main():
    try:
        assert len(sys.argv) == 2, "AssertionError: the arguments are bad"

        string_to_convert = sys.argv[1]

        validity_check = is_space_or_alnum(string_to_convert)
        assert validity_check, "AssertionError: the arguments are bad"

        morse_string = cypher_to_morse_code(string_to_convert)
        print(morse_string)
    except AssertionError as error:
        print(error)
        return 1
    return 0

if __name__ == "__main__":
    main() 