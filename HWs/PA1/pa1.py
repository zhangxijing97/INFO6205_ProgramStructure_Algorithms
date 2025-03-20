import heapq
import sys
import argparse

class Graph:
    def __init__(self, numV):
        self.numV = numV
        self.adj = [[] for _ in range(numV)]  # Adjacency list

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))  # Directed edge from u to v with given weight

    def dijkstra(self, src, ignore_edge=None):
        """
        Runs Dijkstra's algorithm from the given source vertex.
        If ignore_edge is specified, it temporarily ignores that edge.
        """
        dist = [float('inf')] * self.numV
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            current_dist, u = heapq.heappop(pq)
            if current_dist > dist[u]:
                continue
            
            for v, weight in self.adj[u]:
                if ignore_edge and ignore_edge == (u, v):
                    continue  # Ignore a specific edge
                
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        
        return dist

    def find_shortest_cycle(self):
        """
        Finds the shortest cycle in the graph using Dijkstra's algorithm.
        """
        shortest_cycle = float('inf')
        
        for u in range(self.numV):
            for v, weight in self.adj[u]:
                # Temporarily remove edge (u, v)
                shortest_paths = self.dijkstra(v, ignore_edge=(u, v))
                if shortest_paths[u] != float('inf'):
                    shortest_cycle = min(shortest_cycle, shortest_paths[u] + weight)
        
        return shortest_cycle if shortest_cycle != float('inf') else 0


def read_graph_from_file(filename):
    """
    Reads a directed graph from a file.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    graph_dict = {}
    max_vertex = -1
    
    for line in lines:
        parts = line.split(':')
        if len(parts) != 2:
            continue
        
        src = int(parts[0].strip())
        edges = parts[1].strip().split()
        graph_dict[src] = []
        
        for i in range(0, len(edges), 2):
            dest = int(edges[i])
            weight = int(edges[i+1])
            graph_dict[src].append((dest, weight))
            max_vertex = max(max_vertex, src, dest)
    
    numV = max_vertex + 1
    graph = Graph(numV)
    
    for u in graph_dict:
        for v, w in graph_dict[u]:
            graph.add_edge(u, v, w)
    
    return graph

if __name__ == "__main__":
    input_filename = "testcase-1.txt"  # Default input file, edit the input_filename to get another test case file
    
    try:
        graph = read_graph_from_file(input_filename)
        shortest_cycle_length = graph.find_shortest_cycle()
        print(f"The length of the shortest cycle is: {shortest_cycle_length}")
    except Exception as e:
        print(f"Error: {e}")

"""
(2) (20 points) Describe your algorithm in English as comments. It MUST use Dijkstra’s algorithm.

function FIND_SHORTEST_CYCLE(graph):
    shortest_cycle = ∞

    for each edge (u → v, weight) in graph:
        remove edge (u → v)
        shortest_path = DIJKSTRA(graph, start=v, ignore_edge=(u, v))
        
        if shortest_path[u] is not ∞:
            cycle_length = shortest_path[u] + weight
            shortest_cycle = min(shortest_cycle, cycle_length)
        
        restore edge (u → v)
    
    if shortest_cycle == ∞:
        return 0  # No cycle exists
    else:
        return shortest_cycle

function DIJKSTRA(graph, start, ignore_edge=None):
    Initialize dist[] = ∞ for all vertices
    dist[start] = 0
    PriorityQueue pq ← [(0, start)]  # Min-heap (distance, node)
    
    while pq is not empty:
        (current_distance, u) ← pq.pop()
        
        if current_distance > dist[u]:
            continue  # Skip outdated distances
        
        for each (v, weight) in graph[u]:
            if (u, v) == ignore_edge:
                continue  # Skip ignored edge
            
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                pq.push((dist[v], v))
    
    return dist[]  # Return shortest distances from start node"
"""