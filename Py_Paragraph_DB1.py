#Import Dependencies

import os
import csv
import re

#Find and Read File

file_name = os.path.join("raw_data", "paragraph_2.txt")
#print(os.path.exists(file_name))

#Open file as file object
with open (file_name, newline ="") as file_object:
    contents = file_object.read()

#remove new line breaks within the text file

cleaned_contents = contents.replace('\n', ' ')
#print(cleaned_contents)

#Split on spaces to determine individual words

words = cleaned_contents.split()

#Find the the number of words within the text document

number_words = len(words)
#print(number_words)

#Separate sentences on punctuation and find number of sentences

sentences = re.split("(?<=[.!?]) +", cleaned_contents)
number_sentences = len(sentences)
#print(number_sentences)

#Find total number of characters within text document

total_characters = 0
for words in words:
    total_characters += len(words)
#print(total_characters)

#Divide total characters by number of words to find average letter count per word

avg_letter_count = total_characters/number_words
#print(avg_letter_count)

#Divide number words by number of sentences to word count per sentence 

avg_sentence_count = number_words/number_sentences
#print(avg_sentence_count)

#Print results to terminal

print("In this document there are approximately "+ str(number_words)+ " words.")
print("In this document there are approximately "+ str(number_sentences)+ " sentences.")
print("In this document the average letter count per word is "+ str(avg_letter_count)+ " letters.")
print("In this document the average sentence contains approximately "+ str(avg_sentence_count)+ " words.")
