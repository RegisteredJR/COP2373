import re


def count_sentences(text):
    # Regular expression to match sentences
    # Using positive look-ahead to match sentences ending with '.', '!', or '?'
    pattern = r'(?<=[.!?])\s+'

    # Split the text into sentences based on the pattern
    sentences = re.split(pattern, text)

    # Count the number of sentences
    num_sentences = len(sentences)

    # Print each sentence and its index
    for idx, sentence in enumerate(sentences):
        print(f"Sentence {idx + 1}: {sentence}")

    # Print the total count of sentences
    print(f"\nTotal number of sentences: {num_sentences}")


def main():
    # Prompt the user to input text
    print("Enter text containing multiple sentences:")
    text = input()

    # Call the function to count sentences
    count_sentences(text)


# call main
if __name__ == "__main__":
    main()
