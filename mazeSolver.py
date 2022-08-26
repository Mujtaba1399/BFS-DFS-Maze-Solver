size = 12
goal = 120
start = 59
maze = [
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,1,1,1,0,1,1,1,1,1,1,0,
            0,1,0,1,0,1,1,1,1,0,1,0,
            0,0,0,1,0,1,1,1,1,0,0,0,
            0,1,1,1,1,0,0,0,1,0,1,1,
            0,0,0,0,1,0,1,0,1,0,1,0,
            0,1,1,0,1,0,1,0,1,0,1,0,
            0,0,1,0,1,0,1,0,1,0,1,0,
            0,1,1,1,1,1,1,1,1,0,1,0,
            0,0,0,0,0,0,1,0,0,0,1,0,
            1,1,1,1,1,1,1,1,1,1,1,0,
            0,0,0,0,0,0,0,0,0,0,0,0
        ]

"""
positions:

    0       1       2       3       4       5       6       7       8       9       10      11
    12      13      14      15      16      17      18      19      20      21      22      23
    24      25      26      27      28      29      30      31      32      33      34      35
    36      37      38      39      40      41      42      43      44      45      46      47
    48      49      50      51      52      53      54      55      56      57      58      59
    60      61      62      63      64      65      66      67      68      69      70      71
    72      73      74      75      76      77      78      79      80      81      82      83
    84      85      86      87      88      89      90      91      92      93      94      95
    96      97      98      99      100     101     102     103     104     105     106     107
    108     109     110     111     112     113     114     115     116     117     118     119
    120     121     122     123     124     125     126     127     128     129     130     131 
    132     133     134     135     136     137     138     139     140     141     142     143 

initial state  : root_node
sucessor state : new_node
goal test : node.position==goal
path steps : cost
searching steps : moves 
    
"""


class Node:
    def __init__(self , position , cost ):
        self.position = position
        self.cost = cost

def createNode(position , cost):
    return Node(position , cost)

def move_right(pos):
    if pos==11 or pos==23 or pos==35 or pos==47 or pos==59 or pos==71 or pos==83 or pos==95 or pos==107 or pos==119 or pos==131 or pos==143:
        return False
    elif maze[pos+1]==0:
        return False
    return pos+1 

def move_left(pos):
    if pos==0 or pos==12 or pos==24 or pos==36 or pos==48 or pos==60 or pos==72 or pos==84 or pos==96 or pos==108 or pos==120 or pos==132:
        return False
    elif maze[pos-1]==0:
        return False
    return pos-1

def move_up(pos):
    if pos==0 or pos==1 or pos==2 or pos==3 or pos==4 or pos==5 or pos==6 or pos==7 or pos==8 or pos==9 or pos==10 or pos==11:
        return False
    elif maze[pos-12]==0:
        return False
    return pos-12

def move_down(pos):
    if pos==132 or pos==133 or pos==134 or pos==135 or pos==136 or pos==137 or pos==138 or pos==139 or pos==140 or pos==141 or pos==142  or pos==143:
        return False
    elif maze[pos+12]==0:
        return False
    return pos+12

def dfs(visited_dfs , maze , node , moves):
    
    if node.position not in visited_dfs:
        visited_dfs.add(node.position)
        if node.position==goal:
            print("\nDFS GOAL ACHIEVED , searching steps :" + str(moves) )
            return True
        if move_up(node.position):
            new_node = createNode(move_up(node.position) , node.cost+1)
            moves += 1
            dfs(visited_dfs , maze , new_node , moves)
        if move_left(node.position):
            new_node = createNode(move_left(node.position) , node.cost+1)
            moves += 1
            dfs(visited_dfs , maze , new_node , moves)
        if move_right(node.position):
            new_node = createNode(move_right(node.position) , node.cost+1)
            moves += 1
            dfs(visited_dfs , maze , new_node , moves)
        if move_down(node.position):
            new_node = createNode(move_down(node.position) , node.cost+1)
            moves += 1
            dfs(visited_dfs , maze , new_node , moves)
        
    
def bfs(visited_bfs , queue_bfs , cost_bfs , maze , node , moves ):
    visited_bfs.append(node.position)
    queue_bfs.append(node.position)
    cost_bfs.append(node.cost)

    while queue_bfs:
        current_node = createNode(queue_bfs.pop(0) , cost_bfs.pop(0))
        if current_node.position == goal:
            print("BFS GOAL ACHIEVED , searching steps :"  + str(moves) + "\n")
            return True

        if move_up(current_node.position):
            new_node = createNode(move_up(current_node.position) , current_node.cost+1)
            if new_node.position not in visited_bfs:
                moves += 1
                visited_bfs.append(new_node.position)
                queue_bfs.append(new_node.position)
                cost_bfs.append(new_node.cost)

        if move_left(current_node.position):
            new_node = createNode(move_left(current_node.position) , current_node.cost+1)
            if new_node.position not in visited_bfs:
                moves += 1
                visited_bfs.append(new_node.position)
                queue_bfs.append(new_node.position)
                cost_bfs.append(new_node.cost)

        if move_right(current_node.position):
            new_node = createNode(move_right(current_node.position) , current_node.cost+1)
            if new_node.position not in visited_bfs:
                moves += 1
                visited_bfs.append(new_node.position)
                queue_bfs.append(new_node.position)
                cost_bfs.append(new_node.cost)

        if move_down(current_node.position):
            new_node = createNode(move_down(current_node.position) , current_node.cost+1)
            if new_node.position not in visited_bfs:
                moves += 1
                visited_bfs.append(new_node.position)
                queue_bfs.append(new_node.position)
                cost_bfs.append(new_node.cost)



def printmaze():    
    ch = 0
    for i in range ((size*size)):
        print(maze[i] , end=" ")
        ch += 1
        if ch==12:
            print()
            ch = 0

if __name__ == "__main__":
    print("\n\nTHE MAZE:\n0->block space\n1->empty space\n")
    printmaze()
    # print("\n\n")

    root_node = createNode (59 , 0)
    
    visited_dfs = set()
    dfs(visited_dfs , maze , root_node , 0)

    visited_bfs = list()
    queue_bfs = list()
    cost_bfs = list()
    bfs(visited_bfs , queue_bfs , cost_bfs , maze , root_node , 0)
    # print("\n\n")