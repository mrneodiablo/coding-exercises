import collections
from typing import List
import unittest


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())
        # total_elements_with_max_freq, last row elements
        max_freq_ele_count = 0
        i = 0
        while i < len(freq):
            if freq[i] == max_freq:
                max_freq_ele_count += 1
            i += 1

        ans = (max_freq - 1) * (n + 1) + max_freq_ele_count

        return max(ans, len(tasks))


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        expect = 8
        self.assertEqual(
            self.solution.leastInterval(tasks, n),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        expect = 6
        self.assertEqual(
            self.solution.leastInterval(tasks, n),
            expect,
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
