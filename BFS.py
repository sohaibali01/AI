
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

def BFS():
    initialState = 'Arad'
    goalState = 'Bucharest'

    # we think of a graph as a dictionary, items comprise of nodes, where
    # each node has a key and a value. Key is simply the state of the node
    # and value are actual attributes that node object

    graph = {'Arad': Node('Arad', None, ['Zerind', 'Timisoara', 'Sibiu'], None),
             'Zerind': Node('Zerind', None, ['Oradea', 'Arad'], None),
             'Oradea': Node('Oradea', None, ['Sibiu','Zerind'], None),
             'Sibiu': Node('Sibiu', None, ['Fagaras', 'RimnicuVilcea','Oradea', 'Arad'], None),
             'Timisoara': Node('Timisoara', None, ['Lugoj', 'Arad'], None),
             'Lugoj': Node('Lugoj', None, ['Mehadia', 'Timisoara'], None),
             'Mehadia': Node('Mehadia', None, ['Drobeta', 'Lugoj'], None),             
             'Drobeta': Node('Drobeta', None, ['Craiova','Mehadia'], None),
             'Craiova': Node('Craiova', None, ['RimnicuVilcea', 'Pitesti','Drobeta'], None),
             'RimnicuVilcea': Node('RimnicuVilcea', None, ['Sibiu', 'Pitesti', 'Craiova'], None),            
             'Fagaras': Node('Fagaras', None, ['Bucharest','Sibiu'], None),             
             'Bucharest': Node('Bucharest', None, ['Giurgiu', 'Pitesti', 'Urziceni','Fagaras'], None),
             'Giurgiu': Node('Giurgiu', None, ['Bucharest'], None),             
             'Pitesti': Node('Pitesti', None, ['Craiova', 'RimnicuVilcea', 'Bucharest'], None),             
             'Urziceni': Node('Urziceni', None, ['Hirsova', 'Vaslui','Bucharest'], None),             
             'Hirsova': Node('Hirsova', None, ['Eforie','Urziceni'], None),             
             'Eforie': Node('Eforie', None, ['Hirsova'], None),             
             'Vaslui': Node('Vaslui', None, ['Iasi','Urziceni'], None),             
             'Iasi': Node('Iasi', None, ['Neamt','Vaslui'], None),             
             'Neamt': Node('Neamt', None, ['Iasi'], None) }
            
    frontier = [initialState]
    explored=[]

    while len(frontier)!=0:
        
        currentNode = frontier.pop(0)
        
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
                #print(currentNode)
                #print(child)
                #print(frontier)
            #print()
        #print()
        #if currentChildren==0:
        #   del explored[len(explored)-1]
    
solution = BFS()
print(solution)







