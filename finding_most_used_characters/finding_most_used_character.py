from collections import Counter

sentence = "This is a common interview question"

most_used = Counter(sentence) 
most_used = max(most_used, key = most_used.get) 
print(most_used)

#Line 5 counts all the individual characters in the string ready to
#find the max. In the max function we call the variable we want to 
#find the max of and we get the keyname of the item you want to return
#the value largest value from, in this case, the character that's
#used the most.

sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1 
        
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

print(char_frequency_sorted[0])

#This is Mosh's version, it uses an algorithm to check to see if 
#each character has been added to the empty list and if so it will
#add the character and a counter to it