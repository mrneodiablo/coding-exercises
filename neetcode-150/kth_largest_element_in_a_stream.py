"""
Kth Largest Element in a Stream
You are part of a university admissions office and need to keep track
of the kth highest test score from applicants in real-time.
This helps to determine cut-off marks for interviews and
admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k,
maintains a stream of test scores and continuously
returns the kth highest test score after a new score has been submitted.
More specifically,
we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer
k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and
returns the element representing
the kth largest element in the pool of test scores so far.

"""

from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]


# Test cases
if __name__ == "__main__":
    # Test case 1: Example from problem description
    print("Test case 1:")
    kthLargest1 = KthLargest(3, [4, 5, 8, 2])
    assert kthLargest1.add(3) == 4, "Failed: Expected 4"
    assert kthLargest1.add(5) == 5, "Failed: Expected 5"
    assert kthLargest1.add(10) == 5, "Failed: Expected 5"
    assert kthLargest1.add(9) == 8, "Failed: Expected 8"
    assert kthLargest1.add(4) == 8, "Failed: Expected 8"
    print("✓ Passed")

    # Test case 2: k=1 (always return the maximum)
    print("Test case 2:")
    kthLargest2 = KthLargest(1, [1, 2, 3])
    assert kthLargest2.add(4) == 4, "Failed: Expected 4"
    assert kthLargest2.add(0) == 4, "Failed: Expected 4"
    assert kthLargest2.add(5) == 5, "Failed: Expected 5"
    print("✓ Passed")

    # Test case 3: k larger than initial array size
    print("Test case 3:")
    kthLargest3 = KthLargest(3, [5, -1])
    # [-1,2,5], 3rd largest = -1
    assert kthLargest3.add(2) == -1, "Failed: Expected -1"
    # [-1,1,2,5], 3rd largest = 1
    assert kthLargest3.add(1) == 1, "Failed: Expected 1"
    assert (
        kthLargest3.add(-1) == 1
    ), "Failed: Expected 1"  # [-1,-1,1,2,5], 3rd largest = 1
    assert (
        kthLargest3.add(3) == 2
    ), "Failed: Expected 2"  # [-1,-1,1,2,3,5], 3rd largest = 2
    print("✓ Passed")

    # Test case 4: k=4 with larger numbers
    print("Test case 4:")
    kthLargest4 = KthLargest(4, [7, 7, 7, 7, 8, 3])
    assert kthLargest4.add(2) == 7, "Failed: Expected 7"
    assert kthLargest4.add(10) == 7, "Failed: Expected 7"
    assert kthLargest4.add(9) == 7, "Failed: Expected 7"
    assert kthLargest4.add(9) == 8, "Failed: Expected 8"
    print("✓ Passed")

    # Test case 5: Single element
    print("Test case 5:")
    kthLargest5 = KthLargest(1, [5])
    assert kthLargest5.add(3) == 5, "Failed: Expected 5"
    assert kthLargest5.add(10) == 10, "Failed: Expected 10"
    assert kthLargest5.add(7) == 10, "Failed: Expected 10"
    print("✓ Passed")

    # Test case 6: k equals array size
    print("Test case 6:")
    kthLargest6 = KthLargest(3, [1, 2, 3])
    assert kthLargest6.add(0) == 1, "Failed: Expected 1"
    assert kthLargest6.add(4) == 2, "Failed: Expected 2"
    assert kthLargest6.add(5) == 3, "Failed: Expected 3"
    print("✓ Passed")

    print("\n🎉 All test cases passed!")
