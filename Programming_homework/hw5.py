words = 0
cap_words = 0
for line in open('text.txt','r', encoding='utf-8'):
        word = line.split(' ')
        for word in open('text.txt','r', encoding='utf-8'):
            words +=1
            if word.istitle():
                cap_words += 1
s = (cap_words/words)*100
print ("слов, начинающихся с заглавной буквы", s, "%")
