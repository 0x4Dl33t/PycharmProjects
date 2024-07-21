from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Sample text message
text = input("\nPlease enter a phrase or message to validate:\n")

# Tokenize the text message
tokens = word_tokenize(text.lower())

# Initialize the WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Initialize the list of grammar and spelling issues
issues = []

# Check grammar and spelling issues
for token in tokens:
    # Check if the token is a word
    if token.isalpha():
        # Check if the token is spelled correctly
        if token not in wordnet.words():
            issues.append(f"Spelling issue: '{token}'")
        # Check if the token is in plural form
        if token.endswith('s'):
            singular_form = token[:-1]
            if singular_form in wordnet.words():
                issues.append(f"Plural form issue: '{token}'")
        # Lemmatize the token
        lemmatized_token = lemmatizer.lemmatize(token)
        # Check if the lemmatized token is in plural form
        if lemmatized_token.endswith('s'):
            singular_form = lemmatized_token[:-1]
            if singular_form in wordnet.words():
                issues.append(f"Plural form issue: '{token}'")

# Check clarity and conciseness
if len(tokens) < 10:
    issues.append("Clarity issue: The text message is too short.")
if len(tokens) > 200:
    issues.append("Clarity issue: The text message is too long.")
if len(set(tokens)) < len(tokens):
    issues.append("Clarity issue: The text message contains duplicate words.")

# Check tone of the text message
if "excited" in text and "awesome" in text and "make" in text and "lives" in text:
    issues.append("Tone issue: The text message has a positive tone.")
else:
    issues.append("Tone issue: The text message has a negative tone.")

# Display the list of grammar and spelling issues
if issues:
    print("Grammar and spelling issues:")
    for issue in issues:
        print(issue)
else:
    print("The text message is free of grammar and spelling issues.")
