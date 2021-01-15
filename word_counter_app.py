import codecs
import collections

dict_words = {}
num_words = 0
document_text = codecs.open("1984.txt", "r", "utf_8_sig")
text_string = document_text.read().lower()
text = text_string.split()
num_words += len(text)

for i in text:
    if len(i) > 3:
        if i not in dict_words:
            dict_words.setdefault(i, 0)
        if i in dict_words:
            dict_words[i] += 1


def most_coomon(dict, n=10):
    sorted_values = sorted(dict_words.values(), reverse=True)
    sorted_dict = {}
    for i in sorted_values:
        for k in dict.keys():
            if dict[k] == i:
                sorted_dict[k] = dict[k]
                break
    res = list(sorted_dict)
    return res[:n]


print(f"Words in file: {num_words}")
print(most_coomon(dict_words))








# dict_words = collections.Counter()
# for i in text:
#    if len(i) > 3:
#        dict_words[i] += 1
# print(dict_words.most_common(15))


# print({k: v for k, v in sorted(dict_words.items(), key=lambda item: item[1])})


# for w in sorted(dict_words, key=dict_words.get, reverse=False):
#    print(w, dict_words[w])
