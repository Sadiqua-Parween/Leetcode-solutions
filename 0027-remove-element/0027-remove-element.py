class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for i in nums:
            if i != val:
                k+=1
        for i in range(k):
            for j in range(k ,len(nums)):
                if nums[i] == val:
                    if nums[j] != val:
                        nums[i], nums[j] = nums[j] , nums[i]
        return(k)
                
        
        