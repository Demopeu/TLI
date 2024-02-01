# SW Expert Ladder 1
# 사다리 타기

for i in range(1,10+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]
    for y in range(100):
        if matrix[0][y] == 1:
            x = 0
            find = set()
            dx = [0, 0, 1]
            dy = [1, -1, 0]
            answer = y
            while True:
                find.add((x,y))
                old_x = x
                old_y = y
                for k in range(3):
                    new_x = x + dx[k]
                    new_y = y + dy[k]
                    if 0<=new_x<100 and 0<=new_y<100 and (new_x,new_y) not in find and matrix[new_x][new_y] == 1:
                        x,y = new_x, new_y



# 이부분부터 마음에 안듬
                if x == 98 and matrix[x+1][y] == 2:
                    print(f'#{N} {answer}')
                    break
                if old_x == x and old_y == y:
                    break