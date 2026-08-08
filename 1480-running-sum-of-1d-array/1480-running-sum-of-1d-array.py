class Solution(object):
    def runningSum(self, nums):
        sumarr = []
        sum = 0
        for i in range ( 0 , len(nums)) :
            sum = nums[i] + sum
            sumarr.append(sum)
        
        return sumarr 
    

        
        