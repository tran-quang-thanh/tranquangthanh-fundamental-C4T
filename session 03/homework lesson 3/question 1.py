a=[]
for i in range(2000,3201):
    if i%7 == 0 and not i%5 == 0:
        a.append(i)
    else: continue
print(a)