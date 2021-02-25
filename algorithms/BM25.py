import math


def inverse_document_frequency(word):
    if containing_texts(word) == 0:
        return 0
    return math.log(len(texts) / containing_texts(word))


def containing_texts(word):
    val = c_map.get(word)
    if val:
        return val
    c_map[word] = count_occurs(word, texts)/len(texts)
    return c_map[word]


def count_occurs(word, arr):
    counter = 0
    for other in arr:
        if other.lower() == word.lower():
            counter += 1
    return counter


def frequency(word, document):
    return count_occurs(word, document.split(" "))/len(document.split(" "))


def average_len():
    s = 0
    for text in texts:
        s += len(text)
    return s/len(texts)


def score(document, query, av_len):
    k = 2.0
    b = 0.75
    result = 0.0
    for word in query.split(" "):
        result += inverse_document_frequency(word) * (frequency(word, document) * (k + 1)) \
                  / (frequency(word, document) + k * (1 - b + b * len(document.split(" ")))/av_len)
    return result


def bm25():
    av_len = average_len()
    for text in texts:
        print('score of {', text[:4], '...} is: ', score(text, inp, av_len))


if __name__ == '__main__':
    c_map = {}
    inp = 'Мороз и солнце Пушкин'
    texts = ['Трагедия в творчестве Тургенева', 'Заморозки в деревне в июле', 'Пушкин солнце русской литературы']
    bm25()
