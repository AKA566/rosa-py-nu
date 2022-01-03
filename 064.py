import math

dataset = open("dataset.txt", "r+").read().split("\n").map(r=>r.split(" ").map(r=>+r))

for i in range(0, len(dataset)):
    dataset[i] = list(map(lambda a: float(a), dataset[i].split(" ")))
    
mult = []
multreal = []

for i in range(0, len(dataset[0])):
    for j in range(0, len(dataset[1])):
        mult.append(math.floor(1000*(-dataset[1][j] + dataset[0][i])))
        multreal.append(-dataset[1][j] + dataset[0][i])
        
count = {}

for i in range(0, len(mult)):
    if mult[i] not in count:
        count[mult[i]] = 0
    count[mult[i]] += 1
    
maxkey = -1
max0 = -1

for k in count:
    if count[k] > max0:
        max0 = count[k]
        maxkey = float(k)

i0 = 100        
for i in range(0, len(mult)):
    if mult[i] == maxkey:
        i0 = i
        break
        
open("answer.txt", "w+").write(str(max0) + "\n" + str(round(multreal[i0] * 100000)/100000))
