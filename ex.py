import os
direct = 'D:\Downloads\news.zip\news'
files = os.listdir(direct)
for file in files:
    f = open(file, 'r')
    sent = 0
    for line in f:
        if '. ' in line:
            sent += 1
    f.close()
    f = open('sent.txt', 'a')
    f.write(file, '    ', sent, '\n')
    f.close()
    
