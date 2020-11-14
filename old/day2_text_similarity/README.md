# Text Similarity
This class uses spacy to compare the similarity between two strings. The 
class includes some methods to normalize the data before comparing.

## Setup
```angular2
    pip install -R requirements.txt
    python -m spacy download en_core_web_lg
```

## Example Usage
```angular2
text_1 = 'This is a test for dennis!'
text_2 = 'Denis is taking a test@'
test = TextSimilarity(text_1, text_2)

test.remove_stop_words()

test.remove_punctuation()

test.lowercase()

print(test.text_similarity()) --> 0.8062329170420258

```