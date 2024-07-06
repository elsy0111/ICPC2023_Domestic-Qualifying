while (1):
    n = int(input())
    if (n == 0): break
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AA = 0
    BB = 0
    cnt = 0
    whowon = -1 # 0 : A 2 : B
    for i in range(n):
        AA += A[i]
        BB += B[i]
        if (i > 0):
            if (whowon == 0 and BB > AA) or (whowon == 1 and AA > BB):
                cnt += 1
        if (AA > BB) : whowon = 0
        elif (BB > AA): whowon = 1
        # print(AA, BB, cnt)
    print(cnt)

