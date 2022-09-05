# 3. Write a recursive python function to print first N odd natural numbers

def printOddN(n):
    
    if(n>0):
        printOddN(n-1)
        print(2*n-1,end=' ')

printOddN(int(input("Enter a number: ")))