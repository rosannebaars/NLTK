# ------- CH 1. LANGUAGE PROCESSING AND PYTHON

# -- SETUP
# Import nltk
import nltk
# Download sample texts
from nltk.book import *

# -- 1. Try using the Python interpreter as a calculator, and typing expressions like 12 / (4 + 1)
12 / (4 + 1)

# -- 2. Given an alphabet of 26 letters, there are 26 to the power 10, or 26 ** 10, ten-letter strings we can form. That works out to 141167095653376. How many hundred-letter strings are possible?
26**100

# -- 3. The Python multiplication operation can be applied to lists. What happens when you type ['Monty', 'Python'] * 20, or 3 * sent1?
# This returns a list with 20 times the words Monthy and Python, and a list with 3 times the words in sent1

# -- 4. Review 1 on computing with language. How many words are there in text2? How many distinct words are there?
len(text2)
len(set(text2))

# -- 5. Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?
# Lexical diversity can be caulated in Python using len(set(text)) / len(text) .
# Thus, humor with a lexical diversity of 0.231 is more lexically diverse than romance fiction with a lexical diversity of 0.121.
# This means that humor has more unique words as in comparison to the total than romance fiction has.

# -- 6. Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?
text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])

# -- 7. Find the collocations in text5.
text5.collocations()

# -- 8. Consider the following Python expression: len(set(text4)). State the purpose of this expression. Describe the two steps involved in performing this computation.
# This calculates the number of unique words in text4. The set function gives the unique words, the len function gives the number of words

# -- 9. Review 2 on lists and strings.
# -- a. Define a string and assign it to a variable, e.g., my_string = 'My String' (but put something more interesting in the string). Print the contents of this variable in two ways, first by simply typing the variable name and pressing enter, then by using the print statement.
hello = 'Hello'
hello
print(hello)

# -- b. Try adding the string to itself using my_string + my_string, or multiplying it by a number, e.g., my_string * 3. Notice that the strings are joined together without any spaces. How could you fix this?
hello2 = hello + hello
hello3 = hello * 3
hello_fixed = hello + ' ' + hello

# -- 10. Define a variable my_sent to be a list of words, using the syntax my_sent = ["My", "sent"] (but with your own words, or a favorite saying).
# -- a. Use ' '.join(my_sent) to convert this into a string.
word_list = ["This", "is", "a", "wordlist"] 
string_conversion = ' '.join(word_list)
# -- b. Use split() to split the string back into the list form you had to start with.
word_list = string_conversion.split()

# -- 11. Define several variables containing lists of words, e.g., phrase1, phrase2, and so on. Join them together in various combinations (using the plus operator) to form whole sentences. What is the relationship between len(phrase1 + phrase2) and len(phrase1) + len(phrase2)?
phrase1 = "This is a phrase"
phrase2 = "about Python and word lists"
phrase3 = phrase1 + phrase2
len(phrase1 + phrase2) == len(phrase1) + len(phrase2) # They have the same length

# -- 12. Consider the following two expressions, which have the same value. Which one will typically be more relevant in NLP? Why?
# -- "Monty Python"[6:12]
# -- ["Monty", "Python"][1]
# The second, because NLP is mainly concerned with words, not the individual characters, thus it is easier to split a text in list of words

# -- 13. We have seen how to represent a sentence as a list of words, where each word is a sequence of characters. What does sent1[2][2] do? Why? Experiment with other index values.
sent1[2][2]
# It prints the third character of the third word

# -- 14. The first sentence of text3 is provided to you in the variable sent3. The index of 'the' in sent3 is 1, because sent3[1] gives us 'the'. What are the indexes of the two other occurrences of this word in sent3?
sent3.index('the', 2)
sent3.index('the', 6)

# -- 15.  Review the discussion of conditionals in 4. Find all words in the Chat Corpus (text5) starting with the letter b. Show them in alphabetical order.
sorted(set(([w for w in text4 if w.startswith('b')])))

# -- 16. Type the expression list(range(10)) at the interpreter prompt. Now try list(range(10, 20)), list(range(10, 20, 2)), and list(range(20, 10, -2)). We will see a variety of uses for this built-in function in later chapters.
list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(10, 20)) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
list(range(10, 20, 2)) # [10, 12, 14, 16, 18]
list(range(20, 10, -2)) # [20, 18, 16, 14, 12]

# -- 17.  Use text9.index() to find the index of the word sunset. You'll need to insert this word as an argument between the parentheses. By a process of trial and error, find the slice for the complete sentence that contains this word.
text9.index('sunset')
text9[621:644]

# -- 18. Using list addition, and the set and sorted operations, compute the vocabulary of the sentences sent1 ... sent8.
sorted(set(sent1 + sent2 + sent3 + sent4 + sent5 + sent6 + sent7 + sent8))

# -- 19.What is the difference between the following two lines? Which one will give a larger value? Will this be the case for other texts?
sorted(set(w.lower() for w in text1)) # This returns the set of unique words that are lowercase in the text
sorted(w.lower() for w in set(text1)) # This returns the set of unique words in the text, transformed it to lowercase

# -- 20. What is the difference between the following two tests: w.isupper() and not w.islower()?
# w.isupper() checks whether all characters in w are uppercase
# w.islower() checks whether all characters in w are lowercase

# -- 21. Write the slice expression that extracts the last two words of text2.
text2[-2:]

# -- 22. Find all the four-letter words in the Chat Corpus (text5). With the help of a frequency distribution (FreqDist), show these words in decreasing order of frequency.

# -- 23. Review the discussion of looping with conditions in 4. Use a combination of for and if statements to loop over the words of the movie script for Monty Python and the Holy Grail (text6) and print all the uppercase words, one per line.

# -- 24. Write expressions for finding all words in text6 that meet the conditions listed below. The result should be in the form of a list of words: ['word1', 'word2', ...].
# -- a. Ending in ize
# -- b. Containing the letter z
# -- c. Containing the sequence of letters pt
# -- d. Having all lowercase letters except for an initial capital (i.e., titlecase)

# -- 25. Define sent to be the list of words ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']. Now write code to perform the following tasks:
# -- a. Print all words beginning with sh
word_list = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
[w for w in word_list if w.startswith('sh')]
# -- b. Print all words longer than four characters
[w for w in word_list if len(w) > 4]

# -- 26. What does the following Python code do?  sum(len(w) for w in text1) Can you use it to work out the average word length of a text?
# It returns the sum of the length of all words in text1
# The following formula calculates the average word length:
def average_word_length(text):
    return sum(len(w) for w in text)/len(text)
# The average word length is 3.83 for text 1:
average_word_length(text1)

# -- 27. Define a function called vocab_size(text) that has a single parameter for the text, and which returns the vocabulary size of the text.
def vocab_size(text):
    return len(set(text))

# -- 28. Define a function percent(word, text) that calculates how often a given word occurs in a text, and expresses the result as a percentage.
def percent(word, text):
    return text.count(word)/len(text)

# -- 29. We have been using sets to store vocabularies. Try the following Python expression: set(sent3) < set(text1). Experiment with this using different arguments to set(). What does it do? Can you think of a practical application for this?
# It returns true if text1 contains all words in sent3 and at least one additional word.
# A practical application example could be to extract social media posts that contain at least the words of a given query