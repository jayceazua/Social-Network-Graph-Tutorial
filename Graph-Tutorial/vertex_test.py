import unittest
from vertex import Vertex

class VertexTest(unittest.TestCase):

    def test_init(self):
        id = "A"
        v = Vertex(id)
        assert v.id == id
        self.assertDictEqual(v.neighbors, {})

    def test_add_neighbor(self):
        v1 = Vertex(1)
        v2 = Vertex(2)
        # Test default weight variable
        v1.add_neighbor(v2)
        self.assertDictEqual(v1.neighbors, {v2: 1})
        # Error should be raised if v2 is added again
        with self.assertRaises(KeyError):
            v1.add_neighbor(v2)
        # Test passed in weight variable
        v3 = Vertex(3)
        v1.add_neighbor(v3, 3)
        self.assertDictEqual(v1.neighbors, {v2: 1, v3: 3})
        # Error should be raised if v3 is added again
        with self.assertRaises(KeyError):
            v1.add_neighbor(v3, 3)
        # Test recursive adding
        v2.add_neighbor(v1)
        self.assertDictEqual(v2.neighbors, {v1: 1})
        v3.add_neighbor(v1)
        self.assertDictEqual(v3.neighbors, {v1: 1})

    def test_get_neighbors(self):
        v1 = Vertex(1)
        v2 = Vertex(2)
        v3 = Vertex(3)
        # Test getting neighbors
        v1.add_neighbor(v2)
        v1.add_neighbor(v3)
        self.assertCountEqual(v1.get_neighbors(), [v2, v3])
        v2.add_neighbor(v1, 2)
        v2.add_neighbor(v3, 2)
        self.assertCountEqual(v2.get_neighbors(), [v1, v3])
        v3.add_neighbor(v1, 3)
        v3.add_neighbor(v2, 3)
        self.assertCountEqual(v3.get_neighbors(), [v1, v2])

    def test_get_id(self):
        # Test alphabetical ids
        v_a = Vertex("A")
        assert v_a.get_id() == "A"
        v_b = Vertex("B")
        assert v_b.get_id() == "B"
        v_c = Vertex("C")
        assert v_c.get_id() == "C"
        # Test numerical ids
        v1 = Vertex(1)
        assert v1.get_id() == 1
        v2 = Vertex(2)
        assert v2.get_id() == 2
        v3 = Vertex(3)
        assert v3.get_id() == 3

    def test_get_edge_weight(self):
        v1 = Vertex(1)
        v2 = Vertex(2)
        v3 = Vertex(3)
        # Test default weight variable
        v2.add_neighbor(v1)
        assert v2.get_edge_weight(v1) == 1
        # Test passed in weight variable
        v2.add_neighbor(v3, 3)
        assert v2.get_edge_weight(v3) == 3
