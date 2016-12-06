ipm_summa = 0
wordlist = []
for line in open('freq.txt','r', encoding='utf-8'):
    if 'ед жен' in line:
        word = line.split('|')
        for i in word:
            if not i.startswith (' '):
                wordlist.append(i[0:(len(i)-1)])
            elif i.startswith(' ') and not i.endswith(' '):
                ipm = float(i[1:])
                ipm_summa += ipm
print(', '.join(wordlist))
print('сумма ipm:', ipm_summa)

        

                
