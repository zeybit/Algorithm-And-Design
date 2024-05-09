def İnsertionSort(A):
    n=len(A)
    for j in range(2,n):
        key=A[j]
        i=j-1
        while i>0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
        A[i+1]=key    
        
A=[1,3,7,5,6]  
İnsertionSort(A)
print(A)        
