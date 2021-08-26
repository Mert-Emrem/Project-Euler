a = 0
b = 1
evens = []
# turns out, the sequence surpasses 4 million at 32nd number, a range of 4000 is overkill
for fibonacci_number in range(4000):
    if a <= 4000000:
        c = a + b
        a = b
        b = c
        if a % 2 == 0:
            evens.append(a)

print("\n"+str(sum(evens)))
