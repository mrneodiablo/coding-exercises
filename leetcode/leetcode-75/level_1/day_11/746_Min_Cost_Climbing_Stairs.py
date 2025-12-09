from typing import List
import unittest


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i + 2], cost[i] + cost[i + 1])
        return min(cost[0], cost[1])


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        cost = [10, 15, 20]
        expect = 15
        self.assertEqual(
            str(self.solution.minCostClimbingStairs(cost)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        cost = [1, 10, 15, 20]
        expect = 16
        self.assertEqual(
            str(self.solution.minCostClimbingStairs(cost)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_3(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1, 0]

        expect = 6
        self.assertEqual(
            str(self.solution.minCostClimbingStairs(cost)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
