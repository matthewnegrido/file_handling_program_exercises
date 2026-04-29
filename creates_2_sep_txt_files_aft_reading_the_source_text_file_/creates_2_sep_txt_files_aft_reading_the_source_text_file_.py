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

        with open('even_numbers.txt', 'w') as even_file:
            even_file.write('\n'.join(even_list))

        with open('odd_numbers.txt', 'w') as odd_file:
            odd_file.write('\n'.join(odd_list))

        print("Success: Created 'even_numbers.txt' and 'odd_numbers.txt'.")

    except FileNotFoundError:
        print(f"Error: {source_file} not found.")
    except ValueError:
        print("Error: File contains non-integer data.")

if __name__ == "__main__":
    target_source = "integers.txt"
    if not os.path.exists(target_source):
        with open(target_source, "w") as creator:
            sample_data = [str(i) for i in range(1, 21)]
            creator.write('\n'.join(sample_data))

    split_integers_by_parity(target_source)