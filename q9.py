# 9. Write a recursive python function to print first N multiples of a given number.

def Nmultiples(x,N):
   
    if(N>0):
        Nmultiples(x,N-1)
        print(x*N,end=' ')

Nmultiples(int(input("Enter a number: ")),int(input("Enter how many multiples: ")))