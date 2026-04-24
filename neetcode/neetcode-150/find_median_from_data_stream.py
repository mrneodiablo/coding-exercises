"""
295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.

"""

import unittest
import heapq  # min


class MedianFinder:

    def __init__(self):
        self.half_lower = []

        self.half_upper = []

        self.length_of_num_list = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.half_lower, -num)
        heapq.heappush(self.half_upper, -heapq.heappop(self.half_lower))
        if len(self.half_upper) > len(self.half_lower):
            heapq.heappush(self.half_lower, -heapq.heappop(self.half_upper))

        self.length_of_num_list += 1

    def findMedian(self) -> float:
        if self.length_of_num_list % 2 != 0:
            return -self.half_lower[0]
        return (-self.half_lower[0] + self.half_upper[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class TestMedianFinder(unittest.TestCase):
    def test_single_element(self):
        mf = MedianFinder()
        mf.addNum(5)
        self.assertEqual(mf.findMedian(), 5)

    def test_even_number_of_elements(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(3)
        self.assertAlmostEqual(mf.findMedian(), 2.0)

    def test_odd_number_of_elements(self):
        mf = MedianFinder()
        for n in [2, 1, 5]:
            mf.addNum(n)
        self.assertEqual(mf.findMedian(), 2)

    def test_negative_and_positive(self):
        mf = MedianFinder()
        for n in [-1, 0, 1]:
            mf.addNum(n)
        self.assertEqual(mf.findMedian(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
