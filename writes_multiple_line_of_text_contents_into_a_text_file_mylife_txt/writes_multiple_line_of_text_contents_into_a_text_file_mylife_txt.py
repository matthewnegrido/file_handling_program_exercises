class LifeRecorder:
    def __init__(self, file_name="mylife.txt"):
        self.file_name = file_name

    def write_multiple_lines(self):
        with open(self.file_name, 'w') as file_writer:
            while True:
                user_line = input("Enter line: ")

                file_writer.write(user_line + "\n")

                more_lines = input("Are there more lines y/n? ").lower()

                if more_lines != 'y':
                    break

        print(f"\nYour lines have been saved to {self.file_name}")

if __name__ == "__main__":
    recorder_instance = LifeRecorder()
    recorder_instance.write_multiple_lines()