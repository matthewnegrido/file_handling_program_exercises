import os

def split_integers_by_parity(source_file):
    """Reads integers from a source file and splits them into even and odd files."""
    even_list = []
    odd_list = []

    try:
        with open(source_file, 'r') as input_file:
            for line in input_file:
                stripped_line = line.strip()
                if stripped_line:
                    number = int(stripped_line)
                    if number % 2 == 0:
                        even_list.append(str(number))
                    else:
                        odd_list.append(str(number))