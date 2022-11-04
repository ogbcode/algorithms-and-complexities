def binarysearch(array,target):
    found=False
    first=0
    last=len(array)-1
    while(first<=last and found==False):
        midnumber=(first+last)//2
        if(array[midnumber]==target):
            found=True
            index=array.index(array[midnumber])
        else:
            if(target<array[midnumber]):
                last=midnumber-1
            else:
                first=midnumber+1
    return str(found) ,"the index is :"+ str(index )
test=[1,2,3,4,5,6]
print(binarysearch(test,4))