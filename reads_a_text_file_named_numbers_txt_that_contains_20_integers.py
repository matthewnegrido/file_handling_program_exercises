import os

class FileCategorizer:
    def __init__(self, source_file="numbers.txt"):
        self.source_file = source_file
        self.even_file = "even.txt"
        self.odd_file = "odd.txt"