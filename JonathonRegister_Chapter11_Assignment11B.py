import math


def calculate_hypotenuse(angle_degrees, adjacent_side):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)

    # Calculate the length of the hypotenuse using trigonometry (cosine function)
    hypotenuse = adjacent_side / math.cos(angle_radians)

    return hypotenuse


def main():
    # Input from the user
    try:
        angle_degrees = float(input("Enter the nearest angle in degrees (0 < angle < 90): "))
        adjacent_side = float(input("Enter the length of the adjacent side: "))

        # Validate angle input (0 < angle < 90) for a right triangle
        if angle_degrees <= 0 or angle_degrees >= 90:
            print("Error: Angle must be between 0 and 90 degrees (exclusive).")
            return

        # Calculate the hypotenuse
        hypotenuse = calculate_hypotenuse(angle_degrees, adjacent_side)

        # Print the result
        print(f"The length of the hypotenuse is: {hypotenuse}")

    except ValueError:
        print("Error: Invalid input. Please enter valid numerical values.")


if __name__ == "__main__":
    main()
