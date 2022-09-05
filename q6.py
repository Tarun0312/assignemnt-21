# 6. Write a recursive python function to print first N even natural numbers in reverse
# order.

def printEvenNReverse(n):
    
    if(n>0):
        print(2*n,end=' ')
        printEvenNReverse(n-1)

printEvenNReverse(int(input("Enter a number: ")))        