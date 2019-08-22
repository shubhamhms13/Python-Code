def rotate(m):
    size = len(m)
    for x in range(int(size / 2)):
        for y in range(x, size - x - 1):
            nx = size - 1 - x
            ny = size - 1 - y
            swapVal = m[x][y]
            m[x][y] = m[ny][x]
            m[ny][x] = m[nx][ny]
            m[nx][ny] = m[y][nx]
            m[y][nx] = swapVal
        return m
