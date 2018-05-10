a = int(input("nhap so "))
u = 0
for i in range(0,a+1):
    if i == 0 or i == 1:
        u = 1
    else:
        u=u*i
print("a! = ",u)
