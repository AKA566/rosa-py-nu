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

a = []
d = []

let s1 = dataset[0]
let s2 = dataset[1]

for i in range(0, len(s1)):
    if i not in a:
        a.append({})
    if i not in d:
        d.append({})
        
    for j in range(0, len(s2)):
        aijmi = 0
        
        if i in a and j-1 in a[i]:
            aijmi = a[i][j-1]
            
        aim1j = 0
        
        if i-1 in a and j in a[i-1]:
            aim1j = a[i-1][j]
            
        aim1jm1 = 0
        
        if i-1 in a and j-1 in a[i-1]:
            aim1jm1 = a[i-1][j-1]
            
        plo = 0
        
        if s1[i] == s2[j]:
            plo = 1
            
        if not plo and aijm1 > aim1j:
            a[i][j] = aijm1
            d[i][j] = [0,-1]
        elif not plo:
            a[i][j] = aim1j
            d[i][j] = [-1,0]
        else:
			a[i][j] = aim1jm1 + plo
			d[i][j] = [-1,-1]
            
ti = len(s1) - 1
tj = len(s2) - 1

res = ""

while ti >= 0 and tj >= 0

    nti = d[ti][tj][0]
    ntj = d[ti][tj][1]
    
    if nti == -1 and ntj == -1:
        res = s1[ti] + res
        
    ti += nti
    tj += ntj
    
open("answer.txt", "w+").write(res)
