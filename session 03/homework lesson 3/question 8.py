a = input("nhap du lieu ")
import string
for i in a:
    if 97<= ord(i) <= 122:
        u = ord(i)-32
        for t in string.ascii_uppercase:
            if ord(t) == u:
                a = a.replace(i,t)
print(a)
