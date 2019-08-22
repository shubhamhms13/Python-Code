def rotate(matrix):
    size = len(matrix)
    for x in range(int(size / 2)):
        for y in range(x, size - x - 1):
            nx = size - 1 - x
            ny = size - 1 - y
            swapVal = matrix[x][y]
            matrix[x][y] = matrix[ny][x]
            matrix[ny][x] = matrix[nx][ny]
            matrix[nx][ny] = matrix[y][nx]
            matrix[y][nx] = swapVal
        return matrix

