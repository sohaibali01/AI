
def actionSequence(graph, initialState, goalState):
    # returns a list of states starting from goal state moving upwards towards
    # parents until root node is reached
    solution=[goalState]
    currentParent=graph[goalState].parent
    while currentParent!=None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

class Node:
    #state = state         # class variable shared by all instances
    def __init__(self, state, parent, actions, totalCost):
        self.state = state    # instance variable unique to each instance
        self.parent = parent
        self.actions = actions # we are not saving actions themselves,
                               # only output states of those actions 
        self.totalCost = totalCost

def DFS():
    initialState = 'D'
    goalState = 'C'

    # we think of a graph as a dictionary, items comprise of nodes, where
    # each node has a key and a value. Key is simply the state of the node
    # and value are actual attributes that node object

    graph = {'A': Node('A', None, ['B', 'E', 'C'], None),
             'B': Node('B', None, ['D', 'E', 'A'], None),
             'C': Node('C', None, ['A', 'F', 'G'], None),
             'D': Node('D', None, ['B', 'E'], None),
             'E': Node('E', None, ['A', 'B','D'], None),
             'F': Node('F', None, ['C'], None),
             'G': Node('G', None, ['C'], None)}
            
    frontier = [initialState]
    explored=[]

    while len(frontier)!=0:
        
        currentNode = frontier.pop(len(frontier)-1)
        
        explored.append(currentNode)
        #currentChildren=0
        for child in graph[currentNode].actions:
            if child not in frontier and child not in explored:
                graph[child].parent=currentNode
                if graph[child].state==goalState:
                    #print(explored)
                    return actionSequence(graph, initialState, goalState)
                #currentChildren=currentChildren+1
                frontier.append(child)
                print(currentNode)
                print(child)
                print(frontier)
            print()
        print()
        #if currentChildren==0:
        #   del explored[len(explored)-1]
    
solution = DFS()
print(solution)



