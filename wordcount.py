import jieba

data = open('comment.json', 'r', encoding='utf-8').read()
all_word = jieba.lcut(data)
count = {}

for word in all_word:
    if len(word) == 1:
        continue
    else:
        count[word] = count.get(word,0) + 1
items = list(count.items())
items.sort(key=lambda x:x[1], reverse=True)

with open('words.txt','a',encoding='utf-8') as fi:
    for i in range(70):
        word, count = items[i]
        print(u"{0:<10}{1:>5}".format(word, count))
        fi.write(word + '\n')




