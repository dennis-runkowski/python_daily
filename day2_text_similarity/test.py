from main import TextSimilarity

text_1 = 'This is a test for dennis!'
text_2 = 'Denis is taking a test@'

test = TextSimilarity(text_1, text_2)

print(repr(test))

test.remove_stop_words()

print(repr(test))

test.remove_punctuation()

print(repr(test))

test.lowercase()

print(repr(test))

print(test.text_similarity())