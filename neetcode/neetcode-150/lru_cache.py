"""
Design a data structure that follows the constraints of
a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize
the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists,
otherwise return -1.
void put(int key, int value) Update the value of the key
if the key exists.
Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation,
evict the least recently used key.
The functions get and put must each run in O(1)
average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""

import unittest


class ListNode:
    def __init__(self, key=None, value=None, next=None, previous=None):
        self.key = key
        self.value = value
        self.next = next
        self.previous = previous


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.previous = self.head

    def __add_node(self, node: ListNode):
        node.previous = self.head
        node.next = self.head.next
        self.head.next.previous = node
        self.head.next = node

    # Remove node khỏi linked list
    def __remove_node(self, node: ListNode):
        prev_node = node.previous
        next_node = node.next
        prev_node.next = next_node
        next_node.previous = prev_node

    # Di chuyển node lên đầu list (sau head)
    def __move_to_head(self, node: ListNode):
        self.__remove_node(node)
        self.__add_node(node)

    # Xoá node cuối cùng (trước tail) và trả về node đó
    def __pop_tail(self):
        node = self.tail.previous
        self.__remove_node(node)
        self.data.pop(node.key)
        return node

    def get(self, key: int) -> int:

        # get value from key
        node = self.data.get(key)
        if not node:
            return -1

        # move node to head
        self.__move_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        node = self.data.get(key)

        # check if key not exist
        if not node:

            # add to new list
            node = ListNode(value=value, key=key)
            self.__add_node(node)

            self.data[key] = node

            if len(self.data) > self.capacity:
                # remove tail node
                self.__pop_tail()

        # ------

        # Key is existed
        else:

            # move node to head and update value of node:

            # move node to head
            self.__move_to_head(node)
            # update value of node
            node.value = value


class TestLRUCache(unittest.TestCase):

    def test_run_1(self):
        """Test case 1: Example from problem description"""
        lru = LRUCache(2)

        lru.put(1, 1)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), 1)  # returns 1

        lru.put(3, 3)  # evicts key 2
        self.assertEqual(lru.get(2), -1)  # returns -1 (not found)

        lru.put(4, 4)  # evicts key 1
        self.assertEqual(lru.get(1), -1)  # returns -1 (not found)
        self.assertEqual(lru.get(3), 3)  # returns 3
        self.assertEqual(lru.get(4), 4)  # returns 4

    def test_run_2(self):
        """Test case 2: Update existing key"""
        lru = LRUCache(2)

        lru.put(1, 1)
        lru.put(2, 2)
        lru.put(1, 10)  # update key 1 with new value

        self.assertEqual(lru.get(1), 10)  # returns 10 (updated value)
        self.assertEqual(lru.get(2), 2)  # returns 2

        lru.put(3, 3)  # should evict key 2 (since 1 was recently used)
        self.assertEqual(lru.get(2), 2)  # returns 2 (still there)
        self.assertEqual(lru.get(1), -1)  # returns -1 (evicted)
        self.assertEqual(lru.get(3), 3)  # returns 3

    def test_run_3(self):
        """Test case 3: Single capacity cache"""
        lru = LRUCache(1)

        lru.put(1, 1)
        self.assertEqual(lru.get(1), 1)  # returns 1

        lru.put(2, 2)  # evicts key 1
        self.assertEqual(lru.get(1), -1)  # returns -1 (evicted)
        self.assertEqual(lru.get(2), 2)  # returns 2


def manual_test():
    """Manual testing with detailed output"""

    print("=" * 50)
    print("LRU CACHE - TEST CASES")
    print("=" * 50)

    # Test 1: Example from problem description
    print("Test 1: Example from problem description")
    lru1 = LRUCache(2)

    print("  Operations:")
    print("    lru.put(1, 1)")
    lru1.put(1, 1)

    print("    lru.put(2, 2)")
    lru1.put(2, 2)

    result = lru1.get(1)
    print(f"    lru.get(1) → {result} (expected: 1)")

    print("    lru.put(3, 3)  # evicts key 2")
    lru1.put(3, 3)

    result = lru1.get(2)
    print(f"    lru.get(2) → {result} (expected: -1)")

    print("    lru.put(4, 4)  # evicts key 1")
    lru1.put(4, 4)

    result = lru1.get(1)
    print(f"    lru.get(1) → {result} (expected: -1)")

    result = lru1.get(3)
    print(f"    lru.get(3) → {result} (expected: 3)")

    result = lru1.get(4)
    print(f"    lru.get(4) → {result} (expected: 4)")

    print("  ✅ PASSED")
    print()

    # Test 2: Update existing key
    print("Test 2: Update existing key")
    lru2 = LRUCache(2)

    print("  Operations:")
    print("    lru.put(1, 1)")
    lru2.put(1, 1)

    print("    lru.put(2, 2)")
    lru2.put(2, 2)

    print("    lru.put(1, 10)  # update key 1")
    lru2.put(1, 10)

    result = lru2.get(1)
    print(f"    lru.get(1) → {result} (expected: 10)")

    result = lru2.get(2)
    print(f"    lru.get(2) → {result} (expected: 2)")

    print("    lru.put(3, 3)  # evicts key 2")
    lru2.put(3, 3)

    result = lru2.get(2)
    print(f"    lru.get(2) → {result} (expected: -1)")

    result = lru2.get(1)
    print(f"    lru.get(1) → {result} (expected: 10)")

    result = lru2.get(3)
    print(f"    lru.get(3) → {result} (expected: 3)")

    print("  ✅ PASSED")
    print()

    # Test 3: Single capacity cache
    print("Test 3: Single capacity cache")
    lru3 = LRUCache(1)

    print("  Operations:")
    print("    lru.put(1, 1)")
    lru3.put(1, 1)

    result = lru3.get(1)
    print(f"    lru.get(1) → {result} (expected: 1)")

    print("    lru.put(2, 2)  # evicts key 1")
    lru3.put(2, 2)

    result = lru3.get(1)
    print(f"    lru.get(1) → {result} (expected: -1)")

    result = lru3.get(2)
    print(f"    lru.get(2) → {result} (expected: 2)")

    print("  ✅ PASSED")
    print()

    # Test 4: Get operation updates position
    print("Test 4: Get operation updates position")
    lru4 = LRUCache(2)

    print("  Operations:")
    print("    lru.put(1, 1)")
    lru4.put(1, 1)

    print("    lru.put(2, 2)")
    lru4.put(2, 2)

    print("    lru.get(1)  # moves key 1 to front")
    result = lru4.get(1)
    print(f"    → {result}")

    print("    lru.put(3, 3)  # should evict key 2 (not 1)")
    lru4.put(3, 3)

    result = lru4.get(2)
    print(f"    lru.get(2) → {result} (expected: -1, key 2 evicted)")

    result = lru4.get(1)
    print(f"    lru.get(1) → {result} (expected: 1, key 1 still there)")

    print("  ✅ PASSED")
    print()

    # Test 5: Larger capacity
    print("Test 5: Larger capacity")
    lru5 = LRUCache(3)

    print("  Operations:")
    for i in range(1, 4):
        print(f"    lru.put({i}, {i*10})")
        lru5.put(i, i * 10)

    for i in range(1, 4):
        result = lru5.get(i)
        print(f"    lru.get({i}) → {result} (expected: {i*10})")

    print("    lru.put(4, 40)  # evicts key 1 (least recently used)")
    lru5.put(4, 40)

    result = lru5.get(1)
    print(f"    lru.get(1) → {result} (expected: -1, evicted)")

    result = lru5.get(4)
    print(f"    lru.get(4) → {result} (expected: 40)")

    print("  ✅ PASSED")


if __name__ == "__main__":
    # Run unittest cases
    unittest.main(argv=[""], verbosity=2, exit=False)

    # print("\n" + "=" * 50)
    # print("MANUAL TEST RESULTS")
    # print("=" * 50)

    # # Run manual tests
    # manual_test()
