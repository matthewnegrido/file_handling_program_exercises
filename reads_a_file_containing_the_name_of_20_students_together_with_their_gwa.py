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

if __name__ == "__main__":
    if not os.path.exists("students.txt"):
        with open("students.txt", "w") as file_writer:
            modern_students = [
                "Ethan Gabriel Reyes, 92.5", "Skyler Blanche Santos, 88.0",
                "Nathaniel Kyle Cruz, 95.4", "Princess Nicole Garcia, 91.2",
                "John Lloyd Bautista, 87.5", "Chloe Cassandra Mendoza, 93.8",
                "Justin Miguel Castro, 89.9", "Sofia Margarette Ramos, 96.2",
                "Zion Alexander Lim, 90.5", "Samantha Joy Dizon, 94.1",
                "Gian Carlo Villafuerte, 86.7", "Hailey Beatrix Pineda, 92.3",
                "Angelo Rafael Aquino, 97.8", "Ysabella Faith Ocampo, 89.2",
                "Xander James Soriano, 85.9", "Althea Louise Valenzuela, 94.5",
                "Renz Christian Tolentino, 88.3", "Brianna Elise Pascual, 91.7",
                "Matteo Dominic Fajardo, 93.0", "Kaitlyn Bree Hernandez, 90.8"
            ]
            file_writer.write("\n".join(modern_students))
        print("Generated 'students.txt' with 20 modern names.\n")

    analyzer_instance = GradeAnalyzer()
    analyzer_instance.find_highest_gwa()
