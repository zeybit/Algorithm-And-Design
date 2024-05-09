
def MergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[mid:]
        right=arr[:mid]
        MergeSort(left)
        MergeSort(right)
        
        i,j,k=0,0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else :
                arr[k]=right[j]
                j+=1
            k+=1    
        
        while i<len(left):
                arr[k]=left[i]
                i+=1
                k+=1
        while j<len(right):
                arr[k]=right[j]
                j+=1 
                k+=1

if __name__ == "__main__":
    my_list = [38, 27, 43, 3, 9, 82, 10]
    MergeSort(my_list)
    print("Sorted array:", my_list)
            
            
            
            
            
            
            
            
            
            
            
