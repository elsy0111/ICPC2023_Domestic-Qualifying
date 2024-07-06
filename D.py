while (1):
    n = int(input())
    if n == 0: break
    X, Y, d  = map(int,input().split())
    Cx = {}
    Cy = {}
    for _ in range(n):
        x, y = map(int,input().split())
        if (y in Cy):
            Cy[y].append(x)
        else:
            Cy[y] = [x]
        if (x in Cx):
            Cx[x].append(y)
        else:
            Cx[x] = [y]
    for x in Cx:
        Cx[x].sort()
    for y in Cy:
        Cy[y].sort()
    # 0 : 右
    # 1 : 上
    # 2 : 左
    # 3 : 下
    x = X
    y = Y
    direc = 0
    Atk = {}
    while(d > 0):
        if (direc == 0):
            # 障害物が自分の直線状にある
            if (y in Cy):
                IDX = -1 # -1 ならば右端
                for i in range(len(Cy[y])):
                    if x > Cy[y][i]:
                        None
                    else:
                        # あたるときのIDX
                        IDX = i
                        break
                # 通り抜けるので終了!!!
                if IDX == -1:
                    x = x + d
                    break
                else:
                    idou = min(d, (Cy[y][IDX] - 1) - x)
                    d -= idou
                    x = x + idou
                    if (x == Cy[y][IDX] - 1):
                        if ((x, y, direc) in Atk):
                            d = d % (Atk[(x, y, direc)] - d)
                        else:
                            Atk[(x, y, direc)] = d
                    direc = 1
            # 通り抜けるので終了!!!
            else:
                x = x + d
                break
        elif (direc == 1):
            # 障害物が自分の直線状にある
            if (x in Cx):
                IDX = -1 # -1 ならば一番上
                for i in range(len(Cx[x])):
                    if y > Cx[x][i]:
                        None
                    else:
                        # あたるときのIDX
                        IDX = i
                        break
                # 通り抜けるので終了!!!
                if IDX == -1:
                    y = y + d
                    break
                else:
                    idou = min(d, (Cx[x][IDX] - 1) - y)
                    d -= idou
                    y = y + idou
                    if (y == (Cx[x][IDX] - 1)):
                        if ((x, y, direc) in Atk):
                            d = d % (Atk[(x, y, direc)] - d)
                        else:
                            Atk[(x, y, direc)] = d
                    direc = 2
            # 通り抜けるので終了!!!
            else:
                y = y + d
                break
        elif (direc == 2):
            # 障害物が自分の直線状にある
            if (y in Cy):
                IDX = len(Cy[y]) # |Cy[y]| ならば左端
                for i_ in range(len(Cy[y])):
                    i = len(Cy[y]) - 1 - i_
                    if x < Cy[y][i]:
                        None
                    else:
                        # あたるときのIDX
                        IDX = i
                        break
                # 通り抜けるので終了!!!
                if IDX == len(Cy[y]):
                    x = x - d
                    break
                else:
                    idou = min(d, x - (Cy[y][IDX] + 1))
                    d -= idou
                    x = x - idou
                    if (x == (Cy[y][IDX] + 1)):
                        if ((x, y, direc) in Atk):
                            d = d % (Atk[(x, y, direc)] - d)
                        else:
                            Atk[(x, y, direc)] = d
                    direc = 3
            # 通り抜けるので終了!!!
            else:
                x = x - d
                break
        elif (direc == 3):
            # 障害物が自分の直線状にある
            if (x in Cx):
                IDX = len(Cx[x]) # -1 ならば一番下
                for i_ in range(len(Cx[x])):
                    i = len(Cx[x]) - 1 - i_
                    if y < Cx[x][i]:
                        None
                    else:
                        # あたるときのIDX
                        IDX = i
                        break
                # 通り抜けるので終了!!!
                if IDX == len(Cx[x]):
                    y = y - d
                    break
                else:
                    idou = min(d, y - (Cx[x][IDX] + 1))
                    d -= idou
                    y = y - idou
                    if (y == (Cx[x][IDX] + 1)):
                        if ((x, y, direc) in Atk):
                            d = d % (Atk[(x, y, direc)] - d)
                        else:
                            Atk[(x, y, direc)] = d
                    direc = 0
            # 通り抜けるので終了!!!
            else:
                y = y - d
                break
    print(x, y)
