import copy as c
import time

goal=[[1,3,4],[8,6,2],[7,0,5]]
start=[[5,6,7],[4,0,8],[3,2,1]]

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def valid(i,j): # Check if the upcoming step is valid
    if i<0 or i>2 or j<0 or j>2:
        return False
    return True

def getZero(grid): # Obtaining the coordinates (x, y) for the empty location
    i=0
    j=0
    for row in grid:
       j=0
       for element in row:
           if element==0:
               return[i,j]
           j+=1
       i+=1   
        
def do_operation(x,y,tox,toy,state): # Swap two squares
    state[x][y],state[tox][toy]=state[tox][toy],state[x][y]
    return state

q=[]
q.append(1)
getting_state_by_id={1 : start}

tgoal=tuple(tuple(row) for row in goal)
tstart=tuple(tuple(row) for row in start)

cost={}
cost[1]=0
parent={}
parent[1]=1
getting_id_by_state={}
getting_id_by_state[tstart]=1
id=2

while(len(q)>=1):
    curr=q[0]
    q.pop(0)

    if list(list(row) for row in getting_state_by_id[curr])==goal:
        print(cost[curr])
        break
    x,y=getZero(getting_state_by_id[curr])
    for i in range(4):
        tox=x+dx[i]
        toy=y+dy[i]
        if(valid(tox,toy)):
            cpy=do_operation(x,y,tox,toy,list(list(row) for row in getting_state_by_id[curr]))
            tcpy=tuple(tuple(row) for row in cpy)
            if(tcpy not in getting_id_by_state):
                q.append(id)
                getting_state_by_id[id]=tcpy
                getting_id_by_state[tcpy]=id
                cost[id]=cost[curr]+1
                parent[id]=curr
                id+=1

ans=[]
def build(i):
    if parent[i]==i:
        ans.append(i)
        return
    ans.append(i)
    build(parent[i])

build(getting_id_by_state[tgoal])
ans.reverse()

for i in ans:
    print(getting_state_by_id[i])

