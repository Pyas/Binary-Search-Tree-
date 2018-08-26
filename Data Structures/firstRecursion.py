def myFunction(n):
    if(n==1):
        return 1
    return n*myFunction(n-1)
print(myFunction(4))