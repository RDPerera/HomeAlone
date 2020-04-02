
while(True):
    arr=list(map(int,input().split()))
    arr=[0]+arr+[0]
    stateArr=arr[:]
    arr2=arr[:]
    stateArr2=arr[:]
    x=arr[:]
    arr3=arr[:]
    for i in range(len(arr3)-1):
        if arr3[i]>arr3[i+1]:
            arr3[i+1]=0
        else:
            arr3[i]=0
    ans2=sum(arr3)

    def getMaxIdx(x):
        #print("MAX int =",x)
        maximum=x[0]
        index=0
        for i in range(len(x)):
            if maximum < x[i]:
                maximum=x[i]
                index=i
        #print("MAX index =",index,"MAX val=",arr[index])
        return index


    def notAdjEle(x):
        for i in range(len(x)):
            if x[i]!=0:
                if x[i-1]==0 and x[i+1]==0:
                    continue
                else:
                    return False
        return True

    while(True):
        if notAdjEle(arr):
            break
        index=getMaxIdx(stateArr)
        if arr[index+1]+arr[index-1]<arr[index]:
            if index>0 and index<len(arr):
                arr[index-1]=0
                arr[index+1]=0
                stateArr[index-1]=stateArr[index+1]=stateArr[index]=0
                
        else:
            if index>0 and index<len(arr):
                arr[index]=0
                stateArr[index]=0
        #print(arr)
        #print(stateArr)
        #print("")
        
    while(True):
        if notAdjEle(arr2):
            break
        index=getMaxIdx(stateArr2)
        if index>0 and index<len(arr2):
            arr2[index-1]=0
            arr2[index+1]=0
            stateArr2[index-1]=stateArr2[index+1]=stateArr2[index]=0
        #print(arr[index],arr)

    tot1,tot2=0,0
    for i in range(len(x)):
        if(i%2):
            tot1+=x[i]
        else:
            tot2+=x[i]

    print(max(tot1,tot2,sum(arr),sum(arr2),ans2))    
      
