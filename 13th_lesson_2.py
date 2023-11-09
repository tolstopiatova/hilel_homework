def longest_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    words = text.split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]

    return longest_words

file = "article.txt"
result = longest_words(file)
print("Слова максимальної довжини:", result)
