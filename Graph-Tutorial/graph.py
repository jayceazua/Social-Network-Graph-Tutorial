#!python
from collections import deque
import random
import string


class Vertex(object):
    """ Vertex Class
    A helper class for the Graph class that defines vertices and vertex
    neighbors.
    """

    def __init__(self, vertex_id):
        """Initialize a vertex and its neighbors.

        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.id = vertex_id
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=1):
        """Add a neighbor along a weighted edge."""
        # Check if vertex is already a neighbor
        if vertex in self.neighbors:
            # If so, raise KeyError
            raise KeyError(f"{vertex.id} is already a neighbor of {self.id}")
        # If not, add vertex to neighbors and assign weight
        self.neighbors[vertex] = weight

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f"{self.id} adjacent to {[x.id for x in self.neighbors]}"

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        # Return the neighbors
        return set(self.neighbors.keys())

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # Return the weight of the edge from this vertex to the given vertex
        return self.neighbors[vertex]


class Graph:
    """ Graph Class
    A class demonstrating the essential facts and functionalities of graphs.
    """

    def __init__(self, weighted=False, directed=True):
        """Initialize a graph object with an empty dictionary."""
        self.vert_list = {}
        self.num_vertices = 0
        self.weighted = weighted
        self.directed = directed

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return
        the vertex."""
        # Raise error if key already exists in graph
        if key in self.vert_list:
            raise KeyError(f"Vertex({key}) is already in the Graph")
        # Increment the number of vertices
        self.num_vertices += 1
        # Create a new vertex
        new_vertex = Vertex(key)
        # Add the new vertex to the vertex list
        self.vert_list[key] = new_vertex
        # Return the new vertex
        return new_vertex

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        # Raise error if key does not exist in graph
        if key not in self.vert_list:
            raise KeyError(f"Vertex({key}) is not in the Graph")
        # Return the vertex if it is in the graph
        return self.vert_list[key]

    def add_edge(self, from_key, to_key, weight=1):
        """Add an edge from vertex with key `key1` to vertex with key `key2`
        with a weight."""
        """Add edge from vertex with key `from_key` to vertex with key `to_key`.
        If a weight is provided, use that weight.
        """
        if weight != 1 and not self.weighted:
            print(f"Detected weight of {weight} in unweighted graph.")
            print("Graph is now weighted, all previous vertices have weight 1")
            self.weighted = True

        # Add from_key vertex if it is not in the graph
        if from_key not in self.vert_list:
            self.add_vertex(from_key)

        # Add to_key vertex if it is not in the graph
        if to_key not in self.vert_list:
            self.add_vertex(to_key)

        # Get vertices from keys
        from_vert = self.vert_list[from_key]
        to_vert = self.vert_list[to_key]

        # When both vertices in graph, make from_vert a neighbor of to_vert
        from_vert.add_neighbor(to_vert, weight)
        # If the graph undirected, add connection back from to_vert to from_key
        if not self.directed:
            to_vert.add_neighbor(from_vert, weight)

    def get_vertices(self):
        """Return all the vertices in the graph"""
        return self.vert_list.keys()

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax:
        for v in g"""
        return iter(self.vert_list.values())

    def make_graph_from_file(filename):
        # Check if first line is 'G' or 'D' and store the value. If neither, raise an exception
        # For each vertex id in first line, add a vertex to the graph
        # For each of the following lines:
        # Extract the vertex ids and the (optional) weight, and add an edge to the graph
        # If it is a Graph and not a Digraph, add another edge in the opposite direction
        # Raise an exception if line contains too many (or too few) items

    def get_neighbors(self):
        # Make sure the input node is actually in the graph
        # Find all edges for the input node
        # See what nodes are connected to the input node via the edge
        # return the connected nodes

    def breadth_first_search(self, vertex, n):
        # Make sure the input node is actually in the graph
        # Run breadth_first_search starting from the input node and going `n` levels deep
        # Return all nodes found at the `n`th level

    def find_path(self, from_vert, to_vert):
        # Make sure that both nodes from_vert and to_vert are actually in the graph
        # Run BFS or DFS starting from from_vert
        # Figure out a way to keep track of each path you take
        # Once you find to_vert, end the search.
        # Since you've been tracking the paths, find the path that goes from from_vert to to_vert
        # Return the path, in the order of nodes visited starting with from_vert and ending with to_vert
        # Driver code

    def find_shortest_path(self, A, B):
        # Make sure that both nodes A and B are actually in the graph
        # Run BFS starting from A
        # Figure out a way to keep track of each path you take
        # Once you find B, end the search.
        # Since you've been tracking the paths, find the shortest path that goes from A to B
        # Return the shortest path, in the order of nodes visited starting with A and ending with B
    
    def clique(self):
        # Start with an arbitrary vertex u and add it to the clique
        # For v in remaining vertices not in the clique
        # If v is adjacent to every other vertex already in the clique.
        # Add v to the clique
        # Discard v otherwise


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print(f"The vertices are: {g.get_vertices()} \n")

    # Print edges
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print(f"( {v.get_id()} , {w.get_id()} )")
