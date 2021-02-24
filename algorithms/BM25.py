import math


def inverse_document_frequency():
    return math.log(len(texts) / containing_texts)


def frequency():
    return countContainingTexts(word)/len(texts)


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
        result += inverse_document_frequency(word) * (frequency(word) * (k + 1)) \
                  / (frequency(word) + k * (1 - b + b * len(document.split(" ")))/av_len)
    return result


def bm25():
    for text in texts:
        print('score of {', text[:4], '...} is: ', score(text, inp, average_len()))


if __name__ == '__main__':
    inp = 'green apple'
    texts = ['green pineapple', 'apple apple apple', 'green apple']
    bm25()
