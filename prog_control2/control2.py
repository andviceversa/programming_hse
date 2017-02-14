def linecount (text):
    lines = 0
    for line in text:
        lines += 1
    return lines
def freq (text):
    A = dict()
    for line in text:
        if "<w lemma=" in line:
            if line not in A:
                A[line] = 1
            else:
                A[line] += 1
    return A
islandic = open('islandic.xml')
B = freq (islandic)
my_file = open("res.txt", "w")
my_file.write(str(linecount (islandic)))
for key in B:
    my_file.write(key)
my_file.close()
