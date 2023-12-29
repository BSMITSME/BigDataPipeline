# from collections import deque

# N, M = map(int, input().split())
# arrmap = [list(map(int, input())) for i in range(N)] 

# visited = [[0]*M for _ in range(N)]

# def bfs(si, sj, ei, ej) : 
#     q = deque([])
#     q.append((si,sj))
#     visited[si][sj] = 1
#     while q : 
#         ci,cj = q.popleft()
        
#         # 정답 처리가 필요한 경우
#         if (ci,cj) == (ei, ej) : 
#             return visited[ei][ej]
    
#         # 상하좌우  
#         for di,dj in ((-1,0),(1,0),(0,-1),(0,1)) : 
#             ni, nj = ci+di, cj+dj
#             # 범위 내에 있다면
#             if 0<=ni<N and 0<=nj<M and arrmap[ni][nj] == 1 and visited[ni][nj] == 0 : 
#                 q.append((ni,nj))
#                 visited[ni][nj] = visited[ci][cj] + 1

# ans = bfs(0,0,N-1,M-1)
# print(ans)

from collections import deque
def solution(maps):
    visited = [[0 for a in i] for i in maps]
    visited[0][0] += 1
    q = deque([])
    q.append((0,0))
    N, M = len(visited), len(visited[0])
        
    while q : 
        cx, cy = q.popleft()
        if (cx,cy) == (N-1, M-1) :
            return visited[cx][cy]
        # 상하좌우
        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)) : 
            nx = cx + dx
            ny = cy + dy
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                q.append((nx,ny))
                visited[nx][ny] = visited[cx][cy] + 1
                
    return -1
    
    
    
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
