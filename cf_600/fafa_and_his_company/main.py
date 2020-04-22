test = int(input())

count = 0
for l in range(1, test):
    if test%l == 0:
        count += 1
print(count)
