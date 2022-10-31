"""
CP1404 Practical
Word occurances
Count occurances of words in a string
Estimate: 20 minutes
Actual: 25 minutes

Sorts output alphabetically
"""
word_to_occurance = {}
words = input("Text: ").lower().split(' ')
for word in words:
    if word in word_to_occurance:
        word_to_occurance[word] += 1
    else:
        word_to_occurance[word] = 1

max_word_length = max(len(word) for word in word_to_occurance.keys())
max_occurance_length = max(len(str(number)) for number in word_to_occurance.values())

word_to_occurance = dict(sorted(word_to_occurance.items()))

for pair in word_to_occurance.items():
    print(f"{pair[0]:{max_word_length}} : {pair[1]:{max_occurance_length}}")