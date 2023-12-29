from  collections import deque
H, W, N, M = map(int,input().split())

table = [[None] * W for i in range(H)]

def bfs(a, b) : 
    de = deque([])
    de.append((a,b))
    count = 0
    while de : 
        count+=1
        ca, cb = de.popleft()
        table[ca][cb] = True
        
        for da, db in ((ca+2,cb),(ca,cb+2),(ca-2,cb),(ca,ca-2)) : 
            na = ca+da
            nb = cb+db
            if 0<=na<H and 0<=nb<W and table[na][nb] == None : 
                de.append((na,nb))
                
                
    return count

print(bfs(1,1))