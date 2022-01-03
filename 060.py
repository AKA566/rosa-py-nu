import math

dataset = open("dataset.txt", "r+").read().split("\n")
ds = ""

for i in range(0, len(dataset)):
    if dataset[i][0:1] == ">" :
        if len(ds) > 0:
            ds += "\n"
    else:
        ds += dataset[i]

s = ds.split("\n")[0]

p = {}
p[0] = 0

for i in range(1, len(s) + 1):
    len0 = 0
    s1 = s[0:i]
    
    for j in range(i-1, 0, -1):
        pr = s1[0: i -j]
        su = s1[j:i]
        
        if len(pr) > p[i-2] + 1:
            break
            
        if pr == su and len0 < len(su):
            len0 = len(su)
            
    p[i-1] = len0
    
for i in range(0, len(p)):
    p[i] = str(p[i])
    
open("answer.txt", "w+").write(" ".join(p))
