while (1):
    n = int(input())
    if n==0:
        break
    li = list(map(int,input().split()))
    ans = [[0 for j in range(n)] for i in range(n)]
    if li[0]==li[-1]:
        print("Yes")
        ans[0] = li[::-1]
        ans[-1] = li
        for i in range(n):
            ans[i][0] = li[i]
            ans[-1][i] = li[i]
            ans[n-i-1][-1] = li[i]
            ans[0][n-i-1] = li[i]
    else:
        if (li[0] in li[1:]) and (li[-1] in li[:-1]):
            for i in range(1,n):
                if li[0]==li[i]:
                    j0 = i
                if li[-1]==li[n-i-1]:
                    j1 = n-i-1
            # print(j0,j1,li[0],li[-1])
            if j1<j0:
                print("Yes")
                for i in range(n-j0-1):
                    ans[j1][i] = li[n-i-1]
                    ans[n-i-1][j1] = li[n-i-1]
                    ans[n-j1-1][n-i-1] = li[n-i-1]
                    ans[i][n-j1-1] = li[n-i-1]
                for i in range(j1):
                    ans[j0][i] = li[i]
                    ans[n-i-1][j0] = li[i]
                    ans[n-j0-1][n-i-1] = li[i]
                    ans[i][n-j0-1] = li[i]
                for i in range(j1,j0+1):
                    ans[i][0] = li[i]
                    ans[-1][i] = li[i]
                    ans[n-i-1][-1] = li[i]
                    ans[0][n-i-1] = li[i]
            else:
                print("No")
                continue
        else:
            print("No")
            continue
    for i in ans:
        print(*i)