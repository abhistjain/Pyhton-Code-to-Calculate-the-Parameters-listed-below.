# Pyhton-Code-to-Calculate-the-Parameters-listed-below.
Python program that counts the frequency of each word in a given text document. Remove any punctuation marks and convert all words to lowercase before counting. Display the top 5 most frequent words along with their frequencies. Also, calculate the below parameters. 


The formulas for calculations are : 

Positive Score: This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.

Negative Score: This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score by -1 so that the score is a positive number.

 

Polarity Score: This is the score that determines if a given text is positive or negative in nature. It is calculated by using the formula: 

Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)

The range is from -1 to +1

 

Average Sentence Length = the number of words / the number of sentences
