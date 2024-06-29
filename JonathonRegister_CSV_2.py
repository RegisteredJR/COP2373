import csv


def read_grades_from_csv():
    # Open the file in 'r' mode
    with open('grades.csv', 'r', newline='') as file:
        reader = csv.reader(file)

        # Read and print header
        header = next(reader)
        print(f"{header[0]:<15} {header[1]:<15} {header[2]:<8} {header[3]:<8} {header[4]:<8}")
        print("=" * 50)

        # Iterate through each row in the CSV file
        for row in reader:
            first_name, last_name, exam1, exam2, exam3 = row
            print(f"{first_name:<15} {last_name:<15} {exam1:<8} {exam2:<8} {exam3:<8}")


# Example usage:
if __name__ == "__main__":
    read_grades_from_csv()
