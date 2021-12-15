#Prims Algorithm Implementation By Ziithe Ewen Hiwa

from typing import List, Dict # For annotations

#Define Node class
class Node :
    def __init__(self, arg_id) :
        self._id = arg_id

class Graph:
    def __init__(self, source, adj_list) :
        self.source = source
        self.adjlist = adj_list

    def PrimsMST (self) -> int :

        # The distance of source node from itself is 0. Add source node as the first node
        # in the priority queue
        priority_queue = { Node(self.source) : 0 }
        added = [False] * (len(self.adjlist)+1)
        min_span_tree_weight = 0

        while priority_queue :
            # Choose the adjacent node with the least edge weight
            node = min (priority_queue, key=priority_queue.get)
            weight = priority_queue[node]

            # Remove the node from the priority queue
            del priority_queue[node]

            if added[node._id] == False :
                min_span_tree_weight += weight
                added[node._id] = True
                print("Added Vertex : " + str(node._id) + ", current weight is : "+str(min_span_tree_weight))

                for item in self.adjlist[node._id] :
                    adjnode = item[0]
                    adjweight = item[1]
                    if added[adjnode] == False :
                        priority_queue[Node(adjnode)] = adjweight

        return min_span_tree_weight

def main() :

    g1_edges_from_node = {}

    # Implement graphs adjacency list
    g1_edges_from_node[1] = [ (2,28), (6,10) ]
    g1_edges_from_node[2] = [ (1,28), (3,16), (7,14) ]
    g1_edges_from_node[3] = [ (2,16), (4,12) ]
    g1_edges_from_node[4] = [ (3,12), (5,22), (7,18) ]
    g1_edges_from_node[5] = [ (4,22), (6,25), (7,24) ]
    g1_edges_from_node[6] = [ (1,10), (5,25) ]
    g1_edges_from_node[7] = [ (2,14), (4,18), (5,24) ]

    #Put starting node as 6
    g1 = Graph(6, g1_edges_from_node)
    weight = g1.PrimsMST()
    print("\nTotal weight of the Minimum Spanning Tree for this graph is : " + str(weight) +"\n")


main()