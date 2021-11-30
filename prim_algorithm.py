# In this program, I'll be implementing Prim's algorithm to calculate a 
# graph's Minimum Spanning Tree.heapq

def adj_prim(v, graph):
      visitedList = []
      for i in range(0, v):
          visitedList.append([])
          for j in range(0, v):
              visitedList[i].append(0)
      for i in range(0, len(graph)):
          visitedList[graph[i][0]][graph[i][1]] = graph[i][2]
          visitedList[graph[i][1]][graph[i][0]] = graph[i][2]
      return visitedList
      
# v refers to the number of vertices, while graph refers to the input we shall receive to calculate the MST.
def prim_algorithm(v, graph):
      print("Welcome to the MST Program, where we will calculate the MST for a given graph: ")
      #We will use the function above to create an adjacency list from the graph we receive as input
      visitedList = adj_prim(v, graph)

      #We will choose a starting point/node for our implementation.
      starting_vertex = 0
      minSpanTree = []
      edges = []
      visited = []
      minEdge = [None,None,float('inf')]
      #We will ensure that our minimum spanning tree contains every vertex in our graph.
      while len(minSpanTree) != v-1:
          visited.append(starting_vertex)
          for x in range(0, v):
              if visitedList[starting_vertex][x] != 0:
                  edges.append([starting_vertex, x, visitedList[starting_vertex][x]])
          #Attain Prim's constraint by visiting the next adjacent vertex with the smallest weight that has yet to be visited.
          for y in range(0, len(edges)):
              if edges[y][2] < minEdge[2] and edges[y][1] not in visited:
                  minEdge = edges[y]
          edges.remove(minEdge)
          minSpanTree.append(minEdge)
          starting_vertex = minEdge[1]
          minEdge = [None,None,float('inf')]
      return minSpanTree

#To run the algorithm, we will pass in the graph's number of vertices and graph and obtain our MST.

    