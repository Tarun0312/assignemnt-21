# 5. Write a recursive python function to print first N even natural numbers.

def printEvenN(n):

    if(n>0):
        printEvenN(n-1)
        print(2*n,end=' ')


printEvenN(int(input("Enter a number: ")))

