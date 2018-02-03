import urllib.request
import re
import os
req = urllib.request.Request('http://web-corpora.net/Test2_2016/short_story.html')
with urllib.request.urlopen(req) as response:
   html = response.read().decode('utf-8')
words = html.replace('.',' ').replace('&', ' ').replace('-',' ').split(' ')
wordlist = []
regSymbols = re.compile('\W|[a-z]')
for word in words:
    if word.startswith('с'):
        word = regSymbols.sub('', word)
        wordlist.append(word)
        #print(word)
with open('wordlist.txt', 'w', encoding = 'utf-8') as f:
    for word in wordlist:
        f.write(word + '\n')
    f.close()
os.system("C:\mystem.exe -ndi wordlist.txt output.txt")
with open ('output.txt', 'r', encoding = 'utf-8') as t:
    marked_words = t.read().split('}')
    for i in marked_words:
        if i.find('=V') != -1:
            print(i)
