import pandas as pd
import numpy as np

# Load the CSV file into a pandas DataFrame
# BEFORE RUNNING CODE, replace the file path with where you store the grades.csv file on your storage system
df = pd.read_csv('D:/School/ProgConcepts2/Assignments/COP2373/grades.csv')

# Print the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Separate numeric columns
numeric_df = df.select_dtypes(include=[np.number])

# Convert the numeric DataFrame to a numpy array
data = numeric_df.to_numpy()

# Calculate and print statistics for each numeric column
print("\nStatistics for each exam:")
for i, column in enumerate(numeric_df.columns):
    exam_data = data[:, i]

    # Remove NaN values for calculations
    exam_data = exam_data[~np.isnan(exam_data)]

    if len(exam_data) > 0:  # Ensure there's data to process
        mean = np.mean(exam_data)
        median = np.median(exam_data)
        std_dev = np.std(exam_data)
        minimum = np.min(exam_data)
        maximum = np.max(exam_data)

        print(f"\nExam {i + 1} ({column}):")
        print(f"Mean: {mean:.2f}")
        print(f"Median: {median:.2f}")
        print(f"Standard Deviation: {std_dev:.2f}")
        print(f"Minimum: {minimum:.2f}")
        print(f"Maximum: {maximum:.2f}")
    else:
        print(f"\nExam {i + 1} ({column}): No valid data")

# Calculate and print overall statistics for all numeric data combined
all_grades = data.flatten()

# Remove NaN values
all_grades = all_grades[~np.isnan(all_grades)]

if len(all_grades) > 0:  # Ensure there's data to process
    overall_mean = np.mean(all_grades)
    overall_median = np.median(all_grades)
    overall_std_dev = np.std(all_grades)
    overall_min = np.min(all_grades)
    overall_max = np.max(all_grades)

    print("\nOverall statistics for all exams combined:")
    print(f"Mean: {overall_mean:.2f}")
    print(f"Median: {overall_median:.2f}")
    print(f"Standard Deviation: {overall_std_dev:.2f}")
    print(f"Minimum: {overall_min:.2f}")
    print(f"Maximum: {overall_max:.2f}")
else:
    print("\nOverall statistics: No valid data")

# Determine pass/fail count for each numeric column
passing_grade = 60

print("\nPass/Fail count for each exam:")
for i, column in enumerate(numeric_df.columns):
    exam_data = data[:, i]

    # Remove NaN values
    exam_data = exam_data[~np.isnan(exam_data)]

    num_passed = np.sum(exam_data >= passing_grade)
    num_failed = len(exam_data) - num_passed

    print(f"\nExam {i + 1} ({column}):")
    print(f"Number of students who passed: {num_passed}")
    print(f"Number of students who failed: {num_failed}")

# Calculate and print overall pass percentage
overall_passed = np.sum(all_grades >= passing_grade)
total_students = len(all_grades)

if total_students > 0:
    pass_percentage = (overall_passed / total_students) * 100
    print(f"\nOverall pass percentage across all exams: {pass_percentage:.2f}%")
else:
    print("\nOverall pass percentage: No valid data")
