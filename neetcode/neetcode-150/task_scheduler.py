"""
621. Task Scheduler
You are given an array of CPU tasks,
each labeled with a letter from A to Z, and a number n.
Each CPU interval can be idle or allow the completion of one task.
Tasks can be completed in any order,
but there's a constraint:
there has to be a gap of at least n intervals between
two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is:
A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again.
The same applies to task B. In the 3rd interval, neither A nor B can be done,
so you idle. By the 4th interval,
you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.
"""

import heapq
from typing import List
import unittest

from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # cycle = 0
        # counter = Counter(tasks)
        # cooldown_queue = deque(maxlen=n)

        # while sum(counter.values()) > 0:

        #     candidates = []
        #     for task, cnt in counter.items():
        #         if cnt > 0 and task not in cooldown_queue:
        #             candidates.append(task)

        #     if candidates:
        #         chosen = max(candidates, key=lambda x: counter[x])
        #         counter[chosen] -= 1
        #         cooldown_queue.append(chosen)
        #     else:
        #         cooldown_queue.append("idle")

        #     cycle += 1

        # return cycle

        # Đếm tần suất từng task
        counter = Counter(tasks)
        # Heap lưu các task còn lại (dùng số âm để giả lập max-heap)
        task_heap = [(-count, task) for task, count in counter.items()]
        heapq.heapify(task_heap)
        # Queue quản lý cooldown: (thời điểm unlock, -freq, task)
        cooldown_queue = deque()
        cycle = 0

        while task_heap or cooldown_queue:
            cycle += 1

            # Đưa task hết cooldown về lại heap
            if cooldown_queue and cooldown_queue[0][0] == cycle:
                _, neg_count, task = cooldown_queue.popleft()
                heapq.heappush(task_heap, (neg_count, task))

            if task_heap:
                neg_count, task = heapq.heappop(task_heap)
                # Nếu task còn lặp, đưa vào cooldown
                if -neg_count > 1:
                    cooldown_queue.append((cycle + n + 1, neg_count + 1, task))
                # ... thực hiện 1 đơn vị task này
            # else: không có task == idle

        return cycle


class TestTaskScheduler(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        """Test case 1: Example from problem description
        - requires idle time"""
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        expected = 8
        result = self.solution.leastInterval(tasks, n)
        self.assertEqual(result, expected)

    def test_run_2(self):
        """Test case 2: Example from problem description - minimal cooling"""
        tasks = ["A", "C", "A", "B", "D", "B"]
        n = 1
        expected = 6
        result = self.solution.leastInterval(tasks, n)
        self.assertEqual(result, expected)

    def test_run_3(self):
        """Test case 3: No cooling period needed"""
        tasks = ["A", "B", "C", "D", "E", "F"]
        n = 2
        expected = 6
        result = self.solution.leastInterval(tasks, n)
        self.assertEqual(result, expected)

    def test_run_4(self):
        """Test case 3: No cooling period needed"""
        tasks = ["B", "C", "D", "A", "A", "A", "A", "G"]
        n = 1
        expected = 8
        result = self.solution.leastInterval(tasks, n)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    # Run unittest cases
    unittest.main(argv=[""], verbosity=2, exit=False)
