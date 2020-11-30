#   Matthew Lingle
#   CSCI 101 – Section B
#   Python lab 10 
#   References:TA colin  
#   Time: 30 minutes
print("Enter the length of the word you are looking for:")
L=int(input("LENGTH>"))
print("Enter the seed for the random number generator:")
S=int(input("SEED>"))
list1=[]
with open("dictionary.txt", "r") as f:
    for l in f:
        l=l.strip()
        if len(l)==L:
            list1.append(l)
print("There are", len(list1), "words in the dictionary with length", L)
print("OUTPUT", len(list1))
import random
random.seed(S)
print("Here is one random word in the dictionary with length", L)
print(f'OUTPUT "{random.choice(list1)}"')
long_words=[]
max_len=0
for w in long_words:
    if len(w)>max_len:
        max_len=len(w)
        long_words.clear()
        long_words.append(w)
    elif len(w) == max_len:
        long_words.append(w)
print("The longest word(s) is/are:", long_words)
print("OUTPUT", long_words)
print("Goodbye!")
    
    
