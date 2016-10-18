n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
swaps = 0

for i in range(0, n):
    for j in range(0, n-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swaps += 1

    if swaps == 0:
        break

print("Array is sorted in %d swaps." % (swaps))
print("First Element: %d" % (a[0]))
print("Last Element: %d" % (a[n-1]))
