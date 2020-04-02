arr=[0]+list(map(int,input().split()))+[0]
sArr=arr[:]
def getMinIdx(x):
    maxi=x[0];
    ind=0
    for i in range(len(x)):
        if maxi < x[i]:
            maxi=x[i]
            ind=i
    mini=maxi
    index=ind
    for i in range(len(x)):
        if mini > x[i] and x[i]>0:
            mini=x[i]
            index=i
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
    index=getMinIdx(sArr)
    #print(arr)
    if arr[index-1]!=0 or arr[index+1]!=0:
        arr[index]=0
    sArr[index]=0;
print(sum(arr))
