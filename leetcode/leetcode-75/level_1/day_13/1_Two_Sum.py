from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if hash_map.get(complement) is not None:
                output = [hash_map.get(complement), i]
            else:
                hash_map[num] = i
        return output


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expect = [0, 1]
        self.assertEqual(
            str(self.solution.twoSum(nums, target)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        nums = [3, 2, 4]
        target = 6
        expect = [1, 2]
        self.assertEqual(
            str(self.solution.twoSum(nums, target)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_3(self):
        nums = [3, 3]
        target = 6
        expect = [0, 1]
        self.assertEqual(
            str(self.solution.twoSum(nums, target)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
