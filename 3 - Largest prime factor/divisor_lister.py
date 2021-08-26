import math

n = input("\n\n\n\n" + ">Gimme a positive integer to factor: ")
factors = []
print("")
if n.isdigit():
    n = int(n)
    for chk in range(1, math.ceil((n+1)/2)):
        if chk == 1:
            print(str(n) + " = " + str(int(chk)) + " * " + str(int(n/chk)))
            factors.append(chk)
            factors.append(int(n/chk))
        if n % chk == 0 and n/chk >= chk and chk > 1:
            print(" "*(len(str(n))+3) + str(int(chk)) + " * " + str(int(n/chk)))
            if n/chk != chk:
                factors.append(chk)
                factors.append(int(n/chk))
            else:
                factors.append(chk)
    print("")

    if (sum(factors)) == n+1:
        if (sum(factors)) == 2:
            print("You can't factor 1 dumbass.")
        else:
            print("That's a prime.")
    else:
        print(">Here's all " + str(len(factors)) +
              " factors, my dude: \n" + str(sorted(factors, key=int)))
else:
    print(">That's not a positive integer buddy, you effed up.")
