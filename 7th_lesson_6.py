text = """Любіть Україну, як сонце, любіть,

як вітер, і трави, і води…

В годину щасливу і в радості мить,

любіть у годину негоди.

Любіть Україну у сні й наяву,

вишневу свою Україну,

красу її, вічно живу і нову,

і мову її солов’їну.

Між братніх народів, мов садом рясним,

сіяє вона над віками…

Любіть Україну всім серцем своїм

і всіми своїми ділами.

Для нас вона в світі єдина, одна

в просторів солодкому чарі…

Вона у зірках, і у вербах вона,

і в кожному серця ударі,

у квітці, в пташині, в електровогнях,

у пісні у кожній, у думі,

в дитячий усмішці, в дівочих очах

і в стягів багряному шумі…"""
text1 = text.replace(".", " ")
text2 = text1.replace(",", " ")
text3 = text2.replace("’", " ")
text4 = text3.replace("…", " ")
text5 = text4.replace("\n", " ")

print(text5)
words = text5.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
# Знайти слово, яке зустрічається найбільше разів
max_word = max(word_count, key=word_count.get)
max_count = word_count[max_word]
print(f"Слово, яке зустрічається найбільше разів: '{max_word}' ({max_count} разів)")

# Знайти слово, яке зустрічається найменше разів
min_word = min(word_count, key=word_count.get)
min_count = word_count[min_word]
print(f"Слово, яке зустрічається найменше разів: '{min_word}' ({min_count} разів)")
