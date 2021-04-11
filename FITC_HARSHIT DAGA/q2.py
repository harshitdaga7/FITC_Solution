for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=sum(a)
    c=0
    #checkinhg for 0 in array
    for t in a: 
        if not t:
            c+=1
    if k < 100:
        print('NO')
    elif k == 100:
        print('YES')
    else:
        diff = (k - 100)/(n-c)
        if diff >= 1:
            print('NO')
        else:
            print('YES')