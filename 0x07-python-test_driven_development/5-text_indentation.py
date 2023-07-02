#!/usr/bin/python3

"""
function that prints a text with 2 new lines after
each of these characters: ., ?
"""


def text_indentation(text):
    """
    Prints the given text with 2 new lines
    after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If `text` is not a string.

    Examples:
        >>> text_indentation("Hello. How are you? I'm fine.")
        Hello
        How are you
        I'm fine

        >>> text_indentation("This is a test: testing.")
        This is a test
        testing

        >>> text_indentation("No newline characters here")
        No newline characters here

        >>> text_indentation("")

        >>> text_indentation(123)
        TypeError: text must be a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punc = text.replace(".", ".\n\n")
    punc = punc.replace("?", "?\n\n")
    punc = punc.replace(":", ":\n\n")
    new_line = punc.split("\n")
    for line in range(len(new_line)):
        print("{}".format(new_line[line].strip()),
              end=("" if (line == (len(new_line) - 1)) else "\n"))
