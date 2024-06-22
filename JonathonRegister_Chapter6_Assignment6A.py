import re


def validate_phone_number(number):
    # Regular expression to match a phone number
    # Accepts formats like (123) 456-7890, 123-456-7890, 1234567890, etc.
    pattern = r'^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$'
    return re.match(pattern, number) is not None


def validate_ssn(ssn):
    # Regular expression to match a social security number (SSN)
    # Accepts formats like 123-45-6789 or 123456789
    pattern = r'^\d{3}-?\d{2}-?\d{4}$'
    return re.match(pattern, ssn) is not None


def validate_zip_code(zip_code):
    # Regular expression to match a zip code
    # Accepts formats like 12345 or 12345-6789
    pattern = r'^\d{5}(-\d{4})?$'
    return re.match(pattern, zip_code) is not None


def main():
    # Getting input from user in order to validate the inputs after
    phone_number = input("Enter a phone number: ")
    ssn = input("Enter a social security number (SSN): ")
    zip_code = input("Enter a zip code: ")

    # Validating each input from user
    phone_valid = validate_phone_number(phone_number)
    ssn_valid = validate_ssn(ssn)
    zip_valid = validate_zip_code(zip_code)

    # Displaying results to user
    print("\nValidation results:")
    print(f"Phone number {'is' if phone_valid else 'is not'} valid.")
    print(f"SSN {'is' if ssn_valid else 'is not'} valid.")
    print(f"Zip code {'is' if zip_valid else 'is not'} valid.")


if __name__ == "__main__":
    main()
