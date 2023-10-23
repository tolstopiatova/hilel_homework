text = 'Python is good language to learn and in same time we like to tell that it is cool expereance for us'
letter_count = {}

for char in text:

    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1

print(letter_count)