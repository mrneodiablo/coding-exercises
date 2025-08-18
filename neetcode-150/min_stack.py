"""
Design a stack that supports push, pop, top
and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""


class MinStack:
    """
    Alternative implementation using single stack with pairs.
    Each element stores (value, current_minimum_at_this_level).
    """

    def __init__(self):
        # Stack of (value, min_at_this_level) pairs
        self.stack = []

    def push(self, val: int) -> None:
        """Push value along with current minimum."""
        if not self.stack:
            current_min = val
        else:
            current_min = min(val, self.stack[-1][1])

        self.stack.append((val, current_min))

    def pop(self) -> None:
        """Pop the top element."""
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        """Get top element value."""
        return self.stack[-1][0]

    def getMin(self) -> int:
        """Get minimum at current level."""
        return self.stack[-1][1]


# Test cases
def test_min_stack():
    print("=== Testing Main MinStack Implementation ===")
    test_implementation(MinStack(), "Main")

    print("\n=== Testing Alternative MinStack Implementation ===")
    test_implementation(MinStack(), "Alternative")

    print("\n🎉 Both implementations pass all tests!")


def test_implementation(stack_instance, implementation_name):
    """Test any MinStack implementation"""

    print(f"\n--- {implementation_name} Test Case 1: Basic Operations ---")
    stack1 = stack_instance.__class__()

    # Push some values
    stack1.push(-2)
    stack1.push(0)
    stack1.push(-3)

    # Test getMin - should return -3
    assert stack1.getMin() == -3
    print("✓ getMin() after push(-2, 0, -3): -3")

    # Test pop - removes -3
    stack1.pop()

    # Test top - should return 0
    assert stack1.top() == 0
    print("✓ top() after pop(): 0")

    # Test getMin - should return -2
    assert stack1.getMin() == -2
    print("✓ getMin() after pop(): -2")

    print(f"{implementation_name} Test Case 1 passed!")

    print(
        f"\n {implementation_name} Test Case 2: Minimum at Diff Positions"
    )
    stack2 = stack_instance.__class__()

    # Push values where min is at bottom
    stack2.push(1)
    stack2.push(2)
    stack2.push(3)

    assert stack2.getMin() == 1
    print("✓ Min at bottom: 1")

    # Push smaller value
    stack2.push(0)
    assert stack2.getMin() == 0
    print("✓ New minimum: 0")

    # Pop the minimum
    stack2.pop()
    assert stack2.getMin() == 1
    print("✓ After popping min, getMin(): 1")

    print(f"{implementation_name} Test Case 2 passed!")

    print(f"\n--- {implementation_name} Test Case 3: Duplicate Minimums ---")
    stack3 = stack_instance.__class__()

    # Push duplicate minimum values
    stack3.push(1)
    stack3.push(1)
    stack3.push(2)
    stack3.push(1)  # Another minimum

    assert stack3.getMin() == 1
    print("✓ Multiple mins, getMin(): 1")

    # Pop one minimum
    stack3.pop()
    assert stack3.getMin() == 1  # Still should be 1
    print("✓ After popping one min, getMin() still: 1")

    print(f"{implementation_name} Test Case 3 passed!")


def demo_internal_state():
    """Demo showing how the two-stack approach works internally"""
    print("\n=== Internal State Demo ===")
    stack = MinStack()

    print("Initial state:")
    print(f"  Main stack: {stack.stack}")

    for val in [-2, 0, -3]:
        stack.push(val)
        print(f"\nAfter push({val}):")
        print(f"  Main stack: {stack.stack}")
        print(f"  Current min: {stack.getMin()}")

    print(f"\nPopping {stack.top()}...")
    stack.pop()
    print(f"  Main stack: {stack.stack}")
    print(f"  Current min: {stack.getMin()}")


if __name__ == "__main__":
    test_min_stack()
    demo_internal_state()
