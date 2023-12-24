"""
Word Occurrences
Estimate: 20 minutes
Actual:
Pseudocode:
word_counts = {}
get text
for word in words
     frequency = word_counts.get(word, 0)
     word_counts[word] = frequency + 1

words = list(word_counts.keys())
words.sort()

longest_word = max((len(word) for word in words))
for word in words
    get word, longest_word, word_counts[word]
"""

word_counts = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_counts.get(word, 0)
    word_counts[word] = frequency + 1

words = list(word_counts.keys())
words.sort()

longest_word = max((len(word) for word in words))
for word in words:
    print(f'{word:{longest_word}} : {word_counts[word]}')





