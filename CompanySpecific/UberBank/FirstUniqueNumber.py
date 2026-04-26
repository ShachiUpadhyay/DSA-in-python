#https://leetcode.com/problems/first-unique-number/description/?envType=company&envId=uber&favoriteSlug=uber-thirty-days

# 

from collections import OrderedDict


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.od = OrderedDict()
        self.seen = set()
        for item in nums:
            if item in self.od:
                self.od.pop(item)
                self.seen.add(item)
            else:
                if item not in self.seen:
                    self.od[item] = None

    def showFirstUnique(self) -> int:
        if not self.od:
            return -1
        else:
            return next(iter(self.od))
        

    def add(self, value: int) -> None:
        if value in self.od:
            self.od.pop(value)
            self.seen.add(value)
        else:
            if value not in self.seen:
                self.od[value] = None
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)