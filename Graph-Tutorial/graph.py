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
        self.parent = None

    def __repr__(self):
        """Return representation of vertex object."""
        return f"Vertex({self.id})"

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f"{self.id} adjacent to {[x.id for x in self.neighbors]}"

    def _check_type(self, other, operator):
        """Raise TypeError if there is a type mismatch."""
        # Get the name of the type of other object
        other_type = type(other).__name__
        # Create the error message if there is a type mismatch
        error_message = f"""'{operator}' not supported between
                            instances of 'Vertex' and '{other_type}'"""
        # If the other object is not of type Vertex, raise TypeError
        if not isinstance(other, Vertex):
            raise TypeError(error_message)

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

    def make_graph_from_file(self, file_name):
        """Read graph data from a file, and create a graph based on it."""
        valid_types = "gGdD"

        graph_type = ""
        vertices = ""
        edge_list = []
        directed = False
        weighted = False

        with open(file_name, 'r') as f:
            for line in f.readlines():
                # Strip trailing whitespace
                line = line.rstrip()

                # Skip line if it is empty to prevent index range errors below
                if line == "":
                    # Moves to next line (next iteration of for loop)
                    continue

                # Find graph type
                if line[0] in string.ascii_letters:
                    if line[0] in valid_types:
                        graph_type = line[0].upper()
                    else:
                        raise ValueError("Looking for type 'G' or 'D'")

                # Find list of vertices
                if line[0] in string.digits:
                    vertices = line

                # Find edges
                if line[0] == "(":
                    edge_list.append(line)

        # See if graph is a digraph
        if graph_type == "D":
            directed = True
        # See if graph is weighted
        if len(edge_list[0].split(",")) == 3:
            weighted = True

        # Set the graph type if it has not been set yet
        if self.num_vertices == 0:
            self.weighted = weighted
            self.directed = directed

        # Add vertices to graph
        # TODO: Does not handle string vertex names
        for vertex in vertices.split(","):
            self.add_vertex(int(vertex))

        # Add edges to graph
        # TODO: Does not handle string vertex names or decimal weights
        for edge in edge_list:
            # Remove parenthesis
            data = edge[1:-1]
            # Turn data into array by splitting on commas
            data = data.split(",")

            # Split the tuple correctly
            if weighted:
                # Remove parenthesis from strings, and convert strings to ints
                self.add_edge(int(data[0]), int(data[1]), int(data[2]))
            else:
                # Remove parenthesis from strings, and convert strings to ints
                self.add_edge(int(data[0]), int(data[1]))

    def breadth_first_search(self, vertex, n, only_new=True):
        """Find all vertices n edges away from the passed in vertex."""
        # Raise error if non vertex object is passed in as vertex
        if not isinstance(vertex, Vertex):
            raise TypeError("vertex parameter must be of type Vertex")

        # Raise error if vertex not in the graph
        if vertex not in self.get_vertices():
            raise ValueError(f"{vertex} is not in the Graph")

        # If the search is looking for vertices only accessible at level n,
        if only_new:
            # Create a set of vertices that have already been visited
            seen_vertices = set([vertex])

        # Create deque with passed in vertex
        vertex_deque = deque([vertex])
        # n_counter tracks the current level
        n_counter = 0
        # counter tracks how many vertices from level n are still in the deque
        counter = 1

        # Keep looping until there are no more vertices to go through, or
        # until the nth level has been reached
        while len(vertex_deque) > 0 and n_counter < n:
            # Grab a vertex from the front of the deque
            popped_vertex = vertex_deque.popleft()

            # Queue vertices if they will be seen for the first time
            if only_new:
                # Go through the neighbors of the popped_vertex
                for vert in popped_vertex.get_neighbors():
                    # If this vertex is new, allow it to be traversed
                    if vert not in seen_vertices:
                        # Set the parent of this vertex as the popped vertex
                        vert.parent = popped_vertex
                        # Add vertex to back of the deque
                        vertex_deque.append(vert)
                        # Mark that the vertex has been seen
                        seen_vertices.add(vert)
            # Otherwise, just add all vertices
            else:
                # Add all vertices that vert can reach to the back of the deque
                vertex_deque.extend(popped_vertex.get_neighbors())
            # Remove one from the counter because a vertex was just popped
            counter -= 1

            # When all nodes from the current level are removed
            if counter == 0:
                # Set the current level that all the current vertices are on
                n_counter += 1
                # Track how many vertices can be reached on this level
                counter = len(vertex_deque)

        # If the loop above ends early due to lack of levels,
        if n_counter < n:
            # Return empty set because no vertices exist n edges away
            return set()
        # Return a set of all the vertices that can be reached at the nth level
        return set(vertex_deque)

    def find_path(self, from_vert, to_vert):
        # Make sure that both nodes from_vert and to_vert are actually in the graph
        # Run BFS or DFS starting from from_vert
        # Figure out a way to keep track of each path you take
        # Once you find to_vert, end the search.
        # Since you've been tracking the paths, find the path that goes from from_vert to to_vert
        # Return the path, in the order of nodes visited starting with from_vert and ending with to_vert
        # Driver code
        pass

    def find_shortest_path(self, from_v, to_u):
        # Raise error if start or end does not exist in graph
        if from_v not in self.vert_list:
            raise KeyError(f"Vertex({from_v}) is not in the Graph")
        if to_u not in self.vert_list:
            raise KeyError(f"Vertex({to_u}) is not in the Graph")

        # Set the starting and ending vertices, using start and end keys
        start_vert = self.vert_list[from_v]
        end_vert = self.vert_list[to_u]

        # Get the vertices one edge away from starting vertex
        level = 1
        verts_at_n_level = self.breadth_first_search(start_vert, level)
        # Keep searching levels there is nothing, or the end vertex is found
        while end_vert not in verts_at_n_level:
            # If there are no more vertices to search
            if len(verts_at_n_level) == 0:
                # Return None because there is no path between the vertices
                return None
            # Get the vertices one more edge away from the starting vertex
            level += 1
            verts_at_n_level = self.breadth_first_search(start_vert, level)

        # Create a path list and the ending vertex
        path = [end_vert]
        parent = end_vert
        # Go through the parents of each vertex, until start vertex is reached
        while start_vert != parent:
            # Move to the parent of the current vertex, and add it to the path
            parent = parent.parent
            path.append(parent)

        # Reverse the path, and return it
        path[:] = reversed(path)
        return path

    def clique(self):
        # Start with an arbitrary vertex u and add it to the clique
        # For v in remaining vertices not in the clique
        # If v is adjacent to every other vertex already in the clique.
        # Add v to the clique
        # Discard v otherwise
        pass


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
