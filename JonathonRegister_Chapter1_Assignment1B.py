# imports random module
import random


def main():
    # creates the list of strings for the answers
    reply_strings = ['Yes, of course!', 'Without a doubt, Yes!', 'You can count on it.', 'For sure!', 'Ask me later.',
                     'I am not sure', 'I can not tell you right now', 'I will tell you after my nap', 'No way!',
                     'I do not think so', 'Without a doubt, no.', 'The answer is clearly NO!']

    # creates the text file
    f = open('8_ball_responses.txt', 'w')

    # for loop to add the reply_strings list to the text file
    for line in f:

        reply_strings.append(line)

    # takes user's first yes/no question
    user_input = input("Enter your yes/no question: ")

    # creates while loop to keep playing the 8-ball game
    while user_input == 'yes' or 'no':

        # takes a random num between 1 and 12
        index = random.randint(0, 11)

        # prints out the random line based on index variable
        print(reply_strings[index])

        # continues to ask user to input questions until user wants to be done
        user_input = input("Enter your yes/no question: (Press ENTER key to be done.)")

        # ends the while loop if the user inputs ENTER key
        if user_input == "":
            print()
            print("Thanks for playing!")
            break


# calls main
main()
