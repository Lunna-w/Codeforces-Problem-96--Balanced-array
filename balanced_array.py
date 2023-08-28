t = int(input())

for i in range(t):
    n = int(input())
    
    if (n // 2) % 2 != 0:  
        print("NO")
        continue

    sum_even = []
    sum_odd = []

    for j in range(2, n + 2, 2):
        sum_even.append(j)

    for j in range(1, n - 1, 2):
        sum_odd.append(j)


    sum_odd.append(sum(sum_even) - sum(sum_odd))

    if sum(sum_even) == sum(sum_odd):
        print("YES")
        print(" ".join(map(str, sum_even + sum_odd)))
    else:
        print("NO")
