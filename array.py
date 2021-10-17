import array

def rotate(arr, n, d):
    for i in range(d):
        temp = arr[0]
        for j in range(n-1):
            arr[j] = arr[j + 1]
        arr[j+1] = temp

while(True):
    n = int(input("1.Rotate the array\n"))    
    print("-----------------------------\n")
    
    if(n == 1):
        n = int(input("Enter the size of the array\n"))
        d = int(input("Enter the no of rotate\n"))
        arr = array.array('i',[])
        for i in range(n):
            data = int(input("Enter the data\n"))
            arr.append(data)
        rotate(arr, n, d)
        print(arr)
    else:
        break
    print("\n-----------------------------")