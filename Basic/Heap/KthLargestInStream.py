
import heapq
from typing import List

class KthLargest:


    def __init__(self, k: int, nums: List[int]):
        self.minheap: List[int] = []
        self.maxheap: List[int] = []
        self.k = k
        for num in nums:
            heapq.heappush(self.minheap, num)
            while len(self.minheap) > k:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
                
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        while len(self.minheap) > self.k:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        if len(self.minheap) < self.k:
            return -1
        else:
            return self.minheap[0]


if __name__ == "__main__":
    # Test 1: Example from LeetCode
    kth = KthLargest(3, [4, 5, 8, 2])
    print("Test 1:")
    print(kth.add(3), "Expected: 4")
    print(kth.add(5), "Expected: 5")
    print(kth.add(10), "Expected: 5")
    print(kth.add(9), "Expected: 8")
    print(kth.add(4), "Expected: 8")

    # Test 2: k larger than initial list
    kth2 = KthLargest(5, [2, 1])
    print("\nTest 2:")
    print(kth2.add(3), "Expected: -1")
    print(kth2.add(4), "Expected: -1")
    print(kth2.add(5), "Expected: 1")
    print(kth2.add(6), "Expected: 2")
    print(kth2.add(7), "Expected: 3")

    # Test 3: k = 1 (always largest)
    kth3 = KthLargest(1, [5])
    print("\nTest 3:")
    print(kth3.add(2), "Expected: 5")
    print(kth3.add(10), "Expected: 10")
    print(kth3.add(9), "Expected: 10")

