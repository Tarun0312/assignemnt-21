# 4. Write a recursive python function to print first N odd natural numbers in reverse order

def printOddNReverse(n):
    
    if(n>0):
        print(2*n-1,end=' ')
        printOddNReverse(n-1)

printOddNReverse(int(input("Enter a number: ")))
