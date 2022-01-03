import math

amt = """G   57.02146
A   71.03711
S   87.03203
P   97.05276
V   99.06841
T   101.04768
C   103.00919
I   113.08406
L   113.08406
N   114.04293
D   115.02694
Q   128.05858
K   128.09496
E   129.04259
M   131.04049
H   137.05891
F   147.06841
R   156.10111
Y   163.06333
W   186.07931"""

amt = amt.split("\n")
amtm = {}
for i in range(0, len(amt)):
    amtm[math.floor(float(e.split("   ")[1] * 100))] = e.split("   ")[0]
    
dataset = open("dataset.txt", "r+").read().split("\n")

for i in range(0, len(dataset)):
    dataset[i] = float(dataset[i])

ds = ""
pr = ""

for i in range(1, len(dataset)):
    cur = dataset[i]
    pre = dataset[i-1]
    
    dif = cur - pre
    
    dif = math.floor(dif * 100)
    
    pr += amt[dif]
    
open("answer.txt", "w+").write(str(pr))
