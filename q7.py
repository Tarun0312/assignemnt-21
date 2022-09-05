# 7. Write a recursive python function to print squares of first N natural numbers


def printsquaresOfN(n):
   
    if(n>0):
        printsquaresOfN(n-1)
        print(n*n,end=' ')

printsquaresOfN(int(input("Enter a number: ")))        
