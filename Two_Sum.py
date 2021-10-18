class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}  
        
        for i, v in enumerate(nums):
            trace = target - v 
            
            if trace in dict_ :
                return dict_[trace], i
            
            dict_[v] = i
