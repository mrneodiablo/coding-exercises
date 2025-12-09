"""
Time Based Key-Value Store
Design a time-based key-value data structure that
can store multiple values for the same key at different time stamps
and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp)
Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp)
Returns a value such that set was called previously,
with timestamp_prev <= timestamp.
If there are multiple such values,
it returns the value associated with the largest timestamp_prev.
If there are no values, it returns "".


Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1],
["foo", 1],
["foo", 3],
["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar",
since there is no value corresponding to foo at timestamp 3 and timestamp 2,
then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4);
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
"""

import unittest


class TimeMap:
    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.data.get(key):
            self.data[key] = [(timestamp, value)]
        else:
            self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.data.get(key):
            return ""

        data = self.data.get(key)
        left = 0
        right = len(data) - 1
        while left <= right:
            middle = (left+right)//2

            if data[middle][0] <= timestamp:
                left = middle + 1
            elif data[middle][0] > timestamp:
                right = middle - 1
            else:
                return data[middle][1]
        if right < 0:
            return ""
        return data[right][1]


class TestFunctions(unittest.TestCase):
    def test_run_1(self):
        # Test case 1: Basic functionality from the example
        timeMap = TimeMap()
        timeMap.set("foo", "bar", 1)
        self.assertEqual(timeMap.get("foo", 1),
                         "bar",
                         "Should return 'bar' for exact timestamp match")
        self.assertEqual(timeMap.get("foo", 3),
                         "bar",
                         "Should return 'bar' for timestamp > stored "
                         "timestamp")

        timeMap.set("foo", "bar2", 4)
        self.assertEqual(timeMap.get("foo", 4),
                         "bar2",
                         "Should return 'bar2' for exact timestamp match")
        self.assertEqual(timeMap.get("foo", 5),
                         "bar2",
                         "Should return 'bar2' for timestamp > stored "
                         "timestamp")

    def test_run_2(self):
        # Test case 2: Edge cases - non-existent key and early timestamps
        timeMap = TimeMap()
        self.assertEqual(timeMap.get("nonexistent", 1),
                         "",
                         "Should return empty string for non-existent key")

        timeMap.set("love", "high", 10)
        timeMap.set("love", "low", 20)
        self.assertEqual(timeMap.get("love", 5),
                         "",
                         "Should return empty string for timestamp before "
                         "any stored value")
        self.assertEqual(timeMap.get("love", 10),
                         "high",
                         "Should return 'high' for exact timestamp match")
        self.assertEqual(timeMap.get("love", 15),
                         "high",
                         "Should return 'high' for timestamp between "
                         "stored values")
        self.assertEqual(timeMap.get("love", 20),
                         "low",
                         "Should return 'low' for exact timestamp match")
        self.assertEqual(timeMap.get("love", 25),
                         "low",
                         "Should return 'low' for timestamp after last "
                         "stored value")

    def test_run_3(self):
        # Test case 3: Multiple keys and complex timestamp scenarios
        timeMap = TimeMap()

        # Set up multiple keys with different timestamps
        timeMap.set("key1", "value1", 1)
        timeMap.set("key1", "value2", 3)
        timeMap.set("key1", "value3", 5)

        timeMap.set("key2", "a", 2)
        timeMap.set("key2", "b", 4)
        timeMap.set("key2", "c", 6)

        # Test key1
        self.assertEqual(timeMap.get("key1", 1), "value1",
                         "Should return 'value1' for timestamp 1")
        self.assertEqual(timeMap.get("key1", 2), "value1",
                         "Should return 'value1' for timestamp 2")
        self.assertEqual(timeMap.get("key1", 3), "value2",
                         "Should return 'value2' for timestamp 3")
        self.assertEqual(timeMap.get("key1", 4), "value2",
                         "Should return 'value2' for timestamp 4")
        self.assertEqual(timeMap.get("key1", 5), "value3",
                         "Should return 'value3' for timestamp 5")
        self.assertEqual(timeMap.get("key1", 10), "value3",
                         "Should return 'value3' for timestamp 10")

        # Test key2
        self.assertEqual(timeMap.get("key2", 1), "",
                         "Should return empty string for timestamp before "
                         "first value")
        self.assertEqual(timeMap.get("key2", 2), "a",
                         "Should return 'a' for timestamp 2")
        self.assertEqual(timeMap.get("key2", 3), "a",
                         "Should return 'a' for timestamp 3")
        self.assertEqual(timeMap.get("key2", 4), "b",
                         "Should return 'b' for timestamp 4")
        self.assertEqual(timeMap.get("key2", 5), "b",
                         "Should return 'b' for timestamp 5")
        self.assertEqual(timeMap.get("key2", 6), "c",
                         "Should return 'c' for timestamp 6")


def test_time_map():
    """Alternative test function for manual testing"""
    print("Test 1: Basic TimeMap functionality")
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    result1 = timeMap.get("foo", 1)
    result2 = timeMap.get("foo", 3)
    timeMap.set("foo", "bar2", 4)
    result3 = timeMap.get("foo", 4)
    result4 = timeMap.get("foo", 5)

    print(f"  set('foo', 'bar', 1), get('foo', 1): Expected 'bar', "
          f"Got '{result1}' ✅ {'PASSED' if result1 == 'bar' else 'FAILED'}")
    print(f"  get('foo', 3): Expected 'bar', Got '{result2}' ✅ "
          f"{'PASSED' if result2 == 'bar' else 'FAILED'}")
    print(f"  set('foo', 'bar2', 4), get('foo', 4): Expected 'bar2', "
          f"Got '{result3}' ✅ {'PASSED' if result3 == 'bar2' else 'FAILED'}")
    print(f"  get('foo', 5): Expected 'bar2', Got '{result4}' ✅ "
          f"{'PASSED' if result4 == 'bar2' else 'FAILED'}")
    print()

    print("Test 2: Edge cases")
    timeMap2 = TimeMap()
    result5 = timeMap2.get("nonexistent", 1)
    timeMap2.set("love", "high", 10)
    result6 = timeMap2.get("love", 5)
    result7 = timeMap2.get("love", 15)

    print(f"  get('nonexistent', 1): Expected '', Got '{result5}' ✅ "
          f"{'PASSED' if result5 == '' else 'FAILED'}")
    print(f"  set('love', 'high', 10), get('love', 5): Expected '', "
          f"Got '{result6}' ✅ {'PASSED' if result6 == '' else 'FAILED'}")
    print(f"  get('love', 15): Expected 'high', Got '{result7}' ✅ "
          f"{'PASSED' if result7 == 'high' else 'FAILED'}")
    print()

    print("Test 3: Multiple timestamps")
    timeMap3 = TimeMap()
    timeMap3.set("key1", "value1", 1)
    timeMap3.set("key1", "value2", 3)
    timeMap3.set("key1", "value3", 5)

    result8 = timeMap3.get("key1", 2)
    result9 = timeMap3.get("key1", 4)
    result10 = timeMap3.get("key1", 10)

    print(f"  Multiple sets, get('key1', 2): Expected 'value1', "
          f"Got '{result8}' ✅ "
          f"{'PASSED' if result8 == 'value1' else 'FAILED'}")
    print(f"  get('key1', 4): Expected 'value2', Got '{result9}' ✅ "
          f"{'PASSED' if result9 == 'value2' else 'FAILED'}")
    print(f"  get('key1', 10): Expected 'value3', Got '{result10}' ✅ "
          f"{'PASSED' if result10 == 'value3' else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

    # Run manual tests
    print("\n" + "="*50)
    test_time_map()
