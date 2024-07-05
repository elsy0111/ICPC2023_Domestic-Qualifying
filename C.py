while (1):
    n = int(input())
    if n == 0: break
    a, b, j = map(int,input().split())
    for _ in range(n):
        i, j = map(int,input().split())
        #solve here!
        ans = 0
        ans += abs(j)
        if j>0:
            if (-j<=i and i<=0):
                ans += 0
            else:
                if i < 0:
                    i += abs(j)
                else:
                    i -= 0
                ans += abs(i)
        elif j<0:
            if (0<=i and i<=-j):
                ans += 0
            else:
            
                if i < 0:
                    i += 0
                else:
                    i -= abs(j)
                
                ans += abs(i)
        else:
            ans += abs(i)
        #print(i,0)
        print(ans)
    break
