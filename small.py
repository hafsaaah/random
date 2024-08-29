l=list(map(int,input().split()))
min=float('inf')
for i in l:
    if i<min:
        min=i
print(min)