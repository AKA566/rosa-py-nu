dataset = open("dataset.txt", "r+").read().split("\n")

dataset = dataset[0].split(" ")

for i in range(0, len(dataset)):
    dataset[i] = float(dataset[i])

let res = list(map(lambda a: str(2 * (1-a) * a), dataset))

out = " ".join(res)

open("answer.txt", "w+").write(out)
