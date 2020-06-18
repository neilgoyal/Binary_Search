from datetime import datetime
startTime = datetime.now()

#initialize list
def binary_search(mylist, inputVal, high, low):
    if high >= low:
        mid = (high+low)//2
        if mylist[mid] == inputVal:
            return mid
        elif mylist[mid]> inputVal:
            return binary_search(mylist, inputVal, mid-1, low)
        elif mylist[mid]< inputVal:
            return binary_search(mylist, inputVal, high, mid+1)
    else:
        return -1

mylist = list(map(int, input("Enter list(will be converted into ascending order)").split()))
mylist.sort()
inputVal = int(input("Enter value to be found"))

result = binary_search(mylist, inputVal, mylist[-1], mylist[0]) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 
    



print(datetime.now() - startTime)
