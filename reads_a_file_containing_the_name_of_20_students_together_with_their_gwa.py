import os

class GradeAnalyzer:
    def __init__(self, source_file="students.txt"):
        self.source_file = source_file

    def find_highest_gwa(self):
        try:
            highest_student = None
            highest_gwa = -1.0

            with open(self.source_file, 'r') as file_reader:
                for line in file_reader:
                    if not line.strip():
                        continue

                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        student_name = parts[0].strip()
                        current_gwa = float(parts[1].strip())

                        if current_gwa > highest_gwa:
                            highest_gwa = current_gwa
                            highest_student = student_name

            if highest_student:
               print("--- Top Performing Student ---")
               print(f"Name: {highest_student}")
               print(f"GWA: {highest_gwa}")
            else:
               print("No valid student records found.")

        except FileNotFoundError:
        print(f"Error: {self.source_file} not found.")
        except ValueError:
        print("Error: Invalid data format. Ensure GWA is a number.")

