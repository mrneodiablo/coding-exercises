"""
Docstring for neetcode.neetcode-150.detect_squares
2013. Detect Squares

You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.

Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points
"""

from collections import defaultdict
from typing import List
import unittest


class DetectSquares:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        x, y = point
        self.cnt[(x, y)] += 1
        self.points.append((x, y))

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for px, py in self.points:
            if px == x and py != y:
                d = py - y
                res += self.cnt[(x + d, y)] * self.cnt[(x + d, py)]
                res += self.cnt[(x - d, y)] * self.cnt[(x - d, py)]

        return res


class TestDetectSquares(unittest.TestCase):

    def test_basic_square_detection(self):
        """Test basic square detection with 4 points forming a square"""
        detectSquares = DetectSquares()
        detectSquares.add([3, 10])
        detectSquares.add([11, 2])
        detectSquares.add([3, 2])

        # Query point [11, 10] should form 1 square with the 3 added points
        result = detectSquares.count([11, 10])
        self.assertEqual(result, 1)

    def test_no_square_possible(self):
        """Test when no square can be formed"""
        detectSquares = DetectSquares()
        detectSquares.add([3, 10])
        detectSquares.add([11, 2])
        detectSquares.add([3, 2])

        # Query point [14, 8] cannot form a square with any points
        result = detectSquares.count([14, 8])
        self.assertEqual(result, 0)

    def test_duplicate_points(self):
        """Test counting squares with duplicate points"""
        detectSquares = DetectSquares()
        detectSquares.add([3, 10])
        detectSquares.add([11, 2])
        detectSquares.add([3, 2])
        detectSquares.add([11, 2])  # Add duplicate point

        # Query point [11, 10] should form 2 squares (one with each duplicate)
        result = detectSquares.count([11, 10])
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
