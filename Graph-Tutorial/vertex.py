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
      
    def __hash__(self):
        """Return hash of vertex class, for using this class as a dict key."""
        return hash(self.id)

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
