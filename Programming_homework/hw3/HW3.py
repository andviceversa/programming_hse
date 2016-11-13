A = [0] * 7
for i in range(6):
    A[i] = int(input("print number"))
for i in range(6):
    B = ["X"] * A[i]
    if A[i] < 0:
        print ("введено отрицательное число")
    else:
        print (''.join([str(i) for i in B]))
