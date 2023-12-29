import sys
input = sys.stdin.readline
n = int(input())

arr = []
count = 0
answer = []

def dfs(x, y) : 
  global count
  global n
  count += 1
  arr[x][y] = 0
  
  # 상하좌우
  for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)) : 
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 : 
      dfs(nx,ny)
  

for i in range(n) : 
  arr.append(list(map(int, input().split())))

for i in range(n) : 
  for j in range(n) : 
    if arr[i][j] == 1 :
      dfs(i,j)
      answer.append(count) 
      count = 0

print(len(answer))
for i in answer : 
  print(i)
    
import sys
from collections import deque


def bfs(y, x) : 
    queue = deque()
    queue.append([y,x])
    visited[y][x] = True
    count = 1
    
    while queue : 
        r, c = queue.popleft()
        for a, b in [[1,0],[0,1],[-1,0],[0,-1]] : 
            dr = r + a
            dc = c + b
            if(0<=dr<n and 0<=dc<n) and blockMap[dr][dc] ==1 and not visited[dr][dc]:             
                queue.append([dr,dc])
                visited[dr][dc] = True
                count += 1
    return count

n = int(sys.stdin.readline())

blockMap = [list(map(int, input())) for _ in range(n)]

visited = [[False]*(n) for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if blockMap[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i,j))

print(len(result))
result.sort()
for i in result: 
    print(i)
    
