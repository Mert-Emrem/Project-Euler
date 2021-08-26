pals = []
for i in range(1000, 900, -1):
    for a in range(1000, 900, -1):
        num = str(a * i)
        if num == num[::-1]:
            pals.append(num)
print(max(pals))
