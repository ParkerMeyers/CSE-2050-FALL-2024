import unittest

from Graph import AdjacencySetGraph, EdgeSetGraph, Graph


class GraphTestFactory:
    """
    A factory class for testing graph implementations.
    This class provides common test methods for different graph data structures.
    """

    def setUp(self):
        """
        Sets up the graph data structure for testing.
        This method should be overridden in subclasses to specify the graph implementation.
        """
        self.graph_ds = None

    def test_graph_construction(self):
        """
        Tests the construction of a graph by adding vertices and edges.
        """
        g = self.graph_ds()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_edge(('A', 'B'))
        self.assertIn('A', g)
        self.assertIn('B', g)
        self.assertIn('B', g.nbrs('A'))
        self.assertIn('A', g.nbrs('B'))

    def test_graph_construction_init(self):
        """
        Tests the construction of a graph by initializing it with vertices and edges.
        """
        V = {'A', 'B'}
        E = {('A', 'B')}
        g = self.graph_ds(V, E)
        self.assertIn('A', g)
        self.assertIn('B', g)
        self.assertIn('B', g.nbrs('A'))
        self.assertIn('A', g.nbrs('B'))

    def test_is_connected_simple(self):
        """
        Tests the is_connected method for a simple graph.
        """
        V = {'A', 'B', 'C'}
        E = {('A', 'B')}
        g = self.graph_ds(V, E)
        self.assertTrue(g.is_connected('A', 'B'))
        self.assertFalse(g.is_connected('A', 'C'))

    def test_is_connected_cycle(self):
        """
        Tests the is_connected method for a graph with a cycle.
        """
        V = {'A', 'B', 'C'}
        E = {('A', 'B'), ('B', 'C'), ('C', 'A')}
        g = self.graph_ds(V, E)
        self.assertTrue(g.is_connected('A', 'C'))

    def test_bfs(self):
        """
        Tests the bfs method for a graph.
        """
        V = {'A', 'B', 'C', 'D', 'E'}
        E = {('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')}
        g = self.graph_ds(V, E)
        dist_from_A_expected = {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2}
        tree = g.bfs('A')
        dist_from_A_actual = {v: len(g.shortest_path('A', v)) - 1 for v in tree}
        self.assertEqual(dist_from_A_actual, dist_from_A_expected)

    def test_count_trees(self):
        """
        Tests the count_trees method for a graph.
        """
        V = {'A', 'B', 'C', 'D', 'E'}
        E = {('A', 'B'), ('A', 'C'), ('D', 'E')}
        g = self.graph_ds(V, E)
        trees, count = g.count_trees()
        self.assertEqual(count, 2)
        self.assertTrue(any(set(tree.keys()) == {'A', 'B', 'C'} for tree in trees))
        self.assertTrue(any(set(tree.keys()) == {'D', 'E'} for tree in trees))

    def test_shortest_path(self):
        """
        Tests the shortest_path method for a graph.
        """
        V = {'A', 'B', 'C', 'D', 'E'}
        E = {('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')}
        g = self.graph_ds(V, E)
        path = g.shortest_path('A', 'E')
        self.assertEqual(len(path), 3)
        self.assertEqual(path, ['A', 'C', 'E'])


class TestAdjacency(GraphTestFactory, unittest.TestCase):
    """
    Unit tests for the AdjacencySetGraph class.
    """

    def setUp(self):
        """
        Sets up the AdjacencySetGraph for testing.
        """
        self.graph_ds = AdjacencySetGraph


class TestEdge(GraphTestFactory, unittest.TestCase):
    """
    Unit tests for the EdgeSetGraph class.
    """

    def setUp(self):
        """
        Sets up the EdgeSetGraph for testing.
        """
        self.graph_ds = EdgeSetGraph


class TestGraph(unittest.TestCase):
    """
    Unit tests for the Graph class.
    """

    def test_graph_init(self):
        """
        Tests that initializing the Graph class raises a NotImplementedError.
        """
        with self.assertRaises(NotImplementedError):
            Graph()


if __name__ == "__main__":
    unittest.main()
