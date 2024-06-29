import csv


def write_grades_to_csv(num_students):
    # Open the file in 'w' mode with newline='' to avoid extra newlines in CSV
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Input loop for each student
        for _ in range(num_students):
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write the student's data to the CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print(f"Successfully wrote grades for {num_students} students to grades.csv")


# Example usage:
if __name__ == "__main__":
    num_students = int(input("Enter the number of students: "))
    write_grades_to_csv(num_students)
