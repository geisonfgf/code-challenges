import unittest
from train_problem import distance


class TestTrainProblem(unittest.TestCase):
    
    def setUp(self):
        self.graph = {'A': {'B': 5, 'D': 5, 'E': 7},
                      'B': {'C': 4},
                      'C': {'D': 8, 'E': 2},
                      'D': {'C': 8, 'E': 6},
                      'E': {'B': 3}}

    def test_the_distance_of_the_route_A_B_C(self):
        self.assertEqual(distance(self.graph, ['A', 'B', 'C']), 9)

    def test_the_distance_of_the_route_A_D(self):
        self.assertEqual(distance(self.graph, ['A', 'D']), 5)

    def test_the_distance_of_the_route_A_D_C(self):
        self.assertEqual(distance(self.graph, ['A', 'D', 'C']), 13)

    def test_the_distance_of_the_route_A_E_B_C_D(self):
        self.assertEqual(distance(self.graph, ['A', 'E', 'B', 'C', 'D']), 22)

    def test_the_distance_of_the_route_A_E_D(self):
        self.assertEqual(distance(self.graph, ['A', 'E', 'D']), 'NO SUCH ROUTE')


if __name__ == '__main__':
    unittest.main()
