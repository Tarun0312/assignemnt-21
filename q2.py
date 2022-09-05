# 2. Write a recursive python function to print first N natural numbers in reverse order

def printNReverse(n):
    
    if(n>0):
        print(n,end=' ')
        printNReverse(n-1)

printNReverse(int(input("Enter a number: ")))