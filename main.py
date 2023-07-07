'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import string

# Function to count word frequency
def count_word_frequency(text):
    # Remove punctuation marks
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Convert text to lowercase
    text = text.lower()

    # Split text into words
    words = text.split()

    # Count word frequency
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency

# Function to calculate positive score
def calculate_positive_score(word_frequency, positive_words):
    positive_score = 0
    for word in word_frequency:
        if word in positive_words:
            positive_score += word_frequency[word]
    return positive_score

# Function to calculate negative score
def calculate_negative_score(word_frequency, negative_words):
    negative_score = 0
    for word in word_frequency:
        if word in negative_words:
            negative_score += word_frequency[word]
    return negative_score

# Function to calculate polarity score
def calculate_polarity_score(positive_score, negative_score):
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    return polarity_score

# Function to calculate average sentence length
def calculate_average_sentence_length(text):
    sentences = text.split('.')
    num_sentences = len(sentences)

    words = text.split()
    num_words = len(words)

    average_sentence_length = num_words / num_sentences
    return average_sentence_length

# Load positive and negative dictionaries
positive_words = set()
with open('positive-words.txt', 'r') as file:
    for line in file:
        positive_words.add(line.strip())

negative_words = set()
with open('negative-words.txt', 'r') as file:
    for line in file:
        negative_words.add(line.strip())

# Load text document
with open('paragraph.txt', 'r') as file:
    text = file.read()

# Count word frequency
word_frequency = count_word_frequency(text)

# Calculate positive score
positive_score = calculate_positive_score(word_frequency, positive_words)

# Calculate negative score
negative_score = calculate_negative_score(word_frequency, negative_words)

# Calculate polarity score
polarity_score = calculate_polarity_score(positive_score, negative_score)

# Calculate average sentence length
average_sentence_length = calculate_average_sentence_length(text)

# Display top 5 most frequent words
sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 most frequent words:")
for word, frequency in sorted_words:
    print(f"{word}: {frequency}")

# Display calculated parameters
print("Positive Score:", positive_score)
print("Negative Score:", negative_score)
print("Polarity Score:", polarity_score)
print("Average Sentence Length:", average_sentence_length)
