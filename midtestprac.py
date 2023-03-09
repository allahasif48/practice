list_Of_Numbers = [21, 90, 86, 61, 55]
k = 0
for i in list_Of_Numbers:
    if i > k:
        k = i
print(k, "is greatest number")

list_Of_Numbers = [25, 30, 57, 97, 99, 100, 85]

for i in list_Of_Numbers:
    count = 0
    if i > 1:
        for k in range(2, i+1):
            if i % k == 0:
                count += 1
    if count >= 2:
        print(i, count, "is false")
    else:
        print(i, count, "is true")


