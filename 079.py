dataset = open("dataset.txt", "r+").read().split("\n")

trials = int(dataset[0])
A = dataset[1].split(" ")

for i in range(0, len(A)):
	A[i] = float(A[i])
	A[i] = str(A[i] * trials)
	
out = " ".join(A)

open("answer.txt", "w+").write(out)
