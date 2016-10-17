a = input ("введите a")
b = input ("введите b")
c = input ("введите c")
a = int (a)
b = int (b)
c = int (c)
if c == a % b:
    print ("a даёт остаток c при делении на b")
else:
    print ("a НЕ даёт остаток c при делении на b")
if c == a/b:
    print ("a разделить на b равно c")
else:
    print ("a разделить на b НЕ равно c")
