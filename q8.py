# 8. Write a recursive python function to print cubes of first N natural numbers

def printcubeofN(n):
    if(n>0):
        printcubeofN(n-1)
        print(n**3,end=' ')

printcubeofN(int(input("Enter a number: ")))        