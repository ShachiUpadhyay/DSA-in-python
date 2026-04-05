class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        n : int = len(nums)
        return self.binary_search(nums, target, 0, n-1)

    def binary_search(self,nums: list[int], target: int, start: int, end: int) -> int:
        if start > end:
            return -1
        mid = (start + end)//2
        if nums[mid] == target:
            return mid
        
        if(nums[mid] < target):
            return self.binary_search(nums, target, mid+1, end) 
        else:
            return self.binary_search(nums, target, start, mid-1)

        
if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    expected = 4
    result = solution.search(nums, target)
    print("Nums:", nums)
    print("Target:", target)
    print("Expected:", expected)
    print("Result:  ", result)
    print("PASS" if result == expected else "FAIL")