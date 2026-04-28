import os

class FileCategorizer:
    def __init__(self, source_file="numbers.txt"):
        self.source_file = source_file
        self.even_file = "even.txt"
        self.odd_file = "odd.txt"

    def process_data(self):
        try:
            with open(self.source_file, 'r') as file_reader:
                raw_data = file_reader.read().split()
                numbers_list = [int(num) for num in raw_data]

            even_numbers = [str(n) for n in numbers_list if n % 2 == 0]
            odd_numbers = [str(n) for n in numbers_list if n % 2 != 0]

            self.write_output(self.even_file, even_numbers)
            self.write_output(self.odd_file, odd_numbers)

            print(f"Done! Created {self.even_file} and {self.odd_file}.")