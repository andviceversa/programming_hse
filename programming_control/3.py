user_word = input('введите слово ')
while user_word != '':
    for line in open('freq.txt','r', encoding='utf-8'):
        if user_word in line:
            word = line.split('|')
            for i in word:
                if  i.startswith(' ')and i.endswith(' '):
                    print('морфология:', i)
                elif not i.endswith(' '):
                    print('ipm:', i)
            s = 1
    else:
        s = 0
    if s == 0:
        print ('слова нет в словаре')
    user_word = input('введите слово ')
