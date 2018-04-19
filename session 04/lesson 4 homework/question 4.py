a = [(1,2,40),(0,15,60),(10,80,0)]
c = []
for i in range(len(a)):
    b = list(a[i])
    b[-1] = 100
    c.append(b)
print(c)

