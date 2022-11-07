#Define a function fibbo
def fibbo():
    #Initialisation of the series
    l = [0,1]
    
    #Take input for number of terms in the series
    n = int(input("\nenter number of terms: "))
    
    #Since the series already contains the first two elements
    #We want the 'for loop' to run (n-2) times
    for i in range(2, n):
        #Add the values of two preceding elements
        a = l[i - 1] + l[i - 2]
        #Append it in the series
        l.append(a)
    #Print the series and the nth term of the series
    print("\nThe ",n,"th term of the series is == ",l[len(l)-1])
    print("\nThe series is == ",l)

    #Recursion
    if input("\nenter Y to use again: ") in "yY":
        fibbo()
fibbo()
