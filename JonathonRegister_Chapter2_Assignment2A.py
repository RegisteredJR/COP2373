# imports re module
import re

# creates a list of spam keywords and phrases
spam_keywords = [
    "buy now",
    "discount",
    "free",
    "click here",
    "limited time offer",
    "urgent",
    "money back guarantee",
    "act now",
    "amazing",
    "winner",
    "prize",
    "cash",
    "credit card",
    "guarantee",
    "free gift",
    "risk-free",
    "lowest price",
    "order now",
    "no obligation",
    "special promotion",
    "congratulations",
    "extra income",
    "work from home",
    "weight loss",
    "big bucks",
    "make money",
    "opportunity",
    "instantly",
    "income",
    "cheap"
]


# defines function calc_spam_score
def calc_spam_score(message, keywords):

    # defines variable
    spam_score = 0
    spam_keywords_found = []

    # for loop to check for each keyword in the message
    for keyword in keywords:
        if re.search(r'\b{}\b'.format(re.escape(keyword)), message, re.IGNORECASE):
            spam_score += 1
            spam_keywords_found.append(keyword)

    return spam_score, spam_keywords_found


# defines main
def main():
    message = input("Enter your email message: ")

    spam_score, spam_keywords_found = calc_spam_score(message, spam_keywords)

    print("\nSpam Score: {}".format(spam_score))  # prints spam score
    print("Likelihood of spam: {}%".format(spam_score * 10))  # likelihood of spam in percentage format

    if spam_score > 0:
        print("\nSpam keywords/phrases found:")
        for keyword in spam_keywords_found:
            print("- {}".format(keyword))


# calls main
if __name__ == "__main__":
    main()
