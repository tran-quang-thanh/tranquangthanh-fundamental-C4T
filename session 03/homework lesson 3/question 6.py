n = int(input("nhap n "))
sum = 0
for i in range(1,n+1):
    sum = sum + i/(i+1)
print(float(sum))