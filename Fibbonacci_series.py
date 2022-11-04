def fibbo():
    l = [0,1]
    n = int(input("\nenter number of terms: "))
    for i in range(2, n):
        a = l[i - 1] + l[i - 2]
        l.append(a)
    print("\nThe ",n,"th term of the series is == ",l[len(l)-1])
    print("\nThe series is == ",l)

    if input("\nenter Y to use again: ") in "yY":
        fibbo()
fibbo()
