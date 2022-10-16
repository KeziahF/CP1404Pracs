"""
CP1404 Practical
Word occurances
Estimate: 20 minutes
Actual: 25 minutes

Sorts output alphabetically
"""

text = input("Text: ").lower().split(' ')
word_to_occurance = {}
for word in text:
    if word in word_to_occurance:
        word_to_occurance[word] += 1
    else:
        word_to_occurance[word] = 1

max_word_length = max(len(word) for word in word_to_occurance.keys())
max_occurance_length = max(len(str(number)) for number in word_to_occurance.values())
print(max_occurance_length)

word_to_occurance = dict(sorted(word_to_occurance.items()))
print(word_to_occurance)

for pair in word_to_occurance.items():
    print(f"{pair[0]:{max_word_length}} : {pair[1]:{max_occurance_length}}")
