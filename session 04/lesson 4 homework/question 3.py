m = input("nhap ADN ")
k = int(input("nhap k "))
n = len(m)
kmer = []
for i in range(0,n-k+1):
    kmer.append(m[i:i+k])
print(kmer)

