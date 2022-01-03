# Finding a Shared Spliced Motif
# rosalind.info/problems/lcsq/

dataset = open("dataset.txt", "r+").read().split("\n")
ds = ""

for i in range(0, len(dataset)):
    if dataset[i][0:1] == ">" :
        if len(ds) > 0:
            ds += "\n"
    else:
        ds += dataset[i]

dataset = ds.split("\n")

d = {}

s1 = dataset[0]
s2 = dataset[1]

for i in range(0, len(s1) + 1):
    d[i] = {}
    d[i][0] = i
    
for i in range(0, len(s2) + 1):
    d[0][j] = j
    
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        aijmi = 0
        
        if i in d and j-1 in d[i]:
            aijmi = d[i][j-1]
            
        aim1j = 0
        
        if i-1 in d and j in d[i-1]:
            aim1j = d[i-1][j]
            
        aim1jm1 = 0
        
        if i-1 in d and j-1 in d[i-1]:
            aim1jm1 = d[i-1][j-1]
            
        plo = 0
        
        if s1[i] == s2[j]:
            plo = 1
            
        d[i][j] = min(aijm1 + 1, aim1j + 1, aim1jm1 + plo)

open("answer.txt", "w+").write(str(d[i][j]))
