class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_ = {}  
        
        for i, v in enumerate(nums):
            trace = target - v 
            
            if trace in set_ :
                return set_[trace], i
            
            set_[v] = i
