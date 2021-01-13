import codecs
import collections
# https://pythonworld.ru/moduli/modul-collections.html

num_words = 0

document_text = codecs.open("1984.txt", "r", "utf_8_sig")
text_string = document_text.read().lower()
text = text_string.split()
num_words += len(text)

dict_words = collections.Counter()
for i in text:
    dict_words[i] += 1
print(num_words)
print(dict_words.most_common(10))

# for words in dict_words.keys():
#    print(words, dict_words[words])


