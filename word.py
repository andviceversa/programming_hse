s = 8
p = input ("введите число")
p = int (p)
while p!=s:
    if p < s:
        print ("больше")
    else:
        print ("меньше")
    p = input ("ещё раз")
    if len (p) == 0:
        print ("всё")
        break
    p = int (p)
if p==s:
    print ("вы выиграли")
    
