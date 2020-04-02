arr=list(map(int,input().split()))
incl = 0
excl = 0
for i in arr: 
    new_excl = excl if excl>incl else incl 
    incl = excl + i 
    excl = new_excl 
print(excl if excl>incl else incl) 
